import unittest
import time
import re
import sys
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib2
def get_word2vec(word):
    url="http://relatedwords.org/relatedto/"+word
    driver =webdriver.Firefox()
    driver.get(url)
    parentElement = driver.find_element_by_class_name("words")
    elementList = parentElement.find_elements_by_tag_name("a")
    li=[]
    for a in elementList:
        foo=""
        foo=a.get_attribute('href')
        foo=foo[34:]
        li.append(foo)
    driver.quit()

    for i in li:
        print urllib2.unquote(i)
        #urllib2.unquote("%CE%B1%CE%BB%20")
get_word2vec("car")
