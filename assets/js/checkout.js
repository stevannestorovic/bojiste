simpleCart.ready(function() {
  simpleCart.each(function(item, x) {
    $('#checkoutForm').append('<input  type="hidden" name="' + item.get('name') + ' Name" value="' + item.get('name') + '">');
    $('#checkoutForm').append('<input  type="hidden" name="' + item.get('name') + ' Cena" value="' + item.get('price') + '">');
    $('#checkoutForm').append('<input  type="hidden" name="' + item.get('name') + ' Kol" value="' + item.get('quantity') + '">');
    console.log(document.querySelector('#checkoutForm'));
  });
});
