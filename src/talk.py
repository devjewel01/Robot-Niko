
#!/home/pi/robotEnv/bin python 

import os
import os.path

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

#driver.find_element(by=By.XPATH, value='//*[@id="mat-dialog-6"]/app-pw-voices/div/div/div/button[2]/span[1]/div[2]').click()
#driver.find_element(by=By.XPATH, value='//*[@id="mat-dialog-6"]/app-pw-voices/mat-dialog-content/div/mat-selection-list/mat-list-option[9]/div/div[2]/div/div[1]').click()

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
    
    print("")
    print(f" Robot-Niko Answer : {Text}.")
    print("")
    sleep( max(3, len(Data)/12) )
