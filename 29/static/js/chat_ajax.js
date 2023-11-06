user = null;  //当前用户-自己


/**
 * 群聊功能，点击发送按钮时触发，发送的用户数据包含 用户名 用户头像 消息文本
 *     user 内容示例 {'name':'童童','text':'你好','photo':'/static/imgs/1.jpg'}
 * @param  {String} text        自己输入的文字信息
 */
function sendMsgToServer(text) {
    //在下方写你的代码：构建消息对象，发送ajax-post请求，地址/group,并把消息对象发送给服务器
    $.post("/group", data, function (result) {
        if (result.code == 0) {
            alert("发送成功");
        }
    })
}


