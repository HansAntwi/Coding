from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


#USER INPUTS
chosen_currency = "USDGHS" #input("Enter the currency you want to select (e.g., USDGHS): \n").strip().upper()
start_date = "01 Mar 2025" #input("Enter the start date (01 Jan 2025): ").strip()
end_date = "01 June 2025" #input("Enter the end date (31 Jan 2025): ").strip()
output = input("Enter your preferred output format (1 for Excel or 2 for CSV): \n 1: Excel \n 2: csv \n").strip().upper()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.bog.gov.gh/treasury-and-the-markets/daily-interbank-fx-rates/')
#maximize window
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)

"""
STEPS:
1. Open the URL
2. Accept cookies
3. Click on historical data button
4. select currency pair
5. enter date range
6. filter for all
7. click export button to download
8. choose excel or csv
"""


#accept cookies
try:
    accept_cookies = driver.find_element(By.ID,'cookie_action_close_header')
    accept_cookies.click()
    print('cookies accepted')
except:
    print('no cookies to accept')

#historical button
try:
    historical_data_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'elementor-button-text'))
    )
    historical_data_button.click()
    print('historical button clicked')
except:
    print('Program could not reach here')


#select currency
try:
    currency_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="filter-option pull-left"])[3]')))
    # currency_dropdown = driver.find_element(By.XPATH, '(//span[@class="filter-option pull-left"])[3]')
    # currency_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '(//button[@class ="btn dropdown-toggle bs-placeholder btn-default"])[2]')))
    # currency_dropdown = driver.find_element(By.XPATH, '//th[@class="sort column-cd_currency_pair"]//button[@role="button"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", currency_dropdown)
    currency_dropdown.click()
    print('currency dropdown clicked')
    # time.sleep(2)
    print('looking for elements')
    # time.sleep(3)
    print('looking for elements again')
    currencies = wait.until(EC.visibility_of_all_elements_located(
   ( By.XPATH, '(//ul[@class="dropdown-menu inner"])[3]//span[@class="text"]'
    )
    ))
    print('elements found:', len(currencies))
    for currency in currencies:
        if currency.text.strip() == chosen_currency:
            currency.click()
            print('currency selected')
            break
except:
    print('could not select currency')



#select date range
try:
    start_date_input = wait.until(EC.presence_of_element_located((By.ID, 'table_1_range_from_0')))
    driver.execute_script("arguments[0].value = arguments[1];", start_date_input, start_date)
    driver.execute_script("var event = new Event('change', { bubbles: true }); arguments[0].dispatchEvent(event);", start_date_input)
    time.sleep(1)
    start_date_input.send_keys(Keys.ENTER)
    print('Start date set to {start_date}')
    
    end_date_input = wait.until(EC.presence_of_element_located((By.ID, 'table_1_range_to_0')))
    driver.execute_script("arguments[0].value = arguments[1];", end_date_input,  end_date)
    time.sleep(1)
    end_date_input.send_keys(Keys.ENTER)
    print('End date set to {end_date}')
except:
    print('could not find start date input')

#filter for all



#export button
try:
    export_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class = "dt-button buttons-collection DTTT_button DTTT_button_export"]')))
    print('export button located')
    driver.execute_script("arguments[0].scrollIntoView(true);", export_button)
    time.sleep(2)
    print('export button found')
    export_button.click()
    print('export button clicked')
except:
    print('could not find export button')


#click excel or csv
if output == 'EXCEL' or output == '1':
    try:
        Excel_output = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="dt-button buttons-excel buttons-html5"]'))).click()
        print('Excel output clicked')
        print('Excel file successfully downloaded')
    except:
        print('could not find excel output button')

if output == 'CSV' or output == '2':    
    try:
        CSV_output = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dt-button.buttons-csv.buttons-html5'))).click()
        print('CSV output clicked')
        print('CSV file successfully downloaded')
    except:
        print('could not find CSV output button')




"""
CANNOT USE SELENIUM TO ACCESS DOM ELEMENTS IN PRINT PREVIEW WINDOW


#click print button
# try:
#     print_button = driver.find_element(By.CLASS_NAME, "DTTT_button_print").click()
#     print('print button clicked')
#     # time.sleep(5)
# except:
#     print('couldnt find the button')
    
# # 
# driver.switch_to.window(driver.window_handles[1])
# print('switched to print preview window')

# auto_print = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
# print('print preview window located')

"""

    
input('Press Enter to exist: ')
driver.quit()

