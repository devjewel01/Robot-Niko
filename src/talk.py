
#!/home/pi/robotEnv/bin python 

import os
import os.path
import yaml


ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))

with open('{}/src/conversation.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    custom_conversation = yaml.load(conf, Loader=yaml.FullLoader)

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('window-size=1920x1480')

PathofDriver = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=PathofDriver,options=chrome_options)
driver.maximize_window()


Website = "https://text-to-speech.org/"
driver.get(Website)

sleep(0.5)
driver.find_element(by=By.XPATH, value='//*[@id="select_language"]').click()
driver.find_element(by=By.XPATH, value='//*[@id="select_language"]/option[1]').click()


def say(Text):
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="clearBtn"]').click()
        sleep(0.5)

    except:
        pass

    Data = str(Text)
    xpathtec = '//*[@id="text_box"]'
    driver.find_element(by=By.XPATH, value=xpathtec).click()
    driver.find_element(by=By.XPATH, value=xpathtec).send_keys(Data)
    sleep(0.5)
    driver.find_element(by=By.XPATH, value='//*[@id="play_button"]').click()

    print("")
    print(f" Robot-Niko Answer : {Text}.")
    print("")

