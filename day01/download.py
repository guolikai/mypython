#!/usr/bin/python
#coding:utf8
import re
import urllib
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def getImg(html):
#    reg = r'src="(.*?\.png)" width' 
    reg = r'src="(.*?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s\.img' % x)
        x+=1

#print getHtml("http://pdf7.tarena.com.cn/tts8_source/ttsPage/LINUX/NSD_V02/MONITOR/DAY03/COURSE/ppt.html")
html = getHtml("http://pdf7.tarena.com.cn/tts8_source/ttsPage/LINUX/NSD_V02/MONITOR/DAY03/COURSE/ppt.html")
print getImg(html)

