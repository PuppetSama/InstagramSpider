# -*- coding:utf-8 -*-

import urllib.parse,urllib.request
import re
import time
import random

title = 'taylorswift'
location = 'E:/inspic3/'
pre_url = 'https://www.instagram.com/' + title + '/'
def getcontent(url):
	try:
		request = urllib.request.Request(url)
		response = urllib.request.urlopen(request)
		content = response.read().decode('utf-8','ignore')
	except httplib.IncompleteRead as e:
		content = e.partial
	return content

def getnexturl(url):
	content = getcontent(url)
	last_url =  re.compile(str('<a href="/'+title+'/(.max_id=.*?)"')).findall(content)
	if last_url:
		next_url = pre_url + last_url[0]
	else:
		next_url = None
	return next_url

def getpictureurl(url):
	content = getcontent(url)
	picture_urls =  re.compile('"thumbnail_src": "(https://.*?.jpg)"').findall(content)
	return picture_urls

def downloadpic(url):
	for i in range(len(url)):
		filename= location + str(len(url)-i)+ '.jpg'
		urllib.request.urlretrieve(url[i], filename)
	return 'ok'

allurl = []
allurl.extend(getpictureurl(pre_url))
url = getnexturl(pre_url)		
while url != None:
	allurl.extend(getpictureurl(url))
	time.sleep(10)
	url = getnexturl(url)
print(downloadpic(allurl))