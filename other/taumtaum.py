# Import Python Library from Selenium WebDriver

import time
import requests
import array as arr
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Open ChromeDriver
go = webdriver.Chrome()

# Redirect to URL
URL = 'http://localhost'

go.get(URL)

go.maximize_window()

go.implicitly_wait(2)

# Input Email and Password in Login Form
go.find_element(By.ID, 'MemberLoginForm_LoginForm_Email').send_keys('monotaro@yopmail.com')
go.find_element(By.ID, 'MemberLoginForm_LoginForm_Password').send_keys('Qcaz123456')

go.find_element(By.ID, 'MemberLoginForm_LoginForm_action_doLogin').click()

time.sleep(3)

number = 2

while number != 0 :
    
    # Click Whitelist
    # go.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/ul/li[45]/a/span[2]').click()
    go.find_element(By.XPATH, '//*[@id="Menu-dbt_whitelistAdmin"]/a/span[2]').click()
    
    
    # Click Chevron icon
    go.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/form/fieldset/fieldset/div[2]/div[1]/button').click()
    go.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/form/fieldset/fieldset/div[1]/div/div/div/div/button[1]').click()
    time.sleep(2)
    go.find_element(By.XPATH, '//*[@id="Form_Dbt_whitelistsSearchForm_Search_requester_name"]').send_keys(' ')
    go.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/form/fieldset/fieldset/div[1]/div/div/div/div/div[2]/div/button[1]').click()

    # Click Button Approve
    time.sleep(2)

    try :
        Approve = go.find_element(By.XPATH, '//*[@id="Form_EditForm_dbt_whitelist"]/table/tbody/tr[1]/td[5]/a[1]')
        Approve.click()
        
        if go.find_element(By.XPATH, '//*[@id="Form_EditForm_dbt_whitelist"]/table/tbody/tr[1]/td[5]/a[1]'):
            break

    except NoSuchElementException :
                continue
    time.sleep(5)