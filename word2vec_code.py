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
from nltk.stem.porter import *
def get_word2vec(word):
    url="http://relatedwords.org/relatedto/"+word
    driver =webdriver.Firefox()
    driver.get(url)
    parentElement = driver.find_element_by_class_name("words")
    elementList = parentElement.find_elements_by_tag_name("a")
    li=[]
    siz=min(5,len(elementList))
    for i in range(0,siz):
        foo=""
        foo=elementList[i].get_attribute('href')
        foo=foo[34:]
        li.append(foo)
    driver.quit()
    list_stemmed=[]
    for i in li:
        i=urllib2.unquote(i)
	 #STEMMER
	stemmer = PorterStemmer()
	i=stemmer.stem(i)
	list_stemmed.append(i)
    #print list_stemmed
        #urllib2.unquote("%CE%B1%CE%BB%20")
    driver.quit()
    return list_stemmed
#get_word2vec("car")
