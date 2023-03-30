from time import sleep

print('test22')

from selenium import webdriver
chrome = webdriver.Chrome()
chrome.get('http://www.seleniumframework.com/Practiceform/')
sleep(10)
