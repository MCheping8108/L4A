user = null;  //当前用户-自己

/**
 * 注册用户方法
 * @param  {String} user_name 用户输入的名字
 */
function registe_user(user_name){
    $.get("/registe?name="+user_name,function(result){
        user = result;
    })
}

/**
 * 群聊功能，点击发送按钮时触发，发送的用户数据包含 用户名 用户头像 消息文本
 *     user 内容示例 {'name':'童童','text':'你好','photo':'/static/imgs/1.jpg'}
 * @param  {String} text        自己输入的文字信息
 * @param  {String} sendMessage 将消息显示在聊天窗口上
 */
function chat_in_group(text,sendMessage){
    user['text'] = disposeMsg(text);
    $.post("/group",user,function(result){
         if(result == 'success'){
            sendMessage(user);
         }
    })
}

window.onload = function(){
	user_name = prompt('您是');
	registe_user(user_name);

	var timer = setInterval(function(){
		$.get('/msg/list?user_name='+user['name'],function(result){
	        showMsgList(result);
	    })
	},2000);
}








