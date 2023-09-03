function increase(ele){
    var id = $(ele).parent().data('id');
    var amount = parseInt($(ele).parent().parent().children('.p-stock-text').val())
    if(amount < 99){
        $.get('/increase?cart_id='+id,function(result){
            if(result['code'] == 0){
                location.reload()
            }
        })
    }
}

function decrease(ele){
    var id = $(ele).parent().data('id');
    var amount = parseInt($(ele).parent().parent().children('.p-stock-text').val())
    if(amount > 1){
        $.get('/decrease?cart_id='+id,function(result){
            if(result['code'] == 0){
                location.reload()
            }
        })
    }
}

function pay(){
    $.get('/pay',function(result){
        if(result['code'] == 0){
            alert(result['data']);
            location.reload();
        }
    })
}

function del_cart(ele){
    var id = $(ele).parent().data('id');
    $.get('/del_cart?cart_id='+id,function(result){
        if(result['code'] == 0){
            alert(result['data']);
            location.reload();
        }
    })
}