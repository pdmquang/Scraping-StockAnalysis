from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

from utils import *

# Set up the Selenium WebDriver (make sure to specify the path to your WebDriver)
service = Service(executable_path='driver/chromedriver.exe')

options = Options()
options.binary_location = r"./chrome-win64/chrome.exe"
driver = webdriver.Chrome(service=service, options=options)

# Allow some time for the page to load
time.sleep(1)  # Adjust sleep time as necessary

income_metrics = ['Revenue', 'Gross Profit', 'Operating Income', 'Net Income', 'EPS (Diluted)', 'Operating Margin', 'Free Cash Flow']
balance = []
cashflow = []

symbols = ["FPT", "pdn"] # Import list from companies in HOSE.csv
period_type = 'trailing'

report_path = 'output/Companies Reports.xlsx'
writer = pd.ExcelWriter(report_path, engine = 'xlsxwriter')

# Income statements
for sym in symbols:
	income_statement = []

	sym = sym.upper()
	url = build_HOSE_url(sym, '', period_type)
	driver.get(url)

	navigate_report(driver)

	period_name = "Fiscal Year" if period_type == '' else 'Fiscal Quarter'
	period_col_name = get_values_by_metric(driver, period_name)

	for metric in income_metrics:
		values = get_values_by_metric(driver, metric)
		income_statement.append(values)
 
	df = pd.DataFrame(income_statement, columns=period_col_name)
	df.to_excel(writer, sheet_name = f"{sym}", index=False)

writer.close()
driver.quit()