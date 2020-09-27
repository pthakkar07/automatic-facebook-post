from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.facebook.com')
emailelement=driver.find_element( By.XPATH,'//*[@id="email"]')
emailelement.send_keys('# enter you mail ID')
passelement=driver.find_element( By.XPATH,'//*[@id="pass"]')
passelement.send_keys('# Enter your password here.')

elem =driver.find_element_by_name('login')
elem.click()

elem1 =driver.find_element( By.XPATH,'//*[@name="xhpc_message"]')#find Tag according you facebook url
time.sleep(5)
elem1.send_keys("Your limitation")
time.sleep(10)
buttons= driver.find_element_by_tag_name('button') 
time.sleep(10)

for button in buttons:
    if button.text == 'Post':
        button.click()