'''
Created on Aug 20, 2022

@author: manjo
'''
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import  Options
import os
from selenium.webdriver.chrome.service import Service

def SproutsCapture(item:str):
    #Chrome options are used to hide browser in background while scraping occurs
    chrome_options= Options()
    User=os.getlogin()
    service=Service(executable_path='/Users/{}/Downloads/chromedriver_win32/chromedriver.exe'.format(User))
    driver = webdriver.Chrome(service=service, options= chrome_options)
    driver.get('https://shop.sprouts.com/search?search_term={}'.format(item))
    products=[]
    #Sleep is required for browser actions to occur in given time-frame
    time.sleep(3) 
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    #With height of site recorded, below is a spider that crawls through the page in-order to load html elements that otherwise is hidden.
    for i in range(1, total_height, 100):
        driver.execute_script("window.scrollTo(0, {});".format(i))
    time.sleep(3)
    Names=driver.find_elements('xpath','//div[@class="css-15uwigl"]')
    Images=driver.find_elements('xpath','//div[@class="css-1l4w6pd"]/img')
    Price=driver.find_elements('xpath','//div[@class="css-0"]/span')
    #parse products
    for i in range(min(len(Names),len(Images),len(Price))):
        products.append([Names[i].get_attribute('title'),Price[i].get_attribute('innerHTML'), Images[i].get_attribute('src'), 'https://shop.sprouts.com/search?search_term={}'.format(item)])
    #Sort by price in increasing order
    products.sort(key=lambda x: float(x[1].split(' ')[0][1:]))
    return products
