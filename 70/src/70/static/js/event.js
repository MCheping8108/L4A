$(function(){
  var month = $('.month');
  var search = $('.search');
  change_options(month.val())
  month.change(function(){
    change_options($('.month').val())
  });
  search.click(function(){
    month = $('.month').val();
    day = $('.day').val();
    $.get('/search?month='+month+'&day='+day,function(result){
        $('.event-list').html('');
            if(result['data'] != null){
              var data = result['data'];
              for(var i = 0;i<data.length;i++){
                $('.event-list').append('<a target="_blank"><span class="event-date">'+data[i]['date']+'</span><span class="event-title">'+data[i]['title']+'</span></a>');
             }
        }
    });
  })
});

function change_options(month){
  var day = $('.day');
  var m_day = [31,29,31,30,31,30,31,31,30,31,30,31];
  day_count = m_day[month - 1];
  day.html('');
  for(var i = 1;i<day_count+1;i++){
    day.append('<option value='+i+'>'+i+'日</option>');
  }
}
