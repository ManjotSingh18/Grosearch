'''
Created on Aug 22, 2022

@author: manjo
'''
from selenium import webdriver
import re
import time
import os
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.chrome.service import Service

def CostCoCapture(item):
    chrome_options= Options()
    #user_agent is required to access page in its entirety
    #Headless browser makes selenium 
    User=os.getlogin()
    service=Service(executable_path='/Users/{}/Downloads/chromedriver_win32/chromedriver.exe'.format(User))
    driver = webdriver.Chrome(service=service, options= chrome_options)
    driver.get("https://www.costco.com/CatalogSearch?dept=All&keyword={}".format(item))
    #Sleep is required for elements of page to fully load
    time.sleep(3) 
    time.sleep(1)
    Price=driver.find_elements('xpath','//div[@class="price"]')
    
    Names=driver.find_elements('xpath','//span[@class="description"]/a')

    Images=driver.find_elements('xpath','//a[@class="product-image-url"]/img')

    products=[]
    #Products are parsed with nessecary information, if image is not found a default image is passed
    for i in range(min(len(Names), len(Images), len(Price))):
        if Images[i].get_attribute('src'):  
            products.append([Names[i].get_attribute('innerHTML').strip(), re.sub(r'[^a-zA-Z0-9_.]', '', Price[i].get_attribute('innerHTML')), Images[i].get_attribute('src'), Names[i].get_attribute('href')])
        else:
            products.append([Names[i].get_attribute('innerHTML').strip(), re.sub(r'[^a-zA-Z0-9_.]', '', Price[i].get_attribute('innerHTML')), 'https://t3.ftcdn.net/jpg/04/62/93/66/360_F_462936689_BpEEcxfgMuYPfTaIAOC1tCDurmsno7Sp.jpg', Names[i].get_attribute('href')])
    #Lowest-price sort
    products.sort(key=lambda x: float(x[1]))
    return products
