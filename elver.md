---
layout: default
title: Elver, bekker og kanaler
nav_order: 2
permalink: /elver/
has_children: true
okosystem: true
---

# Faktaark for elver, bekker og kanaler
{: .fs-9 }

Faktaark med informasjon om indikatorene for økosystemet elver, bekker og kanaler.
{: .fs-6 .fw-300 }

## Indikatorer

{% assign faktaark = site.pages
 | where: "parent", page.title
 | sort: "nav_order" %}

{% for ark in faktaark %}
- [{{ ark.indikator }}, {{ ark.kode }}]({{ ark.url | relative_url }})
{% endfor %}
