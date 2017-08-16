# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'https://www.qiushibaike.com/text/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
def find(content):
    pattern = re.compile('<div .*?article block untagged mb15">(.*?)>')
    items = re.findall(pattern,content)
    print items

try:
    # request = urllib2.Request(url,headers=headers)
    # response = urllib2.urlopen(request,timeout=5)
    # with open('baidu.html','w') as f:
    #     f.write(response.read())
    with open('baidu.html', 'r') as f:
        find(f.read())

except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason

