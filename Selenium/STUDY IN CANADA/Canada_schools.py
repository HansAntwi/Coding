from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_options = Options()
chrome_options.add_argument('--log-level=3')  # Suppress all logging
chrome_options.add_argument('--disable-logging')  # Disable logging
chrome_options.add_argument('--silent')  # Silent mode
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])



driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/prepare/designated-learning-institutions-list.html')
wait = WebDriverWait(driver, 3)
driver.implicitly_wait(3)
execute = driver.execute_script







quit = input('Press enter to quit')
driver.quit()