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
		html += '<li><a href="{}.html">{}</a></li>'.format(cname.replace(' ', '_') + '_' + sname.replace(' ', '_') + '_' + ssname.replace(' ', '_'), ssname)
	html += '</ul></nav>'
	return html

def make_seo_title(cname="", sname="", ssname=""):
	seo_name = ""
	if cname != "":
		seo_name += '{}'.format(cname)
	if sname != "":
		seo_name += ' - {} '.format( sname)
	if ssname != "":
		seo_name += '- {}'.format(ssname)
	return seo_name




CAT_PAGE = '''---
layout: default
title: seo_title
---
<div class="container">
<div class="sidebar-helper">
<aside> 
    {% include menu_new_side.html %}
</aside>
<section>
<div class="section">
	<div class="container">
	BREADCRUMB
	<div class="filters" data-filter="FILTERS"></div>
    SCRIPT
	<div class="products">
		{% for product in site.products  %}
			{% if product.cat == "CLAB" and product.price != "0" and  product.available %}
				<div class="product simpleCart_shelfItem">
					<h4 class="product-name item_name"><a class="has-text-dark" href="{{product.url}}">{{product.title}}</a></h4>
                                        <h5 class="code item_code">{{product.sifra}}</h5>
					<img class="product-img image" data-src="{{product.img_path}}" alt="">
					<div class="product-data">
						<p class="product-description"> {{product.desc}}</p>
						<strong class="product-price is-main-txt item_price">{{product.price}} <small>RSD</small></strong>
						<p class="product-category item_category">{{ product.category }}</p>
					</div>
					<div class="product-widgets">
                                                {% if product.available %}
							<span class="avl-true">Na stanju</span>
                                                {% else %}
							<span class="avl-false">Nema na stanju</span>
                                                {% endif %}
						<input type="number" value="1" class="item_Quantity is-small input">
						<a class="item_add button is-main-bg buy_button is-small" href="javascript:;">KUPI</a>
					</div>
				</div>
			{% endif %}
		{% endfor %}
		{% for product in site.products  %}
			{% if product.cat == "CLAB" and product.price != "0"  and product.available == false %}
				<div class="product simpleCart_shelfItem">
                                        <h3 style="display:none;" class="item_code">{{product.sifra}}</h3>
					<h4 class="product-name item_name card-header-title"><a class="has-text-dark" href="{{product.url}}">{{product.title}}</a></h4>
					<img class="product-img image" data-src="{{product.img_path}}" alt="">
					<div class="product-data">
						<p class="product-description"> {{product.desc}}</p>
						<strong class="product-price is-main-txt item_price">{{product.price}} <small>RSD</small></strong>
						<p class="product-category item_category">{{ product.category }}</p>
					</div>
					<div class="product-widgets">
                                                {% if product.available %}
							<span class="avl-true">Na stanju</span>
                                                {% else %}
							<span class="avl-false">Nema na stanju</span>
                                                {% endif %}
						<input type="number" value="1" class="item_Quantity is-small input">
						<a class="item_add button is-main-bg buy_button is-small" href="javascript:;">KUPI</a>
					</div>
				</div>
			{% endif %}
		{% endfor %}
	</div>
	</div>
</section>
</div>
</div>
'''

