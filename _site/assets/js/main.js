/*const navSlide = () => {
    console.log('nav slide');
    const burger = document.querySelector(".burger");
    const nav = document.querySelector(".nav-links");

    burger.addEventListener('click', (e) => {
        nav.classList.toggle('nav-active');
    });
}
console.log("main loaded");
navSlide();*/

simpleCart.currency({
	code: "RSD",
	name: "Dinar",
	symbol: "RSD",
	after: true
});
simpleCart({
	checkout: { 
		type: "SendForm", 
		url:"https://diyrama.netlify.com/naplata.html",
		method: "GET"
		},
	cartColumns: [
		{attr: "name", label: "Naziv"},
		{attr: "price", label: "Cena"},
		{view: "decrement", label: false, text: "-1"},
		{attr: "quantity", label: "kol."},
		{view: "increment", label: false, text: "+1"},
		{attr: "total", label: "Ukupno", view:"currency"},
		{view: "remove", text: "Ukloni", label: false}
	],
//		currency: "dinar",
	cartStyle: "table"
});
