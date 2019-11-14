simpleCart.ready(function() {
  simpleCart.each(function(item, x) {
    $('form').append('<input  type="hidden" name="' + item.get('name') + ' Name" value="' + item.get('name') + '">');
    $('form').append('<input  type="hidden" name="' + item.get('name') + ' Cena" value="' + item.get('price') + '">');
    $('form').append('<input  type="hidden" name="' + item.get('name') + ' Kol" value="' + item.get('quantity') + '">');
    console.log(document.querySelector('form'));
  });
});
