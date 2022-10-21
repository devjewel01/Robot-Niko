#  - Listen Functions

# 1- Selenium Based Speech Recognition

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
PathofDriver = "Driver/chromedriver"
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic":1})
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(PathofDriver,options=chrome_options)
driver.maximize_window()
driver.get('https://www.google.com/')

def SpeechRecognition():
    sleep(1)
    print(" Listening........ ")
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[2]').click()
    sleep(5)
    voice = driver.title
    print(voice)
    query = str(voice).replace(" - Google Search","")
    query = str(query).replace("Google","")
    sleep(1)
    driver.get('https://www.google.com/')
    print(f" You Said : {query}.")
    return query

