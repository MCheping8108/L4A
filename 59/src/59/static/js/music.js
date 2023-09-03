function audio(url){
  var audio = document.getElementsByClassName('audio')[0];
  $.post('getUrl',{'url':url},function(result){
    audio.src = result;
    audio.play();
  })

}
