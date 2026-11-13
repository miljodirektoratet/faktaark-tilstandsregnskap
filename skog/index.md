---
layout: default
title: Skog
nav_order: 7
permalink: /skog/
has_children: true
okosystem: true
has_toc: false
---

# Faktaark for skog
{: .fs-9 }

Faktaark med informasjon om indikatorene for økosystemet skog.
{: .fs-6 .fw-300 }

## Indikatorer

{% assign faktaark = site.pages
 | where: "parent", page.title
 | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.title }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}
