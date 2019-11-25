import feedparser
import time
import json
from urllib import request

def alert():
    test = ['CVE','Updates']
    send = 0
    url = 'https://msrc-blog.microsoft.com/feed/'
    b = feedparser.parse(url)
    for i in range(len(b.entries)):
        for j in range(len(test)):
            if test[j] in b.entries[i].title:
                #print(b.entries[i].title)
                c = b.entries[i].published
                timeArray = time.strptime(c, "%a, %d %b %Y %H:%M:%S %z")
                timeStamp = time.mktime(timeArray)
                #print(timeStamp)
                d = '{"tilee":"%s"}'%timeStamp
                #print(d)
                content = '标题：' + b.entries[i].title + '\n' + '时间：' + c +'\n' + '地址：' + b.entries[i].guid
                localtime = time.time()
                if localtime - timeStamp <= 600:
                    raw = {
                        "msgtype": "text",
                        "text": {
                            "content": "%s" %content,
                            "mentioned_list": ["@all"],
                        }
                    }
                    data = json.dumps(raw)
                    data = bytes(data,'utf8')
                    send = 1
        if send == 1:
            url1 = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=658789fd-c93d-479e-bbcf-c67dc495bae2'
            resq = request.urlopen(url1,data=data)
            send = 0

if __name__ == '__main__':
    alert()