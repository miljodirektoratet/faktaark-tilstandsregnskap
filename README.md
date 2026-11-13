# Faktaark for tilstandsregnskap

Faktaark med informasjon om indikatorene i nasjonalt tilstandsregnskap.

**Nettside:** https://miljodirektoratet.github.io/faktaark-tilstandsregnskap/


## Legg inn et nytt faktaark

Alt kan gjøres i nettleseren. Nettsiden oppdateres først når endringene er godkjent og merget til `main`.


### 1. Legg inn PDF-filene og lag ny branch

1. Gå til mappen `assets/pdf/` og velg **Add file** > **Upload files**.
2. Last opp PDF-ene. Filnavnet skal være indikatorkoden, for eksempel `NO_NIPR_002.pdf`.
3. Nederst på siden velger du **Create a new branch for this commit and start a pull request**. Gi branchen et kort navn, for eksempel `faktaark-skog`.
4. Trykk **Propose changes** og deretter **Create pull request**.

**Viktig:** Filnavnet må være det samme som verdien som ligger i kolonnen "kode" excel-arket i data/faktaark.xlsx. Dette blir automatisk `kode` i Markdown-filen. PDF-en kobles automatisk til riktig indikatorside ved hjelp av denne koden.


### 2. Last opp regnearket

1. Gå tilbake til forsiden av repoet.
2. Gå til data/ og klikk på faktaark.xlsx. Last ned filen, åpne den i excel, og legg inn nye rader nederst. Lagre filen.
4. Pass på at du står i branchen din. Gå til mappen `data/`, velg **Add file** > **Upload files** og last opp den nye filen. Med samme navn vil den erstatte den gamle. 
5. Velg **Commit directly to the `faktaark-skog` branch** og trykk **Commit changes**.

> Sjekk at det står navnet på branchen din, og ikke `main`, før du laster opp.

Alternativt, hvis det ligger en oppdatert versjon av filen på sharepoint, kan du bare laste opp den. Ingenting slettes hvis noe av det som allerede ligger på nettsiden mangler i excel-arket, men det er allikevel ryddigst at alle filene som er lastet opp også har en rad i excel-arket. 

Regnearket har én rad per faktaark:

| title | parent | okosystem | kode | nav_order |
| --- | --- | --- | --- | --- |
| Oter | Elver, bekker og kanaler | elver | NO_NIPR_002 | 13 |

- **title**: Navnet på indikatoren slik det skal vises på nettsiden.
- **parent**: Navnet på økosystemet. Det må være skrevet helt likt på alle rader for samme økosystem.
- **okosystem**: Kortnavnet til økosystemet. Det blir mappenavn og en del av nettadressen. Bruk bare små bokstaver a–z, tall og bindestrek.
- **kode**: Indikator-ID. Den må være lik navnet på PDF-filen, uten `.pdf`.
- **nav_order**: Rekkefølgen indikatoren vises i under økosystemet.

Samme indikator kan ligge under flere økosystemer. Da får den én rad per økosystem.

### 3. Vent på at sidene lages

Åpne fanen **Actions** for å følge med:

- **Grønn hake**: Sidene er laget og lagt inn i pull requesten din.
- **Rødt kryss**: Noe i regnearket må rettes. Klikk på kjøringen for å se hvilken rad det gjelder. Rett regnearket og last det opp på nytt, som i steg 2.
- **Gul advarsel**: Sidene er laget, men noe bør sjekkes, for eksempel en PDF som mangler.

Nye økosystemer får automatisk en egen side.


### 4. Kontroller og merge

1. Åpne pull requesten og se under **Files changed** at alt ser riktig ut.
2. Trykk **Merge pull request** og bekreft. Nettsiden oppdateres etter noen minutter.
3. Trykk **Delete branch**.

### 5. Sjekk nettsiden

Kontroller at:

- indikatoren vises under riktig økosystem
- navn og indikator-ID er riktige
- riktig PDF vises, og **Åpne faktaarket i ny fane** fungerer

## Greit å vite

- Regnearket kan inneholde alle faktaarkene eller bare de nye. Ingenting blir slettet. Men det er ryddigst at alt ligger der. 
- Sider for økosystemer som finnes fra før blir aldri endret.
- Små rettelser kan gjøres direkte på `main`.


## Slik er nettsiden bygget opp

Nettsiden har én side per økosystem, og under hver av dem én side per indikator. Hver indikatorside viser faktaarket som PDF.

Nettsiden oppdateres automatisk hver gang noe merges til `main`.

## Oversikt over repoet

| Mappe eller fil | Innhold |
| --- | --- |
| `assets/pdf/` | Faktaarkene som PDF. Filnavnet er indikatorkoden, for eksempel `NO_NIPR_002.pdf`. |
| `data/faktaark.xlsx` | Regnearket med alle faktaarkene. Sidene lages fra dette. |
| `elver/`, `skog/` osv. | Én mappe per økosystem, med `index.md` for økosystemsiden og én `.md`-fil per indikator. Disse lages automatisk. |
| `_layouts/faktaark.html` | Malen for hvordan en indikatorside ser ut. |
| `_config.yml` | Innstillinger for nettsiden. |
| `scripts/` og `.github/workflows/` | Automatikken som lager sidene fra regnearket. Trenger normalt ikke endres. |

## Slik henger det sammen

- **kode → PDF:** `kode: NO_NIPR_002` gjør at siden viser `assets/pdf/NO_NIPR_002.pdf`.
- **parent → økosystem:** `parent: Elver, bekker og kanaler` plasserer siden under økosystemsiden med samme `title`.

## Endre eller fjerne

- **Rette navn eller rekkefølge for en indikator:** Endre raden i regnearket og last det opp på nytt. Små rettelser kan også gjøres direkte i `.md`-filen.
- **Bytte ut en PDF:** Last opp den nye PDF-en med samme filnavn. Den gamle erstattes.
- **Endre en økosystemside** (navn, rekkefølge, tekst): Rediger `index.md` i økosystemets mappe direkte. Den blir ikke endret automatisk. Hvis du endrer `title`, må `parent` endres tilsvarende i regnearket.
- **Fjerne en indikator:** Slett raden i regnearket. Slett også `.md`-filen og PDF-en manuelt, fordi ingenting slettes automatisk.

## Hvis noe går galt

- **Rødt kryss under Actions:** Klikk på kjøringen. Feilmeldingen sier hvilken rad i regnearket som må rettes.
- **Indikatoren havner ikke under riktig økosystem:** Sjekk at `parent` er skrevet helt likt som `title` i økosystemets `index.md`.
- **PDF-en vises ikke:** Sjekk at PDF-filen heter nøyaktig det samme som koden, også med store og små bokstaver.

Spørsmål: [Margrethe Gaardløs / margrethe.gaardlos@miljodir.no]
