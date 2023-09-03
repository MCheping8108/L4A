var ajax_flag = false;
var blog_id = $('.kid-info-title').attr('data-blog-id');

//点赞
function like_on(img){
    if(ajax_flag)return;
    ajax_flag = true;
    var likes = $('.kid-info-like span').html();
    $.get('/like/create?blog_id='+blog_id,function(result){
        if(result.status == 'success'){
            $(img).attr('src','/static/images/like.png').attr('onclick','like_cancle(this)');
            $('.kid-info-like span').html(parseInt(likes) + 1);
            ajax_flag = false;
        }else{
            window.location.href = "/user/login";
        }
    })
}

//取消点赞
function like_cancle(img){
    if(ajax_flag)return;
    ajax_flag = true;
    var likes = $('.kid-info-like span').html();
    $.get('/like/delete?blog_id=' + blog_id,function(result){
        if(result.status == 'success'){
            $(img).attr('src','/static/images/like-no.png').attr('onclick','like_on(this)');
            $('.kid-info-like span').html(parseInt(likes) - 1);
            ajax_flag = false;
        }else{
            window.location.href = "/user/login";
        }
    })
}