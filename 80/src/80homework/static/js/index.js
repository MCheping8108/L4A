
$('.zxnav').click(function(){
    var id = this.dataset.id;
    location.href = '/detail?category_id=' + id;
});
