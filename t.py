# -*- coding: utf-8 -*-
import urllib2,urllib
from bs4 import BeautifulSoup

address = raw_input()

url = "http://www.pm25.in/%s" %address
# url = "http://www.pm25.in/tianjin"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',}
req = urllib2.Request(url,headers=headers)
page = urllib2.urlopen(req).read()

soup = BeautifulSoup(page)

rs = soup.find_all("div", class_="span12 avg",recursive=True)
for x in rs:
	try:
		print x.find(class_="city_name").get_text(strip=True),':',x.find(class_="level").get_text(strip=True)
		print x.find(class_="live_data_time").get_text(strip=True)
	except Exception, e:
		pass
rs = soup.find_all("div", class_="span1",recursive=True)
for x in rs:
	try:
		print x.find(class_="caption").get_text(strip=True),':',x.find(class_="value").get_text(strip=True)
	except Exception, e:
		print e