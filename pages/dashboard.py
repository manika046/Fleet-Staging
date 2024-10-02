import time

from appium.webdriver.common.appiumby import AppiumBy


class DashBoard:
  def __init__(self, driver):
    self.driver = driver
    
    self.allow_el = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'
    self.dont_allow_element = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]'
    self.loc_text = '//android.widget.TextView[@text="Location Access"]'
    self.loc_allow = '//android.widget.TextView[@text="Allow"]'
    self.loc_access = '//android.widget.TextView[@resource-id="com.android.permissioncontroller:id/permission_message"]'
    self.loc_deny = '//android.widget.TextView[@text="Deny"]'
    self.using_el = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'
    self.only_el = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_one_time_button"]'
    self.dont_el = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]'
    self.okay_el = '//android.widget.TextView[@text="Great! you do not have any tasks right now to perform"]'
    self.menu_bar = '//android.widget.TextView[@text=""]'
  
  def AllowElem(self):
    allow_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.allow_el)
    allow_el.click()

  def DontAllowElem(self):
    dont_allow_element = self.driver.find_element(by=AppiumBy.XPATH, value=self.dont_allow_element)
    dont_allow_element.click()
    time.sleep(2)

  def LocationText(self):
    loc_text = self.driver.find_element(by=AppiumBy.XPATH, value=self.loc_text)
    assert loc_text.text == "Location Access"
    print("STAGE CLEAR! ")

  def LocationAllow(self):
    loc_allow = self.driver.find_element(by=AppiumBy.XPATH, value=self.loc_allow)
    loc_allow.click()
    time.sleep(2)

  def LocationAccess(self):
    loc_access = self.driver.find_element(by=AppiumBy.XPATH, value=self.loc_access)
    assert loc_access.text == "Allow Staging Fleetpanda to access this device’s location?"
    print("STAGE2 CLEAR! ")

  def LocationDeny(self):
    loc_deny = self.driver.find_element(by=AppiumBy.XPATH, value=self.loc_deny)
    loc_deny.click()
    time.sleep(2)

  def UsingApp(self):
    using_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.using_el)
    using_el.click()
    time.sleep(2)
  
  def OnlyThisTime(self):
    only_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.only_el)
    only_el.click()
    time.sleep(2)

  def DontAllow(self):
    dont_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.dont_el)
    dont_el.click()
    time.sleep(2)

  # only when there is no tasks assign
  def OkayElem(self):
    okay_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.okay_el)
    assert "Great!" in okay_el.text
    print("OKAY! ")
  
  def MenuBar(self):
    menu_bar = self.driver.find_element(by=AppiumBy.XPATH, value=self.menu_bar)
    menu_bar.click()
    time.sleep(2)