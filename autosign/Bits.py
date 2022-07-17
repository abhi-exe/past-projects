import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser=webdriver.Firefox(executable_path=r'C:\Users\User\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe')
browser.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
time.sleep(1)

unit=browser.find_element_by_id("identifierId")
unit.send_keys("f20201996@pilani.bits-pilani.ac.in")
unit.send_keys(Keys.RETURN)
time.sleep(2)

a=input("Enter the password for your ID: ")
unit=browser.find_element_by_name("password")
unit.send_keys(a)
unit.send_keys(Keys.RETURN)
time.sleep(3)

browser.execute_script('window.open("https://classroom.google.com/h")')
browser.switch_to.window(browser.window_handles[0])




