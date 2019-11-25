import time
from urllib import request
import json

raw = {
    "msgtype": "text",
    "text": {
        "content": "%s",
        "mentioned_list": ["@all"],
        "mentioned_mobile_list":["17521011527"]
    }
}
data = json.dumps(raw)
data = bytes(data,'utf8')
url1 = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=afaf7da4-8489-4c64-bfc4-0777e041a931'
resp = request.urlopen(url1,data=data)