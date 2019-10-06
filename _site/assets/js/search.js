console.log('search init');
let query = window.location.search.substring(1);
query = query.slice(query.indexOf('=')+1);
query = query.replace(/\+/g, '%20');
query = decodeURI(query);

console.log('index');
let idx = new MiniSearch({
    fields: ['name', 'price', 'desc', 'cat', 'subcat', 'subsubcat'],
    storeFields: ['name', 'price', 'desc', 'img_path'],
    searchOptions: {prefix: true, fuzzy: 0.2}
});

idx.addAll(data);

let res = idx.search(query);
let products = document.querySelector('.products');

res.forEach(element => {
    let product = document.createElement('div');
    product.className += 'product simpleCart_shelfItem';

    let productTitle = document.createElement('h4');
    productTitle.className += 'product-name item_name';
    productTitle.innerText = element.name;

    let productImg = document.createElement('img');
    productImg.className += 'product-img image';
    productImg.src = element.img_path;

    let productData = document.createElement('div');
    productData.className += 'product-data';

    let productDesc = document.createElement('p');
    productDesc.className += 'product-description';
    productDesc.innerText = element.desc;

    let productPrice = document.createElement('strong');
    productPrice.classData += 'product-price is-main-txt item_price';
    productPrice.innerText = element.price;

    productData.appendChild(productDesc);
    productData.appendChild(productPrice);

    let productQuantity = document.createElement('input');
    productQuantity.type = 'number';
    productQuantity.value = 1;
    productQuantity.classList += 'item_Quantity input';

    let productBuy = document.createElement('a');
    productBuy.className += 'item_add button is-main-bg buy_button is-large';
    productBuy.href = 'javascript:;';
    productBuy.innerText = 'Kupi';

    product.appendChild(productTitle);
    product.appendChild(productImg);
    product.appendChild(productData);
    product.appendChild(productQuantity);
    product.appendChild(productBuy);

    products.appendChild(product);
});