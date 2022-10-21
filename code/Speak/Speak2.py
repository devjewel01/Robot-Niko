from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
# chrome_options.headless = True
PathofDriver = "Driver/chromedriver"
driver = webdriver.Chrome(PathofDriver,options=chrome_options)
driver.maximize_window()

Website = 'https://www.naturalreaders.com/online/'

driver.get(Website)
sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()
driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-page"]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[1]').click()
sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="mat-dialog-0"]/app-pw-voices/mat-dialog-content/div/mat-selection-list/mat-list-option[4]/div/div[2]/div/div[1]').click()
driver.find_element(by=By.XPATH, value='//*[@id="mat-dialog-0"]/app-pw-voices/div/div/button').click()

def Speak(Text):

    try:
        driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()
        sleep(1)

    except:
        pass

    Data = str(Text)
    xpathtec = '//*[@id="inputDiv"]'
    driver.find_element(by=By.XPATH, value=xpathtec).click()
    driver.find_element(by=By.XPATH, value=xpathtec).send_keys(Data)
    driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-page"]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[3]').click()
    sleep(2)

    try:
        driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()
        sleep(1)

    except:
        pass

    print("")
    print(f" AI : {Text}.")
    print("")
