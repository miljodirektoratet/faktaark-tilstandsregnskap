---
layout: default
title: Kystvann
nav_order: 10
permalink: /kystvann/
has_children: true
okosystem: true
has_toc: false
---

# Faktaark for kystvann
{: .fs-9 }

Kommer snart! Faktaark med informasjon om indikatorene for økosystemet kystvann.
{: .fs-6 .fw-300 }

## Indikatorer

{% assign faktaark = site.pages
 | where: "parent", page.title
 | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.title }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}
