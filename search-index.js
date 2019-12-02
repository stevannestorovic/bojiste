---
---
let data = [
 {% for product in site.products %}
	{
		id: {{forloop.index}},
		name: "{{product.title}}",
		desc: "{{product.desc}}",
		img_path: "{{product.img_path}}",
		cat: "{{product.cat}}",
		subcat: "{{product.subcat}}",
		subsubcat: "{{product.subsubcat}}"
	},
 {% endfor %}
];



