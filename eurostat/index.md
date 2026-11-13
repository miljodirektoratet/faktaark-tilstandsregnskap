---
layout: default
title: Eurostat
nav_order: 11
permalink: /eurostat/
has_children: true
okosystem: true
has_toc: false
---

# Faktaark for eurostat
{: .fs-9 }

Faktaark med informasjon om indikatorene for økosystemet eurostat.
{: .fs-6 .fw-300 }

## Indikatorer

{% assign faktaark = site.pages
 | where: "parent", page.title
 | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.title }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}
