import time

#from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException 

import sys

#from subprocess import call
#call(["chcp", "65001"])
import os
os.system("chcp 65001")

##------------------------ changes in this part only --------------------------------- ##

#C:/Users/doole/Desktop/chromedriver
driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.youtube.com/playlist?list=PLj-AqUNa2cH4zRFGSZ9QcXSrMDaaB8iZ5')
keepgoing = True
index = 0
listOfNames = []
f= open("test.txt","w+",encoding='utf-8')
elem = driver.find_element_by_tag_name("body")
no_of_pagedowns = 600
#600
	
	
while no_of_pagedowns:
	elem.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.2)
	no_of_pagedowns-=1
	
post_elems = driver.find_elements_by_class_name("ytd-playlist-video-list-renderer")

for post in post_elems:
	index+=1
	shouldIDoIt = True
	try:
		post.find_element_by_id('video-title')
	except NoSuchElementException:
		shouldIDoIt = False
    
	if(shouldIDoIt):
		name = post.find_element_by_id('video-title')
		listOfNames.append("%d: %s \n" % (index,name.text))
	else:
		print("cant find it boo hoo")
	
		

for name in listOfNames:
	print(name)
	f.write(name)
driver.quit()
f.close()
