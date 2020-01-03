let query = window.location.search.substring(1);
query = query.slice(query.indexOf('=')+1);
query = query.replace(/\+/g, '%20');
query = decodeURI(query);

let idx = new MiniSearch({
    fields: ['name', 'desc', 'sifra'],
    storeFields: ['name', 'price', 'desc', 'img_path', 'sifra'],
    searchOptions: {prefix: true, fuzzy: 0.1}
});

idx.addAll(data);

let res = idx.search(query);
let products = document.querySelector('.products');

res.forEach(element => {
    let product = document.createElement('div');
    product.className += 'product simpleCart_shelfItem';
   

    let productCode = document.createElement('h3');
    productCode.className += 'item_code';
    productCode.style.display = 'none';
    productCode.innerText = element.sifra;

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
    productPrice.innerText = element.price + ' RSD';

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


    let productWidgets = document.createElement('div');
    productWidgets.classList += 'product-widgets';
    productWidgets.appendChild(productQuantity);
    productWidgets.appendChild(productBuy);

    product.appendChild(productTitle);
    product.appendChild(productCode);
    product.appendChild(productImg);
    product.appendChild(productData);
    product.appendChild(productWidgets);
    

    products.appendChild(product);
});
