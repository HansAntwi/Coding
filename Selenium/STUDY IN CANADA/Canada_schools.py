from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_options = Options()
chrome_options.add_argument('--log-level=3')  # Suppress all logging
chrome_options.add_argument('--disable-logging')  # Disable logging
chrome_options.add_argument('--silent')  # Silent mode
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

province_choice = input("Enter a province: ") 

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/prepare/designated-learning-institutions-list.html')
wait = WebDriverWait(driver, 3)
driver.implicitly_wait(3)
execute = driver.execute_script




province_options = driver.find_elements(By.XPATH, '//select[@id="wb-auto-20"]//option[contains(value,"")]')


province_list = [province.text.strip() for province in province_options[1:]]
count = len(province_list)
print(count)
print(province_list)
# while count>0:
   
# num_provinces = 0
# while num_provinces < count:
# for i in province_list:
#     province_choice = i
province_options = driver.find_elements(By.XPATH, '//select[@id="wb-auto-20"]//option[contains(value,"")]')
for province in province_options:
    if province_choice.title() in province.text.strip():
        province.click()
        
try:
    all_filter_element = driver.find_elements(By.XPATH, '//select[contains(@name,"wb-auto")]')
    for filter in all_filter_element[1:]:
        if filter:
            driver.execute_script("arguments[0].scrollIntoView(true);", filter)
    all_option_filter = driver.find_elements(By.XPATH, '(//select[contains(text(),"")])//option[contains(text(),"")]')

    # driver.execute_script("arguments[0].scrollIntoView(true);", all_option_filter)
    for option in all_option_filter:
        if option.text.strip().lower() == "all":
            # time.sleep(1)
            option.click()
            print(f'all button clicked for {province_choice}')
            # break
except:
    print(f'Could not filter') 
        
try:
    table_path = '//table[@class="wb-tables table wb-init wb-tables-inited dataTable no-footer"]' #each prov has diff attrs
    main_table = driver.find_elements(By.XPATH, f"{table_path}")
    for table in main_table:
        if table:
            driver.execute_script("arguments[0].scrollIntoView(true);", table)
        # //*[contains(@id, "wb-auto-25_wrapper")]//th[contains(@class,"sorting")]

            headers_path = '//th[contains(@class,"sorting'
            headers = table.find_elements(By.XPATH, f'.{headers_path}")]')
            print(len(headers))
            col_headers = [header.text.strip() for header in headers if header != ""]
            print(col_headers)

            tr_path = '//tr'
            all_details = table.find_elements(By.XPATH, f'.{tr_path}')
            print(len(all_details))
            print()

            new_row_data = []
            for row in all_details[1:]:
                cells = row.find_elements(By.XPATH, './/td')
                com_row_data = [cell.text.strip() for cell in cells]
                # print(com_row_data)
                new_row_data.append(com_row_data)
                print(len(new_row_data))
                # break

            df = pd.DataFrame(columns=col_headers, data=new_row_data)
            print(df.head())
            df.to_csv(fr'C:\Users\HANS ANTWI\OneDrive\Documents\Python Coding\Coding\Selenium\STUDY IN CANADA\Canada_schools_{province_choice}.csv', index=False, encoding='utf-8-sig')
          

except:
    print(f'Couldn\'t save as csv' )
    print(f'done with {province_choice}\n')
    # # else:
    #     print(f'There is no filter for all; or \nThere is no designated learning institution in {province_choice} ')

# num_provinces += 1
# driver.refresh()
# time.sleep(2)

    
    # try:
        #### ANOTHER OPTION TO GET ALL SELECTED 
        
   #         all_option_filter = driver.find_elements(By.XPATH, '//select[@name="wb-auto-25_length"]//option[contains(text(),"")]')       
        # for option in all_option_filter:
        #     if option.get_attribute('value') == "-1":
        #         option.click()
    





quit = input('Press enter to quit')
driver.quit()