#!/usr/bin/env python3
import os
import sys

CAT_FILE = "_data/categories.yml"
BRAND_FILE = "_data/brands.yml"


CONTENT_CAT = """
---
layout: default
---

{% assign products=site.products | where:"category", "CAT"%}
{% for product in products %}
	{{product.name}}
	{{product.price}}
	{{product.desc}}
{%  endfor %}
"""

CONTENT_BRAND = """
---
layout: default
---

{% assign products=site.products | where:"brand", "BRAND"%}
{% for product in products %}
	{{product.name}}
	{{product.price}}
	{{product.desc}}
{%  endfor %}
"""

cats = open(CAT_FILE, "r")
brands = open(BRAND_FILE, "r")

for line in cats.readlines():
	if "name" in line:
		name = line.split('"')[1]
		name  = name.replace(" ", "_")
		content = CONTENT_CAT.replace("CAT", name)
		out = open("{}.html".format(name), "w")
		out.write(content)


for line in brands.readlines():
	if "name" in line:
		name = line.split('"')[1]
		name  = name.replace(" ", "_")
		content = CONTENT_BRAND.replace("BRAND", name)
		out = open("{}.html".format(name), "w")
		out.write(content)

