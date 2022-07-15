from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os
import shutil
import time
import ntpath

from time import sleep

print('Starting...')

url = "https://www.barchart.com/futures/quotes/NQZ20/historical-download"

username = "sellmorehomes@gmail.com"
password = "BARchart007$"




CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = './chromedriver'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.add_argument('--user-data-dir=./User_Data')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--remote-debugging-port=9222")
# chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])

print('chrome initied...')

preferences = {
                # "profile.default_content_settings.popups": 0,
                "download.default_directory": os.getcwd() + os.path.sep,
                # "directory_upgrade": True
            }

chrome_options.add_experimental_option('prefs', preferences)

chrome_options.binary_location = CHROME_PATH
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)



driver.maximize_window()
driver.get(url)
main_page = driver.current_window_handle

# login in if not logined

try:
	driver.find_element_by_xpath('/html/body/main/div/div[1]/div[1]/div/div/div[2]/div[1]/a[1]').click()

	sleep(10)

	# Login part
	email = driver.find_element_by_xpath("//input[@name='email']").send_keys(username)
	password = driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
	driver.find_element_by_xpath("//button[@type='submit']").click()
	sleep(10)

except Exception as e:
	print('Already logined')




# Fill data Part
def fill_form(start_date,end_date):

	# change drop down
	select = Select(driver.find_element_by_xpath('//select[@data-ng-model="frequency"]'))
	select.select_by_value('string:nearby_minutes')

	# select minute to 1
	minute_text_box = driver.find_element_by_xpath('//input[@name="aggregation"]')
	minute_text_box.clear()
	minute_text_box.send_keys(1)

	# set start date
	start_date_text_box = driver.find_element_by_xpath('//input[@name="dateFrom"]')
	start_date_text_box.clear()
	start_date_text_box.send_keys(Keys.CONTROL + "a")
	start_date_text_box.send_keys(Keys.DELETE);



	start_date_text_box.send_keys(start_date)


	# set end date
	end_date_text_box = driver.find_element_by_xpath('//input[@name="dateTo"]')
	end_date_text_box.clear()
	end_date_text_box.send_keys(Keys.CONTROL + "a")
	end_date_text_box.send_keys(Keys.DELETE);

	end_date_text_box.send_keys(end_date)


	# hit the download
	minute_text_box = driver.find_element_by_xpath('//a[@data-historical="historical"]').click()


def move_old_files():
	Initial_path = os.getcwd()
	filename = max([Initial_path + "/" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
	base_file_name = os.path.basename(filename)
	final_name = base_file_name+f"-{time.time()} - file.csv"
	shutil.move(filename,os.path.join(Initial_path,final_name))

# part 2

import datetime
from datetime import date

print('It process may take 8 or more days...')
print('--------------------')

# getting start date
start_date = datetime.datetime(2020, 2, 16)

# geting today
today = today = date.today()

# download interval in sec
DOWNLOAD_INTERVAL = 10

is_first_download = True
while True:

	# update today
	today = today = date.today()
	

	print(f'today: {start_date}')

	for i in range(100):	
		
		if not is_first_download:
			move_old_files()

		next_date = start_date + datetime.timedelta(minutes=6*24*60)

		start_date_str = start_date.date().strftime("%m/%d/%Y")
		next_date_str = next_date.date().strftime("%m/%d/%Y")

		print(f'running for: {start_date_str } - {next_date_str }')
		fill_form(start_date_str,next_date_str)
		print('seeping for download')
		print('--------------------')

		is_first_download = False

		sleep(DOWNLOAD_INTERVAL)

		start_date = next_date

		if start_date.date()>today:
			break


	if start_date.date()>today:
		break


	#  day finish 
	print('sleeping for next day')
	sleep(24*60*60)
	print('***************************************')
