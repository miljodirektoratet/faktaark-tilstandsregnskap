---
layout: default
title: Fjell
nav_order: 8
permalink: /fjell/
has_children: true
okosystem: true
has_toc: false
---

# Faktaark for fjell
{: .fs-9 }

Faktaark med informasjon om indikatorene for økosystemet fjell.
{: .fs-6 .fw-300 }

## Indikatorer

{% assign faktaark = site.pages
 | where: "parent", page.title
 | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.title }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}
