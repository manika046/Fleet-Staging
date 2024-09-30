import time

from appium.webdriver.common.appiumby import AppiumBy


class DashBoard:
  def __init__(self, driver):
    self.driver = driver
    
    self.allow_el = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'
  
  def AllowElem(self):
    allow_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.allow_el)
    allow_el.click()

  def DontAllowElem(self):
    dont_allow_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
    dont_allow_element.click()
    time.sleep(2)

  def LocationText(self):
    loc_text = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Location Access"]')
    assert loc_text.text == "Location Access"
    print("STAGE CLEAR! ")

  def LocationAllow(self):
    loc_allow = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Allow"]')
    loc_allow.click()
    time.sleep(2)

  def LocationAccess(self):
    loc_access = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.android.permissioncontroller:id/permission_message"]')
    assert loc_access.text == "Allow Staging Fleetpanda to access this device’s location?"
    print("STAGE2 CLEAR! ")

  def LocationDeny(self):
    loc_deny = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Deny"]')
    loc_deny.click()
    time.sleep(2)

  def UsingApp(self):
    using_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]')
    using_el.click()
    time.sleep(2)
  
  def OnlyThisTime(self):
    only_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_one_time_button"]')
    only_el.click()
    time.sleep(2)

  def DontAllow(self):
    dont_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
    dont_el.click()
    time.sleep(2)

  # only when there is no tasks assign
  def OkayElem(self):
    okay_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Great! you do not have any tasks right now to perform"]')
    assert "Great!" in okay_el.text
    print("OKAY! ")
  
  def MenuBar(self):
    menu_bar = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text=""]')
    menu_bar.click()
    time.sleep(2)