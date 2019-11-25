import feedparser
import time
import json
from urllib import request

def alert():
    test = ['CVE-2019-3758']
    send = 0
    url = 'https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml'
    b = feedparser.parse(url)
    for i in range(len(b.entries)):
        for j in range(len(test)):
            if test[j] in b.entries[i].title:
                #print(b.entries[i].title)
                c = b.entries[i].date
                timeArray = time.strptime(c, "%Y-%m-%dT%H:%M:%SZ")
                timeStamp = time.mktime(timeArray)
                #print(timeStamp)
                d = '{"tilee":"%s"}'%timeStamp
                #print(d)
                content = '标题：' + b.entries[i].title + '\n' + '时间：' + c +'\n' + '地址：' + b.entries[i].guid
                localtime = time.time()
                print(localtime)
                print(timeStamp)
                print(localtime - timeStamp)
                print(b.entries[i].date)
                if localtime - timeStamp <= 10800:
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
            url1 = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=afaf7da4-8489-4c64-bfc4-0777e041a931'
            resq = request.urlopen(url1,data=data)
            send = 0

if __name__ == '__main__':
    alert()