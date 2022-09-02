'''
Created on Aug 22, 2022

@author: manjo
'''
from selenium import webdriver
import re
import time
import os
from selenium.webdriver.chrome.options import  Options

def CostCoCapture(item):
    chrome_options= Options()
    #user_agent is required to acsess page in its entirety
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    chrome_options.add_argument('user-agent={}'.format(user_agent))
    #Headless browser makes selenium 
    chrome_options.add_argument("--headless")
    User=os.getlogin()
    driver = webdriver.Chrome('/Users/{}/Downloads/chromedriver_win32/chromedriver'.format(User), options= chrome_options)
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
