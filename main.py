import time
import pandas
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://lwfoundationschool.org/livetv/registration/'

pd = pandas.read_csv('3266 names - Sheet1.csv')
title = pd.to_dict()['title']
# print(title)
first_name = pd.to_dict()['first name']
middle_name = pd.to_dict()['middle name']
last_name = pd.to_dict()['last name']
kc_id = pd.to_dict()['kc id']
church = pd.to_dict()['church']

data_dict = {}
for i in range(len(title)):
    data_dict[i] = {
        'title': str(title[i]).lower(),
        'first_name': first_name[i],
        'middle_name': str(middle_name[i]),
        'last_name': last_name[i],
        'kc_id': kc_id[i],
        'church': church[i]
    }

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
for n in range(len(data_dict)):
    zone = driver.find_element(By.XPATH, '//*[@id="field_dog0z"]')
    zone.click()
    zone.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN)
    zone.send_keys(Keys.ENTER)

    proceed = driver.find_element(By.LINK_TEXT, 'Proceed To Register')
    proceed.click()

    title = driver.find_element(By.ID, 'input_331_1')
    if data_dict[n]['title'] == 'brother':
        title.send_keys('B')
    elif data_dict[n]['title'] == 'sister':
        title.send_keys('S')
    title.send_keys(Keys.ENTER)

    fname = driver.find_element(By.NAME, 'input_3')
    if data_dict[n]['middle_name'] == 'nan':
        fname.send_keys(data_dict[n]['first_name'])
    else:
        fname.send_keys(f"{data_dict[n]['first_name']} {data_dict[n]['middle_name']}")

    lname = driver.find_element(By.NAME, 'input_4')
    lname.send_keys(data_dict[n]['last_name'])

    kc_id = driver.find_element(By.NAME, 'input_6')
    kc_id.send_keys(data_dict[n]['kc_id'])

    church = driver.find_element(By.NAME, 'input_8')
    church.send_keys(data_dict[n]['church'])

    following = driver.find_element(By.NAME, 'input_9')
    following.click()
    following.send_keys(Keys.ARROW_DOWN)
    following.send_keys(Keys.ENTER)

    role = driver.find_element(By.NAME, 'input_13')
    role.click()
    role.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN)
    role.send_keys(Keys.ENTER)

    country = driver.find_element(By.NAME, 'input_15')
    country.click()
    country.send_keys('Nigeria')
    country.send_keys(Keys.ENTER)

    register = driver.find_element(By.ID, 'gform_submit_button_331')
    register.click()
    register.click()
    time.sleep(5)
    print(f"Done for {n + 1}.{data_dict[n]['first_name']} {data_dict[n]['last_name']}")

    driver.back()
    driver.refresh()
