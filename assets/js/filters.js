/* get data filter*/
let filterDiv = document.querySelector("[data-filter]");
let filters = filterDiv.dataset.filter.replace(/['\[\] ]/g,"")
                                      .split(',');
/* make checkboxes */
filters.forEach((el) => {
	let ch = document.createElement('input');
	ch.type = 'checkbox';
	ch.id = el;
	ch.name = el;
	let label = document.createElement('label');
	label.setAttribute('for', el);
	label.innerText = el.charAt(0).toUpperCase() + el.slice(1);


	filterDiv.appendChild(ch);
	filterDiv.appendChild(label);
});


/* get product data */
let productData = [];
let allProducts = document.querySelectorAll('.product');
allProducts.forEach((el) => {
	let product = {};
	product['elem'] = el;
	product['desc'] = el.innerText;
	productData.push(product);
});


/* react to events */
let chBoxes = document.querySelectorAll("[type='checkbox']");
chBoxes.forEach((el) => {
	el.addEventListener('change', (evt) => {
		let key = evt.target.name;
		if(evt.target.checked) {
			console.log(key + " on");
			productData.forEach((el) => {
				if(!el['desc'].toLowerCase().includes(key)) {
					console.log(key + " found ");
					el['elem'].classList.add('hidden');
				} else {
					el['elem'].classList.remove('hidden');
				}
			});
		} else {
			console.log(key + " off");
			productData.forEach((el) => {
				let elem = el['elem'];
				elem.classList.remove('hidden');
			});
		}
	});
});

