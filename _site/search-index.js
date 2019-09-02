data = [
 
	{
		name: "Mig",
		desc: "mig avion maketa",
		price: "100",
		img_path: "/assets/img/boja-za-tenk.jpeg"
	},
 
];

let idx = lunr(function (){
	this.ref('name');
	this.field('name');
	this.field('desc');
	this.field('price');
	this.field('img_path');
});


