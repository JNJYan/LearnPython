import itchat
import requests
from itchat.content import *


def get_response(msg,):
    tuling_api_url = 'http://www.tuling123.com/openapi/api'
    api_key = 'f722f495d1f04bc79396e53d09693bf1'
    tuling_data = {
        "key": api_key,
        "info": msg,
        'userid': 'wechat_robot'
    }
    try:
        r = requests.post(tuling_api_url, data=tuling_data).json()
        return r.get('text')
    except:
        return


@itchat.msg_register([TEXT, ])
def tuling_reply(msg):
    defaultReply = msg['Text']
    reply = get_response(msg['Text'])
    print(reply)
    return reply or defaultReply


itchat.auto_login(hotReload=True)
itchat.run()
