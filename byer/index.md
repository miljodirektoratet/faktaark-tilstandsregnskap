---
layout: default
title: Bebygd og opparbeidet areal
nav_order: 4
permalink: /byer/
has_children: true
okosystem: true
has_toc: false
---

# Faktaark for bebygd og opparbeidet areal
{: .fs-9 }

Faktaark med informasjon om indikatorene for økosystemet bebygd og opparbeidet areal.
{: .fs-6 .fw-300 }

## Indikatorer

{% assign faktaark = site.pages
 | where: "parent", page.title
 | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.title }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}
