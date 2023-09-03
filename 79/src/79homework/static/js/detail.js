$('.button-cart').click(function(){
    var id = this.dataset.id;
    $.get('/add?product_id=' + id,function(result){
        alert(result['data'])
        if(result['code'] == 0){
            $.get('/count',function(result){
               if(result['code'] == 0) {
                   $('#cart-total').html(result['data'])
            }
   });
        }
    });
});