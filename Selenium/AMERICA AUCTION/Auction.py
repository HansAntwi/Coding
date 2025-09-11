from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

email =  input("Enter your email: ").strip()
password = input("Enter your password: ").strip()
capital_town = input("Enter your capital town of the country you want(e.g., Accra): ").strip().title()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://online-auction.state.gov/en-US")
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)

"""
STEPS:
1. Open the URL
2. Accept cookies
3. Login
4. select country by capital town

"""

try:
    accept_cookies = driver.find_element(By.XPATH,'//a[@class="eupopup-button eupopup-button_1"]')
    accept_cookies.click()
    # print('cookies accepted')
except:
    print('no cookies to accept')
    

try:
    login_button = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    login_button.click()
    # print('login button clicked')
    
    
    #log in details
    user_name = wait.until(
        EC.presence_of_element_located((By.ID, 'Email'))
    )
    user_name.click()
    user_name.send_keys(email)
    print("email entered")
    
    password_element = wait.until(EC.presence_of_element_located((By.ID, 'Password')))
    password_element.click()
    password_element.send_keys(password)
    # print("password entered")
    
    submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit" and  @value="Log in"]')))
    submit_button.click()
    # print("successfully logged in")
    
    text_found = wait.until(
        EC.presence_of_element_located((By.XPATH, '(//div[@class=" your-auctions-title border-bottom"])[1]'))
    )
   #if this text "Your Winning Auctions" is found, then login is successful
    text_found = "Your Winning Auctions" in text_found.text
    if text_found:
        print("Login successful")
    else:
        print("Login failed")
        
except Exception as e:
    print('login button not found', e)

try:
    capital_towns = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="label-postname"]')))
    print(len(capital_towns))      
    print([town.text.strip() for town in capital_towns[1:]])
    # for town in capital_towns:
    #     if capital_town in town.text.strip():
    #         # time.sleep(1)
    #         ActionChains(driver).move_to_element(town).click().perform()
    #         # town.click()
    #         print(f'{capital_town} selected')
    #         break
    #     # if town.text.strip() == capital_town:
    #     #     town.click()
    #     #     print(f'{capital_town} selected')
    #         break
except Exception as e:
    print(f'could not find {capital_town}', e)











close_window = input("Press Enter to close the browser window...")
driver.quit()
