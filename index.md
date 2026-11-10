---
layout: default
title: Hjem
nav_order: 1
---

# Faktaark for tilstandsregnskap
{: .fs-9 }

Faktaark med informasjon om indikatorene i nasjonalt tilstandsregnskap.
{: .fs-6 .fw-300 }

[Vis på GitHub](https://github.com/miljodirektoratet/faktaark-tilstandsregnskap){: .btn .fs-5 .mb-4 .mb-md-0 }

## Faktaark

### Skaleringsfunksjon
Faktaark som forklarer hvordan vi skalerer indikatorene.
- [Skaleringsfunksjon]({% link faktaark_skaleringsfunksjon.md %})

### Økosystemer

{% assign okosystemer = site.pages | where: "okosystem", true | sort: "nav_order" %}

{% for oko in okosystemer %}

#### [{{ oko.title }}]({{ oko.url | relative_url }})

{% assign faktaark = site.pages | where: "parent", oko.title | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.indikator }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}

{% endfor %}
