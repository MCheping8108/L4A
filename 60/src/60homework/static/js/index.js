var plist = document.getElementsByClassName('frame')

window.onload = function(){
  for(var i = 0;i<plist.length;i++){
    plist_info(i,plist[i]);
    
  }
}

function plist_info(index,obj){
  obj.onclick = function(){
    var pid = this.dataset.pid;
    window.location.href = '/plist?id='+pid;
  }
}
