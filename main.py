from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from utils import *

# Set up the Selenium WebDriver (make sure to specify the path to your WebDriver)
service = Service(executable_path='driver/chromedriver.exe')

options = Options()
options.binary_location = r"./chrome-win64/chrome.exe"
driver = webdriver.Chrome(service=service, options=options)

# Allow some time for the page to load
time.sleep(1)  # Adjust sleep time as necessary

symbol = "FPT".upper()
url = get_HOSE_url(symbol, "", "trailing")
driver.get(url)

values = get_values_by_metric(driver, "Revenue", switch_order=True, format="b")
driver.quit()

# try:
#     # Locate the revenue element on the page
#     metric = "Revenue"
#     table_element = driver.find_element(By.XPATH, '//*[@id="main-table"]/tbody')
    
#     child_title_element = driver.find_element(By.XPATH, f"//a[text()='{metric}']")
#     parent_row = child_title_element.find_element(By.XPATH, "./ancestor::tr")

# except Exception as e:
#     print(f'Error occurred: {e}')
# finally:
#     # Close the browser
#     driver.quit()