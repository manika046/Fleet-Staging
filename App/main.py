import time
import os
from pathlib import Path

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv

options = AppiumOptions()
options.load_capabilities({
  "platformName": "android",
  "appium:automationName": "uiautomator2",
  "appium:platformVersion": "15",
  "appium:deviceName": "Pixel 7a API 35",
  "appium:app": "C:\\Users\\acer\\Downloads\\app-staging-release.apk",
})

dotenv_path = Path('../.venv/.env')
load_dotenv(dotenv_path=dotenv_path)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
driver.implicitly_wait(5)


def initial():
  print("STARTING TEST: ")
  
  image_element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView')
  image_element.click()
  time.sleep(2)
  
  url_text = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Enter the Base URL"]').text
  assert "Enter the Base URL" in url_text
  print("CLICKED! ")
  
  base_url = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="base-url"]')
  base_url.send_keys("test.fleetpanda.com")
  time.sleep(2)
  
  submit_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Submit"]')
  submit_el.click()
  time.sleep(2)
  
  signin_button = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="SIGN IN"]')
  signin_button.click()
  time.sleep(2)
  
  mobile_text = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Mobile Number"]').text
  assert "Mobile Number" in mobile_text
  print("YOU CAN INPUT NUMBER HERE! ")
  
  input_element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="phone-number-entry"]')
  input_element.send_keys(os.getenv('NUMBER'))
  time.sleep(2)
  
  continue_button = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="phone-verify"]')
  continue_button.click()
  time.sleep(2)
  
  password_text = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Enter Password"]').text
  assert "Enter Password" in password_text
  print("YOU CAN INPUT PASSWORD! ")
  
  password = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="password"]')
  password.send_keys(os.getenv('PASSWORD'))
  time.sleep(2)
  
  login_element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Login"]')
  login_element.click()
  time.sleep(2)
  
  verify_text = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.android.permissioncontroller:id/permission_message"]')
  assert verify_text.text == 'Allow Staging Fleetpanda to find, connect to, and determine the relative position of nearby devices?'
  print("SIGN IN SUCCESS!")
  
  # for allow
  # allow_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
  # allow_el.click()
  
  # for don't allow
  dont_allow_element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
  dont_allow_element.click()
  time.sleep(2)
  
  loc_text = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Location Access"]')
  assert loc_text.text == "Location Access"
  print("STAGE CLEAR! ")
  
  # for allow location access
  loc_allow = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Allow"]')
  loc_allow.click()
  time.sleep(2)
  
  loc_access = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.android.permissioncontroller:id/permission_message"]')
  assert loc_access.text == "Allow Staging Fleetpanda to access this device’s location?"
  print("STAGE2 CLEAR! ")
  
  # # for deny location access
  # loc_deny = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Deny"]')
  # loc_deny.click()
  # time.sleep(2)
  
  # #for while using app
  # using_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]')
  # using_el.click()
  # time.sleep(2)
  #
  # # for only this time
  # only_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_one_time_button"]')
  # only_el.click()
  # time.sleep(2)
  
  # for don't allow
  dont_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
  dont_el.click()
  time.sleep(2)
  
  # okay_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Great! you do not have any tasks right now to perform"]')
  # assert "Great!" in okay_el.text
  # print("OKAY! ")
  
  menu_bar = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text=""]')
  menu_bar.click()
  time.sleep(2)

# initial()