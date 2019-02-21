from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

name = input("enter the username:")
mssg =input ('enter messg to send:')
number=int(input("enter the count:"))

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com/')
time.sleep(3)

search=driver.find_element_by_class_name("jN-F5")
search.send_keys(name)
time.sleep(3)
search.click()
search.send_keys(Keys.RETURN)

for i in range(number):
    msg_box=driver.find_element_by_class_name("_2S1VP")
    msg_box.send_keys(mssg)
    time.sleep(2)
    button = driver.find_element_by_class_name('_35EW6')
    button.click() 
    time.sleep(3)
    
    
driver.close()
