function dynasty_ajax(element){
  var dynasty = element.innerHTML;
  $.get('/dynasty?name='+dynasty,function(result){
      var data = result['data'];
      //图片切换
      $('.side-left>img').attr('src','/static/images/dynasty/' + data['img']);
      //标题切换
      $('.side-right h1').html(data['title'])
      //介绍切换
      $('.intro').html('');
      for (var i = 0; i < data['intro'].length; i++) {
        $('.intro').append('<p>'+data['intro'][i]+'</p>');
      }
  });
  $.get('/person?name=' + dynasty,function(result){
    var data = result['data'];
      $('.picture').html('');
      for (var i = data.length - 1; i >= 0; i--) {
        $('.picture').append('<li><a href="/info?id='+data[i]['_id']+'" target="_blank"><img src="'+data[i]['photo']+'" width="100" height="100"/></a><a href="/info?id='+data[i]['_id']+'"  target="_blank">['+data[i]['name']+']</a></li>');
      }
  });
  $.get('/list?name=' + dynasty,function(result){
       $('.event-list').html('');
        if(result['data'] != null){
            var data = result['data'];
            for(var i = 0;i<data.length;i++){
              $('.event-list').append('<a target="_blank"><span class="event-date">'+data[i]['date']+'</span><span class="event-title">'+data[i]['title']+'</span></a>');
            }
        }
  });
}
