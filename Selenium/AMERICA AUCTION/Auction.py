from selenium import webdriver
from selenium.webdriver.common.by import By
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


email =  input("Enter your email: ").strip()
password = input("Enter your password: ").strip()
capital_town = input("Enter your capital town of the country you want(e.g., Accra): ").strip().title()

"""STATUS NOT NEEDED FOR NOW"""
# reg_status = 1
# try:
#     reg_status = input('Enter the auction status you want (1: Active \n 2: Preparing": \n').strip().upper()
#     if reg_status == 1 or "ACTIVE":
#         reg_status = 'ACTIVE'
#     elif reg_status == 2 or "PREPARING":
#         reg_status = 'PREPARING'
# except:
#         print('Showing all auctions')


driver = webdriver.Chrome(options=chrome_options)
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
5. period left
6. items and descriptions
7. save as csv

"""

try:
    accept_cookies = driver.find_element(By.XPATH,'//a[@class="eupopup-button eupopup-button_1"]')
    accept_cookies.click()
    # print('cookies accepted')
except:
    print('no cookies to accept')
 
#loging in   
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
    # print("email entered")
    
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
    print('Could not log in. \nProvide valid details', e)
    

#selecting country by capital town
try:
    lots_available = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="num "]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", lots_available[0])
    lot_list = [lot.text.strip() for i,lot in enumerate(lots_available) if i ==0 or i % 2 == 0]
    # print(lot_list)
    
    capital_towns = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@style="text-align: center"]')))
    
    auction_status = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="status label "]')))

    # print(len(capital_towns))
    # print(len(auction_status))
    # list_capital_towns = [town.text.strip() for town in capital_towns]
    # print(list_capital_towns)
    # list_auction_status = [status.text.strip() for status in auction_status]
    # print(list_auction_status)
   
    for town, status, lot in zip(capital_towns, auction_status, lot_list):
        if capital_town in town.text.strip():
            print(f'{town.text.strip()}:-- Status: {status.text.strip()} -- Available Lots:{lot}')
            break
        
    else:
        print(f'could not find {capital_town}')
            
    for town, status in zip(capital_towns, auction_status):
        if capital_town in town.text.strip():
            time.sleep(1)
            # wait.until(
            #     EC.element_to_be_clickable((
            #         By.XPATH, '//div[@style="text-align: center"]')))
            driver.execute_script("arguments[0].scrollIntoView(true);", town)
            driver.execute_script("arguments[0].click();", town)
            time.sleep(1)
            # town.click()
            break  
    # else:
    #     print(f'could not click {capital_town}')
    #     """ DEPENDS ON STATUS IF NEEDED LATER
    #     if reg_status in status.text.strip() and capital_town in town.text.strip():
    #             town.click()
    #             print(f'{capital_town} selected')
    #             print(f'{town.text.strip()}: {status.text.strip()}')
    #         """
except Exception as e:
    print(f'could not find {capital_town}', e)

# ADD CONDITION TO FOR ACTIVE STATUS AND PREPARING 
#finding time left
try:
    active_status = wait.until(
    EC.presence_of_element_located((By.ID,"defaultCountdown")))
    time.sleep(1)
    if active_status:
   
        # time.sleep(1)
        time_desc = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'countdown-period')))
        all_td =[td.text.strip()  for td in time_desc]
        # print(all_td)
        
        time_left = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'countdown-amount')))
        all_tl = [tl.text.strip() for tl in time_left]
        # print(all_tl)
        
        full_period = ' '.join([f'{td}:{tl}' for td, tl in zip(all_td, all_tl)])
        print(f'Auction Ends In:-- {full_period}')
        
except:
        print('No Active Auction available now. Checking for Pending Auctions')
        try:
            driver.refresh
            preparing_status = wait.until(
                    EC.presence_of_element_located((
                        By.XPATH, '//span[contains(@style, "text-transform: uppercase;font-weight:bold;") and contains(text(), "Scheduled start date: ")]'
                    ))
                    )
                    # print('inside the pending auction zone')
            if preparing_status:
                # print('preparing element found')
                start_date = driver.find_element(
                        By.XPATH,'//span[@localdatetime="MMMM d, yyyy, HH:mm"]').text
                print(f'Auction Begins: {start_date}')
            else:
                print('No Pending Auction')
        except:
            print('No Active or Pending Auction Available')

   
