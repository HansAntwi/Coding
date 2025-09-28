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




course = input('Enter Programme to search: ')
"""
steps

1. open site
2. search for course
3. select english course
4. save as csv

"""

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://www.universitaly.it/')
wait = WebDriverWait(driver, 3)
driver.implicitly_wait(3)


#accepting cookies
try:
    cookies = driver.find_element(By.XPATH, '//div[contains(button, "Accept")]').click()
except:
    print("Failed to accept cookies")

#search for course
try:    
    search_field = driver.find_element(By.CLASS_NAME, 'form-control').send_keys(course+ Keys.ENTER)
except:
    print(f'Could not search for {course}')


#sort asc
try:
    sort_element = wait.until(EC.element_to_be_clickable(
        (By.ID, 'selectOrder'))).click()
    # sort_element.click()
    ascending_sort = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//option[@value="ASC"]'
    ))).click()
    otherr_filters_element = driver.find_element(By.CLASS_NAME, 'other-filters-header').click()
except:
    print('Could not sort ASC')

#selecting eng courses only
try:
    course_language = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="EN"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", course_language)
    time.sleep(1)
    course_language.click()
except:
    print('Could not select EN filter')


"""
PRINTING ALL DETAILS AT ONCE

page = 1
description = []
details_element = driver.find_elements(By.XPATH, '//div[@class="group-corso group-pink mb-3"]')

time.sleep(3)
for details in details_element:
    print(details.text.strip())
    print()
    
    # description.append(details.text.strip())
    # print(description) 
"""    
    
    



   
#Extracting relevant details
page = 1
All_Courses = [] #available courses
All_levels = [] #master's or bachelors
All_Universities = [] #universities
taught_in = [] #course is taught in this/these languages
durations = [] #how long it takes to complete the course
All_links = [] #url to the courses

while True:
    course_element = driver.find_elements(By.XPATH, '//div[@class="gordita-medium-outer-space-22px nome-corso"]')
    course_name = [course.text.strip() for course in course_element if course]
    # for course in course_element:
    #     print(course.text.strip())
    All_Courses.extend(course_name)
    
    
    levels_element = driver.find_elements(By.XPATH, '//i[@class="bi bi-book"]/..')
    levels = [level.text.strip().split()[-1] for level in levels_element if level]
    All_levels.extend(levels)
    
    
    university_elements = driver.find_elements(By.CLASS_NAME, 'nome-struttura')
    University_names = [university.text.strip() for university in university_elements if university]
    All_Universities.extend(University_names)
    
    
    languages_element = driver.find_elements(By.XPATH, '//i[@class="bi bi-chat-dots"]/..')
    languages = [language.text.strip() for language in languages_element if language]
    taught_in.extend(languages)
      
      
    duration_elements = driver.find_elements(By.XPATH, '//i[@class="bi bi-stopwatch"]/..')
    periods = [duration.text.strip() for duration in duration_elements if duration]
    durations.extend(periods)
    
    
    link_elements = driver.find_elements(By.CLASS_NAME, 'corso-button')
    href = [link.get_attribute('href') for link in link_elements]
    All_links.extend(href)
    
    try:    
        next_element = driver.find_elements(By.XPATH, '(//a[@class="page-link" and  text()="Next"])[1]')
        if not next_element:
            print(f'Search Successfully Completed \n{len(All_Courses)} Courses Found' )
            break
        
        next_element = driver.find_element(By.XPATH, '(//a[@class="page-link" and  text()="Next"])[2]')
        if next_element:
            wait.until(
                EC.element_to_be_clickable(next_element)
            )
            
            driver.execute_script("arguments[0].scrollIntoView;", next_element)
            driver.execute_script("arguments[0].click();", next_element)
            page += 1
            # print(f'Moving to page: {page}')
            # print()
            time.sleep(2)
    except:
        print('No more pages')
        
# print(f'Number of Courses found is {len(All_Courses)}')
# print(f'Number of Unis found : {len(All_Universities)}')
# print(f'Number of levels found is {len(All_levels)}')
# print(f'Number of Languages found : {len(taught_in)}')
# print(f'Number of Periods found : {len(durations)}')
# print(f'Number of links found : {len(All_links)}')


# print(All_Courses)
# print(All_Universities)
# print(All_levels)
# print(taught_in)
# print(durations)
# print(All_links)


df = pd.DataFrame({
    "Course": All_Courses,
    "University": All_Universities,
    "Masters/Bachelors": All_levels,
    "Language": taught_in,
    "Course Duration": durations,
    "Course Link": All_links
})


print(df)


df.to_csv(fr'C:\Users\HANS ANTWI\OneDrive\Documents\Python Coding\Coding\Selenium\STUDY IN ITALY\{course}.csv', index=False, encoding='utf-8-sig')


quit = input("Press Enter to quit")
driver.quit()