SUBCAT_PAGE = '''---
layout: default
title: seo_title
---
<div class="container">
<div class="sidebar-helper">
<aside>
    {% include menu_new_side.html %}
</aside>
<section>
<div class="section">
<div class="container">
BREADCRUMB
<div class="filters" data-filter="FILTERS"></div>
SCRIPT
<div class="products">
    {% for product in site.products %}
		{% if product.cat == "CLAB" and product.subcat == "SLAB" and product.price != "0" and product.available %}
				<div class="product simpleCart_shelfItem">
					<h4 class="product-name item_name"><a class="has-text-dark" href="{{product.url}}">{{product.title}}</a></h4>
                                        <h5 class="code item_code">{{product.sifra}}</h5>
					<img class="product-img image" data-src="{{product.img_path}}" alt="">
					<div class="product-data">
						<p class="product-description"> {{product.desc}}</p>
						<strong class="product-price is-main-txt item_price">{{product.price}} <small>RSD</small></strong>
						<p class="product-category item_category">{{ product.category }}</p>
					</div>
					<div class="product-widgets">
                                                {% if product.available %}
							<span class="avl-true">Na stanju</span>
                                                {% else %}
							<span class="avl-false">Nije na stanju</span>
                                                {% endif %}
						<input type="number" value="1" class="item_Quantity input is-small">
						<a class="item_add button is-main-bg buy_button is-small" href="javascript:;">KUPI</a>
					</div>
				</div>
		{% endif %}
    {% endfor %}
    {% for product in site.products %}
		{% if product.cat == "CLAB" and product.subcat == "SLAB"  and product.price != "0" and product.available  == false %}
				<div class="product simpleCart_shelfItem">
                                        <h3 style="display:none;" class="item_code">{{product.sifra}}</h3>
					<h4 class="product-name item_name card-header-title"><a class="has-text-dark" href="{{product.url}}">{{product.title}}</a></h4>
					<img class="product-img image" data-src="{{product.img_path}}" alt="">
					<div class="product-data">
						<p class="product-description"> {{product.desc}}</p>
						<strong class="product-price is-main-txt item_price">{{product.price}} <small>RSD</small></strong>
						<p class="product-category item_category">{{ product.category }}</p>
					</div>
					<div class="product-widgets">
                                                {% if product.available %}
							<span class="avl-true">Na stanju</span>
                                                {% else %}
							<span class="avl-false">Nije na stanju</span>
                                                {% endif %}
						<input type="number" value="1" class="item_Quantity input is-small">
						<a class="item_add button is-main-bg buy_button is-small" href="javascript:;">KUPI</a>
					</div>
				</div>
		{% endif %}
    {% endfor %}
</div>
</div>
</div>
</section>
</div>
</div>
'''


SUBSUBCAT_PAGE = '''---
layout: default
title: seo_title
---
<div class="container">
<div class="sidebar-helper">
    <aside> 
        {% include menu_new_side.html %}
    </aside>
    <section>
        <div class="section">
            <div class="container">
            BREADCRUMB
            <div class="filters" data-filter="FILTERS"></div>
            SCRIPT
            <div class="products">
                {% for product in site.products %}
                            {% if product.cat == "CLAB" and product.subcat == "SLAB" and product.subsubcat == "SUBSUBLAB" and product.available %}
                                            <div class="product simpleCart_shelfItem">
                                                    <h4 class="product-name item_name card-header-title"><a class="has-text-dark" href="{{product.url}}">{{product.title}}</a></h4>
						    <h5 class="code item_code">{{product.sifra}}</h5>
                                                    <img class="product-img image" data-src="{{product.img_path}}" alt="">
                                                    <div class="product-data">
                                                            <p class="product-description"> {{product.desc}}</p>
                                                            <strong class="product-price is-main-txt item_price">{{product.price}} <small>RSD</small></strong>
                                                            <p class="product-category item_category">{{ product.category }}</p>
                                                    </div>
                                                    <div class="product-widgets">
							{% if product.available %}
								<span class="avl-true">Na stanju</span>
							{% else %}
								<span class="avl-false">Nije na stanju</span>
							{% endif %}
                                                            <input type="number" value="1" class="item_Quantity input is-small">
                                                            <a class="item_add button is-main-bg buy_button is-small" href="javascript:;">KUPI</a>
                                                    </div>
                                            </div>
                            {% endif %}
                {% endfor %}
                {% for product in site.products %}
                            {% if product.cat == "CLAB" and product.subcat == "SLAB" and product.subsubcat == "SUBSUBLAB" and product.available == false%}
                                            <div class="product simpleCart_shelfItem">
						    <h3 style="display:none;" class="item_code">{{product.sifra}}</h3>
                                                    <h4 class="product-name item_name"><a class="has-text-dark" href="{{product.url}}">{{product.title}}</a></h4>
                                                    <img class="product-img image" data-src="{{product.img_path}}" alt="">
                                                    <div class="product-data">
                                                            <p class="product-description"> {{product.desc}}</p>
                                                            <strong class="product-price is-main-txt item_price">{{product.price}} <small>RSD</small></strong>
                                                            <p class="product-category item_category">{{ product.category }}</p>
                                                    </div>
                                                    <div class="product-widgets">
							{% if product.available %}
								<span class="avl-true">Na stanju</span>
							{% else %}
								<span class="avl-false">Nije na stanju</span>
							{% endif %}
                                                            <input type="number" value="1" class="item_Quantity input is-small">
                                                            <a class="item_add button is-main-bg buy_button is-small" href="javascript:;">KUPI</a>
                                                    </div>
                                            </div>
                            {% endif %}
                {% endfor %}
            </div>
            </div>
        </div>
    </section>
</div>
</div>
'''




