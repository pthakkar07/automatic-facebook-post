from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('http://www.google.com')
#elem = driver.find_element_by_link_text('About')

#time.sleep(5)# 
#elem.click()# in order to click particular link we page

#time.sleep(15) //refresh buttion
#driver.refresh()

# forward and backward buttion in selenium
"""
elem = driver.find_element_by_link_text('About')
time.sleep(5)
elem.click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
"""
#Scrolling and getting the current URL

driver.get('http://www.wikipedia.org')
elem =driver.find_element_by_tag_name('html')
time.sleep(0)
elem.send_keys(Keys.END)
time.sleep(0)
elem.send_keys(Keys.HOME)

driver.get('http://www.google.com')
elem = driver.find_element_by_link_text('About')
time.sleep(5) 
elem.click()
time.sleep(5)
print(driver.current_url)