#!/usr/bin/env python3
"""
Genererer faktaark-sider fra data/faktaark.xlsx (første ark).

Kolonner: title | parent | okosystem | kode | nav_order
  -> <okosystem>/<kode>.md   (opprettes/oppdateres)
  -> <okosystem>/index.md    (opprettes kun hvis den mangler)

Kjøres fra roten av repoet:  python scripts/generer_faktaark.py
"""
import argparse
import re
import sys
from pathlib import Path

import yaml
from openpyxl import load_workbook

KOLONNER = ["title", "parent", "okosystem", "kode", "nav_order"]
PDF_MAPPE = Path("assets/pdf")

INDEX_TEKST = """
# Faktaark for __NAVN__
{: .fs-9 }

Faktaark med informasjon om indikatorene for økosystemet __NAVN__.
{: .fs-6 .fw-300 }

## Indikatorer

{% assign faktaark = site.pages
 | where: "parent", page.title
 | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.title }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}
"""

feil, advarsler = [], []


def rens(v):
    if isinstance(v, float) and v.is_integer():
        return int(v)
    if isinstance(v, str):
        v = v.strip()
        return v or None
    return v


def les_rader(ws):
    rader = ws.iter_rows(values_only=True)
    headere = [str(h).strip().lower() if h is not None else None for h in next(rader, [])]
    mangler = [k for k in KOLONNER if k not in headere]
    if mangler:
        feil.append(f"Excel-arket mangler kolonne(r): {', '.join(mangler)}")
        return []
    ut = []
    for radnr, rad in enumerate(rader, start=2):
        d = {h: rens(v) for h, v in zip(headere, rad) if h in KOLONNER}
        if all(d.get(k) is None for k in KOLONNER):
            continue  # tom rad
        for k in KOLONNER:
            if d.get(k) is None:
                feil.append(f"Rad {radnr}: '{k}' er tom.")
        if d.get("nav_order") is not None and not isinstance(d["nav_order"], int):
            feil.append(f"Rad {radnr}: nav_order må være et heltall (fikk '{d['nav_order']}').")
        for k in ("okosystem", "kode"):
            if d.get(k) is not None:
                d[k] = str(d[k])
        ut.append((radnr, d))
    return ut


def les_front_matter(fil):
    try:
        tekst = fil.read_text(encoding="utf-8")
        if tekst.startswith("---"):
            return yaml.safe_load(tekst.split("---", 2)[1]) or {}
    except Exception:
        pass
    return {}


def front_matter(d):
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=1000) + "---\n"


def skriv(fil, innhold, endringer):
    if fil.exists() and fil.read_text(encoding="utf-8") == innhold:
        return
    status = "oppdatert" if fil.exists() else "ny"
    fil.parent.mkdir(parents=True, exist_ok=True)
    fil.write_text(innhold, encoding="utf-8")
    endringer.append(f"{status}: {fil.as_posix()}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/faktaark.xlsx")
    p.add_argument("--repo", default=".")
    args = p.parse_args()
    repo = Path(args.repo)

    wb = load_workbook(args.input, data_only=True, read_only=True)
    rader = les_rader(wb.worksheets[0])

    # Eksisterende økosystemer i repoet: mappe -> front matter
    eksisterende = {}
    for index in repo.glob("*/index.md"):
        fm = les_front_matter(index)
        if fm.get("title"):
            eksisterende[index.parent.name] = fm

    # Sjekk at okosystem og parent henger sammen
    mappe_til_parent, parent_til_mappe = {}, {}
    for radnr, d in rader:
        mappe, parent = d.get("okosystem"), d.get("parent")
        if mappe is None or parent is None:
            continue
        if not re.fullmatch(r"[a-z0-9-]+", mappe):
            feil.append(f"Rad {radnr}: okosystem '{mappe}' kan bare ha små bokstaver a-z, tall og bindestrek.")
        if mappe_til_parent.setdefault(mappe, parent) != parent:
            feil.append(f"Rad {radnr}: okosystem '{mappe}' har parent '{parent}', men tidligere rader har '{mappe_til_parent[mappe]}'.")
        if parent_til_mappe.setdefault(parent, mappe) != mappe:
            feil.append(f"Rad {radnr}: parent '{parent}' er brukt med både '{parent_til_mappe[parent]}' og '{mappe}'.")
        if mappe in eksisterende and eksisterende[mappe]["title"] != parent:
            feil.append(f"Rad {radnr}: parent '{parent}' er ikke lik title i {mappe}/index.md ('{eksisterende[mappe]['title']}').")

    # Sjekk koder, PDF-er og rekkefølge
    koder, rekkefolge = set(), {}
    for radnr, d in rader:
        kode, mappe = d.get("kode"), d.get("okosystem")
        if kode is None:
            continue
        if not re.fullmatch(r"[A-Za-z0-9_-]+", kode):
            feil.append(f"Rad {radnr}: kode '{kode}' inneholder ugyldige tegn.")
        if kode in koder:
            feil.append(f"Rad {radnr}: kode '{kode}' står flere ganger.")
        koder.add(kode)
        if not (repo / PDF_MAPPE / f"{kode}.pdf").exists():
            advarsler.append(f"Mangler PDF: {PDF_MAPPE.as_posix()}/{kode}.pdf")
        for annen in repo.glob(f"*/{kode}.md"):
            if annen.parent.name != mappe:
                advarsler.append(f"{kode} finnes også i {annen.as_posix()}; slett den hvis faktaarket er flyttet.")
        if mappe and d.get("nav_order") is not None:
            nokkel = (mappe, d["nav_order"])
            if nokkel in rekkefolge:
                advarsler.append(f"Rad {radnr}: nav_order {d['nav_order']} brukes også av {rekkefolge[nokkel]} i '{mappe}'.")
            rekkefolge[nokkel] = kode

    if feil:
        print("Fant feil i Excel-filen, ingen filer er skrevet:\n")
        for f in feil:
            print(f"::error::{f}")
        sys.exit(1)

    endringer = []

    # Nye økosystemer får neste ledige nav_order
    brukte = [fm["nav_order"] for fm in eksisterende.values() if isinstance(fm.get("nav_order"), int)]
    neste = max(brukte, default=1) + 1
    for mappe, parent in mappe_til_parent.items():
        if mappe in eksisterende:
            continue
        fm = {"layout": "default", "title": parent, "nav_order": neste,
              "permalink": f"/{mappe}/", "has_children": True, "okosystem": True, "has_toc": False}
        navn = parent[:1].lower() + parent[1:]
        skriv(repo / mappe / "index.md", front_matter(fm) + INDEX_TEKST.replace("__NAVN__", navn), endringer)
        advarsler.append(f"Nytt økosystem {mappe}/index.md fikk nav_order {neste}; endre ved behov.")
        neste += 1

    for _, d in rader:
        fm = {"layout": "faktaark", "title": d["title"], "parent": d["parent"],
              "kode": d["kode"], "nav_order": d["nav_order"]}
        skriv(repo / d["okosystem"] / f"{d['kode']}.md", front_matter(fm), endringer)

    for a in advarsler:
        print(f"::warning::{a}")
    print("\n".join(endringer) if endringer else "Ingen endringer.")


if __name__ == "__main__":
    main()
