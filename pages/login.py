import time
# import os
# from pathlib import Path
#
# from appium import webdriver
# from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
# from dotenv import load_dotenv
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = AppiumOptions()
# options.load_capabilities({
#   "platformName": "android",
#   "appium:automationName": "uiautomator2",
#   "appium:platformVersion": "15",
#   "appium:deviceName": "Pixel 7a API 35",
#   "appium:app": "C:\\Users\\acer\\Downloads\\app-staging-release.apk",
# })
#
# dotenv_path = Path('../.venv/.env')
# load_dotenv(dotenv_path=dotenv_path)
#
# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
# driver.implicitly_wait(5)


class LoginPage:
  def __init__(self, driver):
    self.driver = driver
    
    self.image_element = "//android.widget.ImageView"
    self.url_text = '//android.widget.TextView[@text="Enter the Base URL"]'
    self.base_url = '//android.widget.EditText[@resource-id="base-url"]'
    self.submit_el = '//android.widget.TextView[@text="Submit"]'
    self.signin_button = '//android.widget.TextView[@text="SIGN IN"]'
    self.mobile_text = '//android.widget.TextView[@text="Mobile Number"]'
    self.input_element = '//android.widget.EditText[@resource-id="phone-number-entry"]'
    self.continue_button = '//android.view.ViewGroup[@resource-id="phone-verify"]'
    self.password_text = '//android.widget.TextView[@text="Enter Password"]'
    self.password = '//android.widget.EditText[@resource-id="password"]'
    self.login_element = '//android.widget.TextView[@text="Login"]'
    self.verify_text = '//android.widget.TextView[@resource-id="com.android.permissioncontroller:id/permission_message"]'
    
    print("STARTING TEST: ")
    
  def ImageElement(self):
    self.driver.implicitly_wait(10)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.image_element).click()
    time.sleep(1)
    
  def URLText(self):
    url_text = self.driver.find_element(by=AppiumBy.XPATH, value=self.url_text).text
    assert "Enter the Base URL" in url_text
    print("CLICKED! ")
    
  def BaseUrl(self, url):
    base_url = self.driver.find_element(by=AppiumBy.XPATH, value=self.base_url)
    base_url.send_keys(url)
    time.sleep(2)
    
  def Submit(self):
    submit_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.submit_el)
    submit_el.click()
    time.sleep(2)
    
  def SignInButton(self):
    signin_button = self.driver.find_element(by=AppiumBy.XPATH, value=self.signin_button)
    signin_button.click()
    time.sleep(2)
    
  def MobileText(self):
    mobile_text = self.driver.find_element(by=AppiumBy.XPATH, value=self.mobile_text).text
    assert "Mobile Number" in mobile_text
    print("YOU CAN INPUT NUMBER HERE! ")
    
  def InputElement(self, number):
    input_element = self.driver.find_element(by=AppiumBy.XPATH, value=self.input_element)
    input_element.send_keys(number)
    time.sleep(2)
    
  def ContinueButton(self):
    continue_button = self.driver.find_element(by=AppiumBy.XPATH, value=self.continue_button)
    continue_button.click()
    time.sleep(2)
    
  def PasswordText(self):
    password_text = self.driver.find_element(by=AppiumBy.XPATH, value=self.password_text).text
    assert "Enter Password" in password_text
    print("YOU CAN INPUT PASSWORD! ")
  
  def Password(self, password):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.password).send_keys(password)
    time.sleep(2)

  def LoginButton(self):
    login_element = self.driver.find_element(by=AppiumBy.XPATH, value=self.login_element)
    login_element.click()
    time.sleep(2)

  def VerifyText(self):
    verify_text = self.driver.find_element(by=AppiumBy.XPATH, value=self.verify_text)
    assert verify_text.text == 'Allow Staging Fleetpanda to find, connect to, and determine the relative position of nearby devices?'
    print("SIGN IN SUCCESS!")
  
  #   # for allow
  #   # allow_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
  #   # allow_el.click()
  #
  #   # for don't allow
  #   dont_allow_element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
  #   dont_allow_element.click()
  #   time.sleep(2)
  #
  #   loc_text = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Location Access"]')
  #   assert loc_text.text == "Location Access"
  #   print("STAGE CLEAR! ")
  #
  #   # for allow location access
  #   loc_allow = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Allow"]')
  #   loc_allow.click()
  #   time.sleep(2)
  #
  #   loc_access = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.android.permissioncontroller:id/permission_message"]')
  #   assert loc_access.text == "Allow Staging Fleetpanda to access this device’s location?"
  #   print("STAGE2 CLEAR! ")
  #
  #   # # for deny location access
  #   # loc_deny = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Deny"]')
  #   # loc_deny.click()
  #   # time.sleep(2)
  #
  #   # #for while using app
  #   # using_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]')
  #   # using_el.click()
  #   # time.sleep(2)
  #   #
  #   # # for only this time
  #   # only_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_one_time_button"]')
  #   # only_el.click()
  #   # time.sleep(2)
  #
  #   # for don't allow
  #   dont_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
  #   dont_el.click()
  #   time.sleep(2)
  #
  #   # okay_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Great! you do not have any tasks right now to perform"]')
  #   # assert "Great!" in okay_el.text
  #   # print("OKAY! ")
  #
  #   menu_bar = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text=""]')
  #   menu_bar.click()
  #   time.sleep(2)
  #
  # # initial()