var tabs = $('.tabs a')
tabs.on('click',function(argument){
  tabs.removeAttr('id');
  $(this).attr('id','activate');
  var keyword = $(this).html();
  $.get('/getRanking?key=' + keyword,function(result){
    var data = result['data'];
    var str = '';
    for(var i = 0;i<data.length;i++){
      var template = 
          '<li class="flex-c" data-rid="'+data[i]["_id"]+'" onclick="clickHandle(this);">'+
            '<img src="/static/images/ranking/'+data[i]["pic"]+'">'+
            '<div class="item-info">'+
              '<p class="name">'+data[i]["name"]+'</p>'+
            '</div>'+
          '</li>';
      str += template;
    }
    $('.tab-con').html(str);
  })
})

// var lis = $('.tab-con li');
// lis.on('click',function(){
//   console.log('click');
// })

function clickHandle(element){
	var title = $(element).find('.name').html();
  var rid = element.dataset.rid;
  $.get('/music_list?rid='+rid,function(result){
    var data = result['data'];
    var str = ''
    for(var i = 0;i<data.length;i++){
      var template = 
          '<li class="song-item flex-c">'+
            '<div class="song-rank flex-c">'+
              '<div class="rank-num">'+
                '<span>'+(i+1)+'</span>'+
              '</div>'+
              '<div class="status"></div>'+
              '<img src="/static/images/songs/'+data[i]["pic"]+'" class="cover">'+
            '</div>'+
            '<div class="song-name flex-c"  onclick="javascript:audio(\''+data[i]["url"]+'\');">'+
              '<span class="name">'+data[i]["name"]+'</span>'+
            '</div>'+
            '<div class="song-artist">'+
              '<span>'+data[i]["artist"]+'</span>'+
            '</div>'+
            '<div class="song-album">'+
              '<span>'+data[i]["album"]+'</span>'+
            '</div>'+
            '<div class="song-time">'+
              '<span>'+data[i]["songTimeMinutes"]+'</span>'+
            '</div>'+
            '<div class="song-opts flex-c"></div>'+
          '</li>';
        str += template;
    }
    $('.rank-list').html(str);
    $('.r-title').html(title);
  })
}
