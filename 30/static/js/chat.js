//发送消息，点击发送后会触发此函数
function sendMsg() {
    var text = document.getElementById("text");
    var value = disposeMsg(text.value.trim())
    text.value = "";
    if (value == "" || value == null) {
        alert("发送信息为空， 请输入！")
        return;
    }
    //使用ajax把消息发送给服务器并展示
    sendMsgToServer(value);
}


function showMsg(data) {
    var str = createMsg(data);
    var msgs = document.getElementById("msgs");
    msgs.innerHTML = msgs.innerHTML + str;
    effectRain(data['text'])
    //移除之前的消息
    while (msgs.childNodes.length > 100) {
        msgs.removeChild(msgs.firstChild);
    }
    //滚动到最下面
    var show = document.getElementById("show");
    show.scrollTop = show.scrollHeight;
}

//替换回车换行及空格
function disposeMsg(detail) {
    detail = detail.replace(/\n/g, "<br>").replace(/ /g, "&nbsp;")
    return detail;
}

// 生成内容
function createMsg(data) {
    var str = "";
    if (data['name'] == user['name']) {
        str = "<div class=\"msg guest\"><div class=\"msg-right\" worker=\"" + data['name'] + "\"><div class=\"msg-host photo\" style=\"background-image: url(" + data['photo'] + ")\"></div><div class=\"msg-ball\" data-time=" + data['time'] + ">" + data['text'] + "</div></div></div>";
    } else if (data['name'] == 'admin') {
        str = "<div id=\"welcome\" data-time=" + data['time'] + ">" + data['text'] + "</div>";
    } else {
        str = "<div class=\"msg robot\"><div class=\"msg-left\" worker=\"" + data['name'] + "\"><div class=\"msg-host photo\" style=\"background-image: url(" + data['photo'] + ")\"></div><div class=\"msg-ball\" data-time=" + data['time'] + ">" + data['text'] + "</div></div></div>";
    }
    return str;
}

// 展示最新消息列表
function show_new_list(result) {
    for (var i = 0; i < result.length; i++) {
        showMsg(result[i]);
    }
}


function getTime() {
    var msgs = document.getElementById("msgs").getElementsByTagName("div");
    var last_time = msgs[msgs.length - 1].dataset.time;
    return last_time;
}

/**
 * 展示特效，发送数据包含特定字符串，会下特效雨
 */
var word = ['想你', '生日快乐', '爱', '棒', '钱', 'money', '雪', '音乐', '可乐'];

function effectRain(text) {
    for (var w = 0; w < word.length; w++) {
        if (text.match(word[w])) {
            new Effect({
                //特效图片，多张图片时传入数组[]，单个图片时传入字符串
                effectUrl: "../static/imgs/11/" + word[w] + '.png',
                //特效旋转，1/true为旋转，0/false为不旋转
                rotate: 0,
                //特效方向，left/right/up/down
                direction: "up"
            });
        }
    }
}


window.onload = function () {
    var name = document.getElementsByTagName("b")[0].innerText;
    var photo = document.getElementById('welcome').dataset.photo;
    user = {"name": name, "photo": photo};
    setInterval(function () {
        var last_time = getTime();
        $.get('/get_list?last_time=' + last_time, function (result) {
        show_new_list(result);
    });
    }, 1000);
    
    // 在下方写你的代码：定时器，展示最新消息列表
    // setInterval(function () {
    // $.get("/msg/list?user_name=" + user['name'], function (result) {
    //     show_new_list(result);
    // })
    // }, 2000);
};