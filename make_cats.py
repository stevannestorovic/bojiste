#!/usr/bin/env python3
import yaml 
import os
import sys


def make_breadcrumbs(cname="", sname="", ssname=""):
	html = '<nav class="breadcrumb has-arrow-separator" aria-label="breadcrumbs">'
	html += '<ul>'
	if cname != "":
		html += '<li><a href="{}.html">{}</a></li>'.format(cname.replace(' ', '_'), cname)
	if sname != "":
		html += '<li><a href="{}.html">{}</a></li>'.format(cname.replace(' ', '_') +'_'+ sname.replace(' ', '_'), sname)
	if ssname != "":
		html += '<li><a href="{}.html">{}</a></li>'.format(cname.replace(' ', '_') +'_'+ sname.replace(' ', '_') + ssname.replace(' ', '_'), ssname)
	html += '</ul></nav>'
	return html

def make_seo_title(cname="", sname="", ssname=""):
	seo_name = ""
	if cname != "":
		seo_name += '{} - '.format(cname)
	if sname != "":
		seo_name += '{} '.format( sname)
	if ssname != "":
		seo_name += '- {}'.format(ssname)
	return seo_name

PAGE='''---
layout: default
---
<h1>PATH</h1>

<div class="products">
    {% for product in site.products %}
        <div class="product simpleCart_shelfItem card">
            <img class="product-img"src="{{product.img_path}}" alt="">
            <div class="product-data is-left-txt">
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
title: seo_title
---

<div class="section">
	<div class="container">
	BREADCRUMB
	<div class="products">
		{% for product in site.products  %}
			{% if product.cat == "CNAME" %}
				<div class="product simpleCart_shelfItem">
					<h4 class="product-name item_name card-header-title"><a class="has-text-dark" href="{{product.url}}">{{product.title}}</a></h4>
					<img class="product-img image" src="{{product.img_path}}" alt="">
					<div class="product-data">
						<p class="product-description"> {{product.desc}}</p>
						<strong class="product-price is-main-txt item_price">{{product.price}} <small>RSD</small></strong>
						<p class="product-category item_category">{{ product.category }}</p>
					</div>
					<div class="product-widgets">
						<input type="number" value="1" class="item_Quantity input">
						<a class="item_add button is-main-bg buy_button is-large" href="javascript:;">Kupi</a>
					</div>
				</div>
			{% endif %}
		{% endfor %}
	</div>
	</div>
</div>
'''

SUBCAT_PAGE = '''---
layout: default
title: seo_title
---
<div class="section">
<div class="container">
BREADCRUMB
<div class="products">
    {% for product in site.products %}
		{% if product.cat == "CNAME" and product.subcat == "SNAME"%}
				<div class="product simpleCart_shelfItem">
					<h4 class="product-name item_name card-header-title"><a class="has-text-dark" href="{{product.url}}">{{product.title}}</a></h4>
					<img class="product-img image" src="{{product.img_path}}" alt="">
					<div class="product-data">
						<p class="product-description"> {{product.desc}}</p>
						<strong class="product-price is-main-txt item_price">{{product.price}} <small>RSD</small></strong>
						<p class="product-category item_category">{{ product.category }}</p>
					</div>
					<div class="product-widgets">
						<input type="number" value="1" class="item_Quantity input">
						<a class="item_add button is-main-bg buy_button is-large" href="javascript:;">Kupi</a>
					</div>
				</div>
		{% endif %}
    {% endfor %}
</div>
</div>
</div>
'''


SUBSUBCAT_PAGE = '''---
layout: default
title: seo_title
---

<div class="section">
<div class="container">
BREADCRUMB
<div class="products tile is-ancestor">
    {% for product in site.products %}
		{% if product.cat == "CNAME" and product.subcat == "SNAME" and product.subusbcat == "SSNAME"%}
				<div class="product simpleCart_shelfItem">
					<h4 class="product-name item_name card-header-title"><a class="has-text-dark" href="{{product.url}}">{{product.title}}</a></h4>
					<img class="product-img image" src="{{product.img_path}}" alt="">
					<div class="product-data">
						<p class="product-description"> {{product.desc}}</p>
						<strong class="product-price is-main-txt item_price">{{product.price}} <small>RSD</small></strong>
						<p class="product-category item_category">{{ product.category }}</p>
					</div>
					<div class="product-widgets">
						<input type="number" value="1" class="item_Quantity input">
						<a class="item_add button is-main-bg buy_button is-large" href="javascript:;">Kupi</a>
					</div>
				</div>
		{% endif %}
    {% endfor %}
</div>
</div>
</div>
'''




CATS = ''

with open('_data/cats.yml') as f:
	CATS = yaml.safe_load(f)



print('CATS')
for cat in CATS:
	cname = cat['maincat']
	breadcrumb = make_breadcrumbs(cname=cname)
	seo_title = make_seo_title(cname=cname)
	f = open('{}.html'.format(cat['maincat']).replace(' ', '_'), 'w')
	content = CAT_PAGE.replace('PATH', cat['maincat'])
	content = content.replace('CNAME', cname)
	content = content.replace('BREADCRUMB', breadcrumb)
	content = content.replace('seo_title', seo_title)
	f.write(content)
	f.close()
	print("[+] " + cat['maincat'])

print('CATS->SUBCATS')
for cat in CATS:
	cname = cat['maincat']
	try:
		for subcat in cat['subcats']:
			sname = subcat['name']
			breadcrumb = make_breadcrumbs(cname=cname,sname=sname)
			seo_title = make_seo_title(cname=cname, sname=sname)
			path = '{} {}'.format(cname, sname)
			f = open(path.replace(' ', '_') + '.html', 'w')
			content = SUBCAT_PAGE.replace('PATH', path)
			content = content.replace('CNAME', cname)
			content = content.replace('SNAME', sname)
			content = content.replace('BREADCRUMB', breadcrumb)
			content = content.replace('seo_title', seo_title)
			f.write(content)
			f.close()
			print('[+]' + path)
	except Exception as e:
				print(e)

print('CAT->SUBCATS->SUBSUBCATS')
for cat in CATS:
	cname = cat['maincat']
	try:
		for subcat in cat['subcats']:
			sname = subcat['name']
			try:
				for subsubcat in subcat['subsubcats']:
					ssname = subsubcat
					breadcrumb = make_breadcrumbs(cname=cname,sname=sname, ssname=ssname)
					seo_title = make_seo_title(cname=cname, sname=sname, ssname=ssname)
					path = '{} {} {}'.format(cname, sname, ssname)
					f = open(path.replace(' ', '_') + '.html', 'w')
					content = SUBSUBCAT_PAGE.replace('PATH', path)
					content = content.replace('CNAME', cname)
					content = content.replace('SNAME', sname)
					content = content.replace('SSNAME', ssname)
					content = content.replace('BREADCRUMB', breadcrumb)
					content = content.replace('seo_title', seo_title)
					f.write(content)
					f.close()
					print('[+]' + path)
			except Exception as e:
				print(e)
	except:
		pass

