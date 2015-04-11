# !/usr/bin/env python
# -*- coding:UTF-8 -*-
# import sys
# import webbrowser
# sys.path.append("libs")
# import time

 
# value = ['message','tree','mouse','nicki']
# url = 'http://translate.google.cn/translate_tts?ie=UTF-8&tl=en&q='
# for v in value:
# 	webbrowser.open_new_tab(url+v)
# 	webbrowser.BackgroundBrowser
# 	time.sleep(1)


# print webbrowser.get()
# import httplib
# import io
# import pyglet

# conn = httplib.HTTPConnection('translate.google.cn')
# conn.request('get', '/translate_tts?ie=UTF-8&tl=en&q=nicki')
# r = conn.getresponse()

# conn.close()
import urllib
import urllib2
import cookielib
import types
import sys

# cj = cookielib.LWPCookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# urllib2.install_opener(opener)

# req = urllib2.Request('http://translate.google.cn/translate_tts?ie=UTF-8&tl=en&q=nicki')
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0')

# operate = opener.open(req)
# msg = operate.read()

# print type(msg)

# file_object = open('d://baidu.wav','w')
# file_object.write(msg)
# file_object.close()
headers = {"Host": "translate.google.cn",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) "
                         "AppleWebKit/535.19 (KHTML, like Gecko) "
                         "Chrome/18.0.1025.163 Safari/535.19"
}
req = urllib2.Request('http://translate.google.cn/translate_tts?ie=UTF-8&tl=en&q=truck', '', headers)
response = urllib2.urlopen(req)
f = open('d:\\a.mp3', 'w')
f.write(response.read())
f.close()
