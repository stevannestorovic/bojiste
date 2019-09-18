#!/usr/bin/env python3
import yaml 
import os
import sys


PAGE='''---
layout: default
---
<h1>PATH</h1>

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
'''

CAT_PAGE = '''---
layout: default
---

<div class="products">
    {% for product in site.products  %}
		{% if product.cat == "CNAME" %}
			<div class="product simpleCart_shelfItem">
				<img class="product-img" src="{{product.img_path}}" alt="">
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
		{% endif %}
    {% endfor %}
</div>
'''

SUBCAT_PAGE = '''---
layout: default
---

<div class="products">
    {% for product in site.products %}
		{% if product.cat == "CNAME" and product.subcat == "SNAME"%}
			<div class="product simpleCart_shelfItem">
				<img class="product-img" src="{{product.img_path}}" alt="">
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
		{% endif %}
    {% endfor %}
</div>
'''


SUBSUBCAT_PAGE = '''---
layout: default
---

<div class="products">
    {% for product in site.products %}
		{% if product.cat == "CNAME" and product.subcat == "SNAME" and product.subusbcat == "SSNAME"%}
			<div class="product simpleCart_shelfItem">
				<img class="product-img" src="{{product.img_path}}" alt="">
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
		{% endif %}
    {% endfor %}
</div>
'''




CATS = ''

with open('_data/cats.yml') as f:
	CATS = yaml.safe_load(f)



print('CATS')
for cat in CATS:
	cname = cat['maincat']
	f = open('{}.html'.format(cat['maincat']).replace(' ', '_'), 'w')
	content = CAT_PAGE.replace('PATH', cat['maincat'])
	content = content.replace('CNAME', cname)
	f.write(content)
	f.close()
	print("[+] " + cat['maincat'])

print('CATS->SUBCATS')
for cat in CATS:
	cname = cat['maincat']
	try:
		for subcat in cat['subcats']:
			sname = subcat['name']
			path = '{} {}'.format(cname, sname)
			f = open(path.replace(' ', '_') + '.html', 'w')
			content = SUBCAT_PAGE.replace('PATH', path)
			content = content.replace('CNAME', cname)
			content = content.replace('SNAME', sname)
			f.write(content)
			f.close()
			print('[+]' + path)
	except:
		pass

print('CAT->SUBCATS->SUBSUBCATS')
for cat in CATS:
	cname = cat['maincat']
	try:
		for subcat in cat['subcats']:
			sname = subcat['name']
			try:
				for subsubcat in subcat['subsubcats']:
					ssname = subsubcat
					path = '{} {} {}'.format(cname, sname, ssname)
					f = open(path.replace(' ', '_') + '.html', 'w')
					content = SUBSUBCAT_PAGE.replace('PATH', path)
					content = content.replace('CNAME', cname)
					content = content.replace('SNAME', sname)
					content = content.replace('SSNAME', ssname)
					f.write(content)
					f.close()
					print('[+]' + path)
			except:
				pass
	except:
		pass

