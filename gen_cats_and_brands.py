#!/usr/bin/env python3
import os
import sys

CAT_FILE = "_data/categories.yml"
BRAND_FILE = "_data/brands.yml"


CONTENT_CAT = """---
layout: default
---

{% assign products=site.products | where:"category", "CAT"%}
<h3> NAME </h3>
<div class="products">
    {% for product in products %}
        <div class="product simpleCart_shelfItem">
            <img class="product-img"src="{{product.img_path}}" alt="">
            <div class="product-data">
                <h4 class="product-name item_name">{{product.title}}</h4>
                <p class="product-description"> {{product.desc}}</p>
                <p class="product-price item_price">{{product.price}}</p>
                <p class="product-category item_category">{{ product.category }}</p>
                <p class="product-brand item_brand">{{ product.brand }}</p>
            </div>
            <input type="number" value="1" class="item_Quantity">
            <a class="item_add btn_buy" href="javascript:;">Kupi</a>
        </div>
    {% endfor %}
</div>
"""


CONTENT_BRAND = """---
layout: default
---

{% assign products=site.products | where:"brand", "BRAND"%}
<h3> NAME </h3>
<div class="products">
    {% for product in site.products %}
        <div class="product simpleCart_shelfItem">
            <img class="product-img"src="{{product.img_path}}" alt="">
            <div class="product-data">
                <h4 class="product-name item_name">{{product.title}}</h4>
                <p class="product-description"> {{product.desc}}</p>
                <p class="product-price item_price">{{product.price}}</p>
                <p class="product-category item_category">{{ product.category }}</p>
                <p class="product-brand item_brand">{{ product.brand }}</p>
            </div>
            <input type="number" value="1" class="item_Quantity">
            <a class="item_add btn_buy" href="javascript:;">Kupi</a>
        </div>
    {% endfor %}
</div>
"""

cats = open(CAT_FILE, "r")
brands = open(BRAND_FILE, "r")

for line in cats.readlines():
	if "name" in line:
		name = line.split('"')[1]
		content = CONTENT_CAT
		content = content.replace("CAT", name)
		content = content.replace("NAME", name.capitalize())
		name  = name.replace(" ", "_")
		out = open("{}.html".format(name), "w")
		out.write(content)


for line in brands.readlines():
	if "name" in line:
		name = line.split('"')[1]
		content = CONTENT_BRAND
		content = content.replace("BRAND", name)
		content = content.replace("NAME", name.capitalize())
		name  = name.replace(" ", "_")
		out = open("{}.html".format(name), "w")
		out.write(content)

