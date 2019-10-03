data = [
 
	{
		name: "boja a",
		desc: "boja za bojenje",
		price: "10",
		img_path: "/assets/img/marinac.jpeg"
	},
 
	{
		name: "maketa plasticna miniart",
		desc: "dsadasd",
		price: "11",
		img_path: "/assets/img/tigar-tenk.jpg"
	},
 
	{
		name: "Mig",
		desc: "mig avion maketa",
		price: "100",
		img_path: "/assets/img/boja-za-tenk.jpeg"
	},
 
	{
		name: "mk1",
		desc: "dasds",
		price: "adas",
		img_path: "/assets/img/boja-za-tenk.jpeg"
	},
 
	{
		name: "stealth",
		desc: "lmao",
		price: "10",
		img_path: "/assets/img/header-bg.jpeg"
	},
 
	{
		name: "Vozic 2",
		desc: "multitrack drifting",
		price: "100",
		img_path: "/assets/img/slider-img-2.jpeg"
	},
 
	{
		name: "Vozic 22",
		desc: "multitrack drifting",
		price: "100",
		img_path: "/assets/img/slider-img-2.jpeg"
	},
 
	{
		name: "Vozic 42",
		desc: "multitrack drifting",
		price: "100",
		img_path: "/assets/img/slider-img-2.jpeg"
	},
 
	{
		name: "Vozic",
		desc: "multitrack drifting",
		price: "100",
		img_path: "/assets/img/slider-img-2.jpeg"
	},
 
];

let idx = lunr(function (){
	this.ref('name');
	this.field('name');
	this.field('desc');
	this.field('price');
	this.field('img_path');
});


