import time

from appium.webdriver.common.appiumby import AppiumBy


class ScheduleDelivery:
  def __init__(self, driver):
    self.driver = driver
    
    self.elem = '//android.widget.TextView[@text="Schedule Delivery Order"]'
    self.select_customer = '//android.widget.TextView[@text="100 ASSETS CUSTOMER - 100-AC"]'
    self.date_elem = '//android.view.ViewGroup[@resource-id="date"]'
    self.select_date = '//android.view.View[@content-desc="06 October 2024"]'
    self.date_ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.time_el = '(//android.widget.TextView[@text=""])[2]'
    self.time_ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.customer_site = '//android.view.ViewGroup[@resource-id="customer"]'
    self.select_customer = '//android.widget.TextView[@text="100 Assets -customer -shipto"]'
    self.create_order = '//android.widget.TextView[@text="Create Order"]'
    
  def ScheduleDelivery(self):
    elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.elem)
    elem.click()
    time.sleep(1)
    
  def SelectCustomer(self):
    select_customer = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_customer)
    select_customer.click()
    time.sleep(1)
    
  def DateElem(self):
    date_elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.date_elem)
    date_elem.click()
    time.sleep(1)
    
    select_date = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_date)
    select_date.click()
    time.sleep(1)
    
    date_ok = self.driver.find_element(by=AppiumBy.XPATH, value=self.date_ok)
    date_ok.click()
    time.sleep(1)
    
  def TimeElem(self):
    time_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.time_el)
    time_el.click()
    time.sleep(1)
    
    time_ok = self.driver.find_element(by=AppiumBy.XPATH, value=self.time_ok)
    time_ok.click()
    time.sleep(1)
    
  def CustomerSite(self):
    customer_site = self.driver.find_element(by=AppiumBy.XPATH, value=self.customer_site)
    customer_site.click()
    time.sleep(1)
    
    select_customer = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_customer)
    select_customer.click()
    time.sleep(1)
    
  def CreateOrder(self):
    create_order = self.driver.find_element(by=AppiumBy.XPATH, value=self.create_order)
    create_order.click()
    time.sleep(1)

