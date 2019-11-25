from typing import List

import feedparser
import time
test1 = ['seacms', 'SEACMS']
test2 = ['CVE']

def feed(test):
    record = []
    url1 = 'https://xz.aliyun.com//feed'
    a = feedparser.parse(url1)
    for i in range(10):
        for j in range(len(test)):
            if test1[j] in a.entries[i].title:
                print(a.entries[i].title)
                print(a.entries[i].published)
                record.append(i)
    print(record)


def test():
    url2 = 'https://msrc-blog.microsoft.com/feed/'
    b = feedparser.parse(url2)
    for i in range(10):
        print(b.entries[i].title)
        c = b.entries[i].published
        timeArray = time.strptime(c, "%a, %d %b %Y %H:%M:%S %z")
        timeStamp = time.mktime(timeArray)
        #print(timeStamp)
    d = '{"tilee":"%s",' \
        '"lll":"lll"}'%timeStamp
    print(d)


if __name__ == '__main__':
    feed(test1)
    test()


