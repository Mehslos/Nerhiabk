# ------------------------------------------------------------ #
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import names
import secrets
import random
import string
import os
# ------------------------------------------------------------
CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
options = Options()
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH , chrome_options=options)
# ------------------------------------------------------------
driver.get('https://www.minitex.co/?r=73238')
time.sleep(10)
driver.find_element(by=By.XPATH, value='//*[@id="main"]/section[1]/div[2]/div/div[1]/div/a[1]').click()
time.sleep(10)
driver.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys(names)
time.sleep(4)
driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(main)
time.sleep(5)
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(main2)
time.sleep(6)
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').send_keys(main2)
time.sleep(6)
driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/div/div[7]/button').click()
time.sleep(10)
driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/div/div[3]/div[1]/div/span').click()
time.sleep(10)
driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/div/div[3]/div[2]/a[3]').click()
time.sleep(10)
driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/div[1]/div[7]/div/div[4]/div/input').send_keys(3)
time.sleep(10)
driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/div[1]/div[7]/div/div[6]/button').click()
time.sleep(random.randint(25,60))






