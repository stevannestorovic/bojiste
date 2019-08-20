data = [
 
	{
		name: "Boja",
		desc: "Odlicna boja za bojenje",
		price: "20$",
		img_path: "/assets/img/varnish.jpeg"
	},
 
	{
		name: "MiG",
		desc: "artikal opis bla bla",
		price: "150$",
		img_path: "/assets/img/boja-za-tenk.jpeg"
	},
 
	{
		name: "star wars",
		desc: "Bla bla",
		price: "1",
		img_path: "/assets/img/tigar-tenk.jpg"
	},
 
	{
		name: "test",
		desc: "testiranje",
		price: "199",
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


