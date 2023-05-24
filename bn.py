from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import names
import secrets
import random
import string
import os
from selenium.webdriver.common.by import By


chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://www.minitex.co/?r=73238')
time.sleep(15)
driver.find_element(by=By.XPATH, value='//*[@id="main"]/section[1]/div[2]/div/div[1]/div/a[1]').click()
time.sleep(15)
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






