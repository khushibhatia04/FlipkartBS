from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

driver = webdriver.Chrome()

try:
    # Load Flipkart home page
    driver.get("https://www.flipkart.com")
    wait = WebDriverWait(driver, 10)

    # Search  "Samsung Galaxy S10"
    search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
    search_box.send_keys("Samsung Galaxy S10")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Click on "Mobiles" category
    mobiles_category = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Mobiles")))
    mobiles_category.click()
    time.sleep(2)  

    # Apply filter by clicking on "SAMSUNG" text
    samsung_filter = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_6i1qKy" and contains(text(), "SAMSUNG")]')))
    samsung_filter.click()
    time.sleep(2)  

    # Apply "Flipkart Assured" filter
    flipkart_assured_filter = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="SwtzWS"]')))
    flipkart_assured_filter.click()
    time.sleep(2)  

    # Sort by Price -> High to Low
    sort_by_high_to_low = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="sHCOk2"]//div[text()="Price -- High to Low"]')))
    sort_by_high_to_low.click()
    time.sleep(8)  
 
    # Read results from page 1
    product_containers = driver.find_elements(By.XPATH, '//div[contains(@class, "_75nlfW")]')
        
    for index, container in enumerate(product_containers):
                
        try:
            product_name_element = container.find_element(By.XPATH, './/div[contains(@class, "KzDlHZ")]')
            product_name = product_name_element.text
        except Exception as e:
            product_name = "No product name found"
            print(f"Failed to find product name in container {index + 1}: {e}")
        
        try:
            product_price = container.find_element(By.XPATH, './/div[contains(@class, "hl05eU")]/div[contains(@class, "Nx9bqj") and contains(@class, "_4b5DiR")]').text
        except Exception as e:
            product_price = "No product price found"
            print(f"Failed to find product price in container {index + 1}: {e}")
        
        try:
            product_link = container.find_element(By.XPATH, './/a[contains(@class, "CGtC98")]').get_attribute("href")
        except Exception as e:
            product_link = "No product link found"
            print(f"Failed to find product link in container {index + 1}: {e}")
            
       
        print(f'Product Name: {product_name}')
        print(f'Display Price: {product_price}')
        print(f'Product Link: {product_link}')
        print('---------------------------------\n')
        
        time.sleep(0.5)

finally:
    driver.quit()




# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import sys

# sys.stdout.reconfigure(encoding='utf-8')

# username = os.environ.get('BROWSERSTACK_USERNAME')
# accessKey = os.environ.get('BROWSERSTACK_ACCESS_KEY')
# buildName = 'flipkart-bs'
# local = os.environ.get('BROWSERSTACK_LOCAL')
# localIdentifier = os.environ.get('BROWSERSTACK_LOCAL_IDENTIFIER')

# # Set BrowserStack capabilities
# bstack_options = {
#     "os" : "Windows",
#     "osVersion" : "10",
#     "sessionName" :  buildName,
#     "local": 'true',
#     "localIdentifier": 'localIdentifier040404',
#     "seleniumVersion" : "4.0.0",
#     "userName": username,
#     "accessKey": accessKey
# }

# options = webdriver.ChromeOptions()
# options.set_capability('bstack:options', bstack_options)

# driver = webdriver.Remote(
#     command_executor="https://hub.browserstack.com/wd/hub",
#     options=options
# )

# try:
#     # Load Flipkart home page
#     driver.get("https://www.flipkart.com")
#     wait = WebDriverWait(driver, 10)

#     # Search  "Samsung Galaxy S10"
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
#     search_box.send_keys("Samsung Galaxy S10")
#     search_box.send_keys(Keys.RETURN)
#     time.sleep(2)

#     # Click on "Mobiles" category
#     mobiles_category = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Mobiles")))
#     mobiles_category.click()
#     time.sleep(2)  

#     # Apply filter by clicking on "SAMSUNG" text
#     samsung_filter = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_6i1qKy" and contains(text(), "SAMSUNG")]')))
#     samsung_filter.click()
#     time.sleep(2)  

#     # Apply "Flipkart Assured" filter
#     flipkart_assured_filter = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="SwtzWS"]')))
#     flipkart_assured_filter.click()
#     time.sleep(2)  

#     # Sort by Price -> High to Low
#     sort_by_high_to_low = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="sHCOk2"]//div[text()="Price -- High to Low"]')))
#     sort_by_high_to_low.click()
#     time.sleep(3)  

#     # Wait for sorting to complete
#     time.sleep(3)  

#     # Read results from page 1
#     product_containers = driver.find_elements(By.XPATH, '//div[contains(@class, "_75nlfW")]')
    
#     for index, container in enumerate(product_containers):
#         try:
#             product_name_element = container.find_element(By.XPATH, './/div[contains(@class, "KzDlHZ")]')
#             product_name = product_name_element.text
#         except Exception as e:
#             product_name = "No product name found"
#             print(f"Failed to find product name in container {index + 1}: {e}")
        
#         try:
#             product_price = container.find_element(By.XPATH, './/div[contains(@class, "hl05eU")]/div[contains(@class, "Nx9bqj") and contains(@class, "_4b5DiR")]').text
#         except Exception as e:
#             product_price = "No product price found"
#             print(f"Failed to find product price in container {index + 1}: {e}")
        
#         try:
#             product_link = container.find_element(By.XPATH, './/a[contains(@class, "CGtC98")]').get_attribute("href")
#         except Exception as e:
#             product_link = "No product link found"
#             print(f"Failed to find product link in container {index + 1}: {e}")
            
#         print(f'Product Name: {product_name}')
#         print(f'Display Price: {product_price}')
#         print(f'Product Link: {product_link}')
#         print('---------------------------------\n')
        
#         time.sleep(1)  

# finally:
#     driver.quit()
