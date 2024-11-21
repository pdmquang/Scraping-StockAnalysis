from selenium.webdriver.common.by import By
from web_extraction import *

def get_HOSE_url(symbol, report_type="", period="Quarterly"):
	
	assert report_type in ["", "balance-sheet","cash-flow-statement","ratios"], \
			"Invalid value for 'report_type'. Must be '', 'balance-sheet','cash-flow-statement','ratios'."
	
	assert period in ["", "quarterly", "trailing"], \
			"Invalid value for 'period'. Must be '' or 'quarterly' or 'trailing'."
	
	url = f"https://stockanalysis.com/quote/hose/{symbol}/financials{'/' + report_type}/{'?p=' + period}"

	return url

def get_values_by_metric(driver, metric, switch_order=True, format="b"):
	assert format in ["", "b"], \
		"Invalid value for 'report_type'. Must be '', 'b'."
	
	try:
		if switch_order:
			switch_element = driver.find_element(By.XPATH, '//button[@title="Switch order of columns"]')
			if 'active' not in switch_element.get_attribute('class'):
				click_element(driver, '//button[@title="Switch order of columns"]')
			print(switch_element.get_attribute('class'))
		if format == 'b':
			click_element(driver, '//button[@title="Change number units"]')
			click_element(driver, '//button[contains(text(), "Billions")]')

		# switch_order
		# class contains `active`, eg `controls-btn sm:py-2 active`

		table_element = driver.find_element(By.XPATH, '//*[@id="main-table"]/tbody')
		
		child_title_element = table_element.find_element(By.XPATH, f"//a[text()='{metric}']")
		parent_row = child_title_element.find_element(By.XPATH, "./ancestor::tr")
		return process_row(parent_row.text)

	except Exception as e:
		print(f'Error occurred: {e}')
		return ""

def process_row(text):
	# 'Revenue\n59,931,389 57,790,313 55,029,450 52,617,901 50,962,143 48,348,957 45,960,653 44,009,528 41,678,929 39,255,542 37,801,189 35,657,263 33,619,912 32,447,868 30,786,163 29,830,401 29,283,884 28,835,129 28,681,045 27,716,960\nUpgrade'
	text_seq = text.split("\n")
	title = text_seq[0]
	values = text_seq[1].split(" ")
	return "\t".join([title] + values)
	