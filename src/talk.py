#!/usr/bin/env python3

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('window-size=1920x1480')

PathofDriver = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=PathofDriver,options=chrome_options)
driver.maximize_window()


Website = "https://ttsmp3.com/"
driver.get(Website)

sleep(0.5)
driver.find_element(by=By.XPATH, value='//*[@id="sprachwahl"]/option[51]').click()

def say(Text):
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="voicetext"]').clear()
        sleep(0.5)

    except:
        pass

    Data = str(Text)
    xpathtec = '//*[@id="voicetext"]'
    driver.find_element(by=By.XPATH, value=xpathtec).click()
    driver.find_element(by=By.XPATH, value=xpathtec).send_keys(Data)
    sleep(0.5)
    
    driver.find_element(by=By.XPATH, value='//*[@id="vorlesenbutton"]').click()
    
    print(f" Robot-Niko Answer : {Text}.")
    sleep( max(3, len(Data)/12) )
