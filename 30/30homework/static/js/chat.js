function sendMsg(){
    var text = document.getElementById("text");
    var value = text.value
    text.value = "";
    if (value == "" || value == null){
        alert("发送信息为空，请输入！")
        return;
    }
    //使用ajax把消息发送给服务器
    chat_in_group(value,function(data){
        addMsg(data);
    });
}



function addMsg(data)
{
    var str = createMsg(data);
    var msgs = document.getElementById("msgs");
    msgs.innerHTML = msgs.innerHTML + str;
    //移除之前的消息
    while (msgs.childNodes.length > 100) {
        msgs.removeChild(msgs.firstChild);
    }
    //滚动到最下面
    var show = document.getElementById("show");
    show.scrollTop = show.scrollHeight;
}
//替换回车换行及空格
function disposeMsg(detail){
    detail = detail.replace(/\n/g, "<br>").replace(/ /g, "&nbsp;")
    return detail;
}

// 生成内容
function createMsg(data){
    var str = "";
    if(data['name'] == user_name){
        str = "<div class=\"msg guest\"><div class=\"msg-right\" worker=\"" + data['name'] + "\"><div class=\"msg-host photo\" style=\"background-image: url(" + data['photo'] +")\"></div><div class=\"msg-ball\" >" + data['text'] +"</div></div></div>";
    }else if(data['name'] == 'admin'){
        str = "<div id=\"welcome\">" + data['text'] +"</div>";
    }else{
        str = "<div class=\"msg robot\"><div class=\"msg-left\" worker=\"" + data['name'] + "\"><div class=\"msg-host photo\" style=\"background-image: url(" + data['photo'] +")\"></div><div class=\"msg-ball\" >" + data['text'] + "</div></div></div>";
    }
    return str;
}

function showMsgList(result){
    var msgs = document.getElementById("msgs");
    msgs.innerHTML = ""
    //遍历消息列表，显示所有消息
    for(var i=0;i<result.length;i++){
        var msg = result[i]
        addMsg(msg);
    }
}

