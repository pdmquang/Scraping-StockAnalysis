from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


def click_element(driver, locator):
	wait_element(driver, locator)
	driver.find_element(By.XPATH, locator).click()

def wait_element(driver, locator):
	WebDriverWait(driver, 15, 
			   ignored_exceptions=(StaleElementReferenceException,)).until(EC.presence_of_element_located((By.XPATH, locator)))