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




# course = input('Enter Programme to search: ')
preferred_country = "United States" #input('Enter full name of the country: ')

"""
steps

1. open site
2. accept cookies
3. choose a country (usa default)
4 select no application fee schools
5. select offescools with financial aid
6. save as csv

"""

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://www.commonapp.org/explore/')
wait = WebDriverWait(driver, 3)
driver.implicitly_wait(3)
execute = driver.execute_script

try:
    cookies_element = driver.find_element(By.XPATH, '(//button[@class="cky-btn cky-btn-accept"])[1]').click()
except:
    print('No cookies accepted')
    
      
#choose a country
try:
    location_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Location")]'))).click()
    time.sleep(2)
    country_element = wait.until(EC.element_to_be_clickable((By.ID, 'country-location-input')))
    driver.execute_script("arguments[0].scrollIntoView;", country_element)
    driver.execute_script("arguments[0].click();", country_element)
    countries = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains (@id,"country-location-option") and contains(@value,"")]')))
    for country in countries:
        country.get_attribute('value')
        if preferred_country.lower() in country.text.strip().lower():
            driver.execute_script("arguments[0].click();", country)
except:
    print('No country found. Check the name and try again')     
time.sleep(1)

#select first year application
try:
    FY_student = driver.find_element(By.XPATH, '//*[contains(text(),"Application for first-year students")]')
    driver.execute_script("arguments[0].click();", FY_student)

    No_app_fee = wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "caf-first-year")]')))
    driver.execute_script("arguments[0].scrollIntoView(true);",No_app_fee)
    driver.execute_script("arguments[0].click();", No_app_fee)

    time.sleep(1)

    #select financial aid
    financial_aid = wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(span,"Financial aid")]')))
    execute("arguments[0].scrollIntoView(true);", financial_aid)
    execute("arguments[0].click();", financial_aid)
    aid_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[contains(@id,"finaid")]')))
    for aid in aid_elements:
        execute("arguments[0].scrollIntoView(true);",aid)
        execute("arguments[0].click();", aid)
except:
    print('No selections made')
    
    
#print search result
schools = []
locations = []
try:
    search_results = wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"search-results")]')))
    
    print(f'{search_results.text.strip().split()[0]} colleges in {preferred_country.title()} with Financial aid and no application fees found ')


    #school names
    number_of_schools = int(search_results.text.strip().split()[0])
    print(f'Number of schools found: {number_of_schools}')
    
    school_names = driver.find_elements(By.CLASS_NAME, 'school-name')
    schools = [school.text.strip() for school in school_names if school]
    # print(schools)
    
    location_of_schools = driver.find_elements(By.XPATH, '//p[contains(@class,"school-location")]') 
    locations = [location.text.strip() for location in location_of_schools if location]
    # print(locations)
    
    
    while len(schools) < number_of_schools:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        school_names = driver.find_elements(By.CLASS_NAME, 'school-name')
        schools = [school.text.strip() for school in school_names]
        location_of_schools = driver.find_elements(By.XPATH, '//p[contains(@class,"school-location")]') 
        locations = [location.text.strip() for location in location_of_schools if location]
        # print(f'{schools}:{locations}\n\n')
        print(f"Schools loaded: {len(school_names)}/{number_of_schools}\n")
    print(f"Done! Loaded {len(schools)} schools and {len(locations)} locations")

    # print(schools)
    # print(locations)

except:
    print('No search result found')
    
df = pd.DataFrame({
    "School": schools,
    "Location": locations
})

df.to_csv(fr'C:\Users\HANS ANTWI\OneDrive\Documents\Python Coding\Coding\Selenium\STUDY IN USA\CommonApp.csv', index=False, encoding="utf-8-sig")

quit = input('Press Enter to quit:')
driver.quit()