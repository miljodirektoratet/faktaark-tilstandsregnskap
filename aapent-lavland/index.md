---
layout: default
title: Åpent lavland
nav_order: 6
permalink: /aapent-lavland/
has_children: true
okosystem: true
has_toc: false
---

# Faktaark for åpent lavland
{: .fs-9 }

Faktaark med informasjon om indikatorene for økosystemet åpent lavland.
{: .fs-6 .fw-300 }

## Indikatorer

{% assign faktaark = site.pages
 | where: "parent", page.title
 | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.title }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}