CATS = ''

with open('_data/cats.yml') as f:
	CATS = yaml.safe_load(f)



for cat in CATS:
	if 'filters' in cat['maincat'].keys():
		filters = cat['maincat']['filters']
		script_tag = '<script defer src="/assets/js/filters.js"></script>'
	else:
		filters = ""
		script_tag = ""
	cname = cat['maincat']['name']
	clab = cat['maincat']['label']
	#print(cname)
	breadcrumb = make_breadcrumbs(cname=cname)
	seo_title = make_seo_title(cname=cname)
	fname = cname.replace(' ', '_') + '.html'
	f = open(fname, 'w')
	print(fname)
	content = CAT_PAGE.replace('PATH', cname)
	content = content.replace('CLAB', clab)
	content = content.replace('BREADCRUMB', breadcrumb)
	content = content.replace('seo_title', seo_title)
	content = content.replace('SCRIPT', script_tag)
	content = content.replace('FILTERS', str(filters))
	f.write(content)
	f.close()
	#print("[+] " + cname)
print("[+] CATS DONE")


for cat in CATS:
	cname = cat['maincat']['name']
	clab = cat['maincat']['label']
	try:
		for subcat in cat['subcats']:
			if 'filters' in subcat.keys():
				filters = subcat['filters']
				script_tag = '<script defer src="/assets/js/filters.js"></script>'
			else:
				filters = ""
				script_tag = ""
			sname = subcat['name']
			slab = subcat['label']
			breadcrumb = make_breadcrumbs(cname=cname,sname=sname)
			seo_title = make_seo_title(cname=cname, sname=sname)
			path = '{} {}'.format(cname, sname)
			f = open(path.replace(' ', '_') + '.html', 'w')
			content = SUBCAT_PAGE.replace('PATH', path)
			content = content.replace('CLAB', clab)
			content = content.replace('SLAB', slab)
			content = content.replace('BREADCRUMB', breadcrumb)
			content = content.replace('seo_title', seo_title)
			content = content.replace('SCRIPT', script_tag)
			content = content.replace('FILTERS', str(filters))
			f.write(content)
			f.close()
			#print('[+]' + path)
	except Exception as e:
				print(e)

print('[+] SUBCAT DONE')
for cat in CATS:
	cname = cat['maincat']['name']
	clab = cat['maincat']['label']
	#try:
	if 'subcats' in cat.keys():
		for subcat in cat['subcats']:
			sname = subcat['name']
			slab = subcat['label']
			#try:
			if 'subsubcats' in subcat.keys():
				for subsubcat in subcat['subsubcats']:
					ssname = subsubcat['name']
					if 'filters' in subsubcat.keys():
						filters = subsubcat['filters']
						script_tag = '<script defer src="/assets/js/filters.js"></script>'
					else:
						filters = ""
						script_tag = ""
					if 'label' in subsubcat.keys():
						sslab = subsubcat['label']
					else:
						print(subsubcat)
						exit(1)
					#print(ssname)
					breadcrumb = make_breadcrumbs(cname=cname,sname=sname, ssname=ssname)
					seo_title = make_seo_title(cname=cname, sname=sname, ssname=ssname)
					path = '{} {} {}'.format(cname, sname, ssname)
					f = open(path.replace(' ', '_') + '.html', 'w')
					content = SUBSUBCAT_PAGE
					content = content.replace('CLAB', clab)
					content = content.replace('SLAB', slab)
					content = content.replace('SUBSUBLAB', sslab)
					content = content.replace('BREADCRUMB', breadcrumb)
					content = content.replace('FILTERS', str(filters))
					content = content.replace('SCRIPT', script_tag)
					content = content.replace('seo_title', seo_title)
					f.write(content)
					f.close()
						#print('[+]' + path)
					#except Exception as e:
					#	print(subsubcat)	
			else:
				print("[!] no subsubcat")	
		
	#except:
	#	pass
print("[+] SUBSUBCAT DONE")
