---
layout: default
title: Våtmark
nav_order: 9
permalink: /vaatmark/
has_children: true
okosystem: true
has_toc: false
---

# Faktaark for våtmark
{: .fs-9 }

Faktaark med informasjon om indikatorene for økosystemet våtmark.
{: .fs-6 .fw-300 }

## Indikatorer

{% assign faktaark = site.pages
 | where: "parent", page.title
 | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.title }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}
