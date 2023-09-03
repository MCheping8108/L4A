$(function(){
   $.get('/count',function(result){
       if(result['code'] == 0) {
           $('#cart-total').html(result['data'])
       }
   });
});

function show_login_mask(){
    $('.mask').show();
    $('.login').show();
    $('.login-close').click(function(){
        hide_login_mask();
    })
}

function hide_login_mask(){
    $('.mask').hide();
    $('.login').hide();
}

function hide_register_mask(){
    $('.register').hide();
    $('.mask').hide();
}

$('.signin').click(function(){
    show_login_mask()
})

$('.login-sub').click(function(){
   var username = $('.login-input .username').val();
   var password = $('.login-input .password').val();
   var data = {
       'username' : username,
       'password' : password
   }
   $.post('/login',data , function(result){
       if(result['code'] == 0){
           hide_login_mask();
           alert(result['data'])
       }else{
           alert(result['data'])
       }
   });
});

$('.signup').click(function(){
    $('.mask').show();
    $('.register').show();
    $('.register-close').click(function(){
        hide_register_mask();
    });
});

$('.regist-sub').click(function(){
    var username = $('.register-input .username').val();
    var password = $('.register-input .password').val();
    var repassword = $('.register-input .repassword').val();
    var data = {
        'username' : username,
        'password' : password,
        'repassword':repassword
    }
    $.post('/register',data,function(result){
        if(result['code'] == 0){
            hide_register_mask();
            show_login_mask()
        }else{
            alert(result['data']);
        }
    })
});
