#!/usr/bin/python
#coding:utf8
import urllib

def urlencode_method():
    src_data = {
    	"10.10.10.54": {"Net": "eth0 C8:1F:66:FB:52:5C\r\neth1 C8:1F:66:FB:52:5C\r\neth2 C8:1F:66:FB:52:5E\r\neth3 C8:1F:66:FB:52:5F", "Mem": "64375MB", "SN": "GFNTS42", "Model": "PowerEdge R720", "Disk": "/dev/sda | 1199.1 GB", "OS": "CentOS release 6.7|2.6.32-573.el6.x86_64", "CPU": "Intel(R) Xeon(R) CPU E5-2630 v2 @ 2.60GHz", "Manufacturer": "Dell Inc."},
    }
    '''
    src_data = {
    		"type" : "AUTO",
    		"i" : "glk",
    		"doctype" : "json",
    		"xmlVersion" : "1.8",
    		"keyfrom" : "fanyi.web",
    		"ue" : "UTF-8",
    		"action" : "FY_BY_CLICKBUTTON",
    		"typoResult" : "true"
    		}
    '''
    Url="http://192.168.30.191/post"
    post_data=urllib.urlencode(src_data)
    print Url+"?"+post_data


def baidu():
    #通过urllib.urlencode()参数是一个Dict类型,":"转变成"="
    #fullurl="https://www.baidu.com/baidu?wd=python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%BC%80%E5%8F%91%E5%AE%9E%E6%88%98+%E5%B4%94%E5%BA%86%E6%89%8D"
    url = "https://www.baidu.com/baidu"
    wd = {"wd":"python3网络爬虫开发实战 崔庆才"}
    wd = urllib.urlencode(wd)
    fullurl = url+"?"+wd
    print fullurl
    print "转换为中文形式:",urllib.unquote(fullurl)

if __name__ == "__main__":
	baidu()