#finding all items and descriptions
page = 1
all_lots = [] #lot number
all_items = [] #abailable items
all_lot_state = [] #lot status --usable
all_bid_status = [] #lot bidding state 
all_curr_bid_prices = [] # current bid price
all_lots_desc = [] #description of lot
all_urls = [] #urls of lots
while True:
    
    lots = driver.find_elements(By.XPATH, '(//div[@class="form-control input oa-bg-orange"])')
    needed_lots = lots[1::3]
    lots_num = [lot.text.strip() for lot in needed_lots]
    all_lots.extend(lots_num)  
    # print(lots_num)
    
    item_name = driver.find_elements(By.XPATH, '//div[@class="col-lg-9 col-md-8 col-sm-7 name-of-the-item"]')
    items = [item.text.strip() for item in item_name]
    all_items.extend(items)    # print(item.text.strip().title())
    
    lot_status = driver.find_elements(By.XPATH, '(//div[@class="form-control input oa-bg-orange" and @id=""])')
    needed_status = lot_status[0::2]
    lot_states = [lot_state.text.strip() for lot_state in needed_status]
    all_lot_state.extend(lot_states)
        
    status_elements = driver.find_elements(By.XPATH, '//div[@class="oa-generic-status-indicator"]')
    needed_bid_status = status_elements[0::2]
    bid_status = [status.get_attribute("textContent").strip() for status in needed_bid_status]
    all_bid_status.extend(bid_status)
    
    current_prices = driver.find_elements(By.XPATH, '//div[contains(@data-format,"01")]')
    currency_symbol = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(@class,"input-group-addon left fontBold")][1]'))).text.strip()
    
    # print(len(current_prices))
    prices = [price.text.strip() for i, price in enumerate(current_prices) if i%2 ==0]
    new_prices = [currency_symbol+" "+price for price in prices]
        
    all_curr_bid_prices.extend(new_prices)
    
    lot_desc_element = driver.find_elements(By.XPATH, '//div[@class="form-control textarea oa-bg-orange"]')
    needed_desc = lot_desc_element[0::2]
    lot_descs = [lot_desc.text.strip() for lot_desc in needed_desc]
    all_lots_desc.extend(lot_descs)
    
    lots_url_elements = driver.find_elements(By.XPATH, '//button[contains(text(),"View This Lot")]')
    needed_urls = lots_url_elements[0::2]
    urls = [url.get_attribute("onclick").split("'")[1] for url in needed_urls]
    base_url = 'https://online-auction.state.gov'
    new_urls = [base_url+url for url in urls]
    all_urls.extend(new_urls)
    
    
    
    
    for lot_num, item, lot_state, status, price, description, url in zip(lots_num, items, lot_states, bid_status, new_prices, lot_descs, new_urls):
        print(f'Lot {lot_num} \n {item} \n Lot Status -- {lot_state}\n Bidding Status -- {status} \n Current bid price is {price} \n Description: \n {description},\n Lot link -- {url}')
        print()
    
      
        
    try:
        last_page = driver.find_elements(By.XPATH, '//li[contains(@class,"disabled PagedList-skipToNext")]')
        if last_page:
            print('last page')
            # print()
            # print(all_lots) 
            # print()
            # print(all_items)
            # print()
            # print(all_bid_status)
            # print()
            # print(all_lot_state)
            # print()
            # print(all_curr_bid_prices)
            # print()
            # print(all_lots_desc)
            # print()
            # print(all_urls)
            break 
            
        """while next button is clickable"""
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@rel="next"]')))
        next_button.click()
        page += 1
        print(f'Moving to Page {page}')
        time.sleep(1)
      

    except:
        print('No more pages')
        break

print(len(all_lots))
print(len(all_items))
print(len(all_lot_state))
print(len(all_bid_status))
print(len(all_curr_bid_prices))
print(len(all_urls))



auction_df = pd.DataFrame(
    {
        "LOT NUMBER": all_lots,
        'ITEM': all_items,
        'LOT STATUS': all_lot_state,
        'BID STATUS': all_bid_status,
        "CURRENT BID PRICE": all_curr_bid_prices,
        "LOT DESCRIPTION": all_lots_desc,
        'LINK': all_urls
    }
)

# print(auction_df.info())
# print(auction_df.head())

#was getting extra character before currency symbol so i added encoding
auction_df.to_csv(r'C:\Users\HANS ANTWI\OneDrive\Documents\Python Coding\Coding\Selenium\AMERICA AUCTION\America_Auction.csv', index=False, encoding='utf-8-sig')

df_auction = pd.read_csv(r'C:\Users\HANS ANTWI\OneDrive\Documents\Python Coding\Coding\Selenium\AMERICA AUCTION\America_Auction.csv')
print(df_auction)





close_window = input("Press Enter to close the browser window...")
driver.quit()
