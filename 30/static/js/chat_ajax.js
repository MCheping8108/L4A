/**
 * 群聊功能，点击发送按钮时触发，发送的用户数据包含 用户名 用户头像 消息文本
 *     user 内容示例 {'name':'童童','text':'你好','photo':'/static/imgs/1.jpg'}
 * @param  {String} text        自己输入的文字信息
 */
function sendMsgToServer(text) {
    var message = user;
    message['text'] = text;
    $.post("/group", message, function (result) {
        if (result['state'] == 'success') {
            message['time'] = result['time'];
            showMsg(message);
        }
    })
}
