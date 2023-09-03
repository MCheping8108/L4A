from urllib import request
import json


#与图灵机器人聊天
def talk(data):
    tuling = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": data
            }
        },
        "userInfo": {
            "apiKey": "d06c89c507fd4306ae277fe747533730",
            "userId": "c3e6916f4040b551"
        }
    }
    req = request.urlopen('http://openapi.tuling123.com/openapi/api/v2',data=json.dumps(tuling).encode('utf-8'))
    html = req.read().decode('utf-8')
    result = json.loads(html)
    
    return result['results'][0]['values']['text']
