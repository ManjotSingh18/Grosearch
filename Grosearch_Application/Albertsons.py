'''
Created on Aug 22, 2022

@author: manjo
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import time
import re
import os
def AlbertsonCapture(item):
    #The chrome options are used to hide the selenium bowser that is scraping in the background
    chrome_options= Options()
    User=os.getlogin()
    driver = webdriver.Chrome('/Users/{}/Downloads/chromedriver_win32/chromedriver'.format(User), options= chrome_options)
    driver.get("https://www.albertsons.com/shop/search-results.html?q={}".format(item))
    #sleep is required for page elements to load in completely
    time.sleep(2.5) 
    Names=driver.find_elements('xpath','//a[@class="product-title__name"]')
    
    Price=driver.find_elements('xpath','//span[@class="product-price__saleprice product-price__discounted-price"]')
    
    Images=driver.find_elements('xpath', '//source[@media="(max-width: 575px)"]')
    
    products=[]
    # Products are parsed to return ones with full details
    for i in range(min(len(Names), len(Price), len(Images))):
        products.append([Names[i].get_attribute('innerHTML'), Price[i].get_attribute('innerHTML')[41:46], Images[i].get_attribute('data-srcset'), Names[i].get_attribute('href')])
    # Products sorted by price
    products.sort(key=lambda x: float(re.sub(r'[^a-zA-Z0-9_.]', '', x[1])))
    return products