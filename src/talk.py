
#!/home/pi/robotEnv/bin python 

import os
import os.path
import yaml


ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))

with open('{}/src/conversation.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    custom_conversation = yaml.load(conf, Loader=yaml.FullLoader)

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options
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

Website = 'https://www.naturalreaders.com/online/'
driver.get(Website)

sleep(0.5)
driver.find_element(by=By.XPATH, value='//*[@id="v_5"]').click()
driver.find_element(by=By.XPATH, value='/html/body/app-root/app-voice-selection/div/div[3]/button').click()

sleep(3)
#driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()
#driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-page"]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[1]/span[1]/svg/use').click()

#sleep(1)
#driver.find_element(by=By.XPATH, value='//*[@id="mat-dialog-0"]/app-pw-voices/mat-dialog-content/div/mat-selection-list/mat-list-option[5]/div/div[2]/div/div[1]').click()
#driver.find_element(by=By.XPATH, value='//*[@id="mat-dialog-0"]/app-pw-voices/div/div/button').click()


def say(Text):
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()
        sleep(0.5)

    except:
        pass

    Data = str(Text)
    sleep(0.5)
    xpathtec = '//*[@id="inputDiv"]'
    driver.find_element(by=By.XPATH, value=xpathtec).click()
    sleep(0.5)
    driver.find_element(by=By.XPATH, value=xpathtec).send_keys(Data)
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-page"]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[3]').click()
    sleep(2)

    
    print("")
    print(f" Robot-Niko Answer : {Text}.")
    print("")
