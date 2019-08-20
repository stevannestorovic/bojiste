---
---
data = [
 {% for product in site.products %}
	{
		name: "{{product.title}}",
		desc: "{{product.desc}}",
		price: "{{product.price}}",
		img_path: "{{product.img_path}}"
	},
 {% endfor %}
];

let idx = lunr(function (){
	this.ref('name');
	this.field('name');
	this.field('desc');
	this.field('price');
	this.field('img_path');
});


