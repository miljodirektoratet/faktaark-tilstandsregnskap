---
layout: default
title: Innsjøer og vannmagasiner
nav_order: 3
permalink: /innsjo/
has_children: true
okosystem: true
has_toc: false
---

# Faktaark for innsjøer og vannmagasiner
{: .fs-9 }

Faktaark med informasjon om indikatorene for innsjøer og vannmagasiner.
{: .fs-6 .fw-300 }

## Indikatorer

{% assign faktaark = site.pages
 | where: "parent", page.title
 | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.title }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}
