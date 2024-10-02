import time

from appium.webdriver.common.appiumby import AppiumBy


class RecordDelivery:
  def __init__(self, driver):
    self.driver = driver
    
    self.elem = '//android.widget.TextView[@text="Record Delivery Order"]'
    self.ver = '(//android.widget.TextView[@text="Record Delivery Order"])[1]'
    self.select_customer = '//android.view.ViewGroup[@resource-id="cell-0"]'
    self.asset_el = '(//android.view.ViewGroup[@resource-id="asset-0"])[1]'
    self.select_asset = '//android.widget.TextView[@text="107 - LCR"]'
    self.asset_ell = '(//android.view.ViewGroup[@resource-id="asset-1"])[1]'
    self.select_asset_ell = '//android.widget.TextView[@text="AG Trailer 1"]'
    self.customer_branch = '//android.view.ViewGroup[@resource-id="branch"]'
    self.select_branch = '//android.widget.TextView[@text="100 Assets -customer -shipto"]'
    self.date_elem = '//android.view.ViewGroup[@resource-id="date"]'
    self.select_date = '//android.view.View[@content-desc="06 October 2024"]'
    self.date_ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.time_el = '(//android.widget.TextView[@text=""])[2]'
    self.time_ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.search_el = '//android.widget.EditText[@resource-id="search"]'
    self.select_search_el = '(//android.view.ViewGroup[@resource-id="asset-0"])[2]'
    self.clicked = '//android.widget.EditText[@resource-id="compartment-0"]'
  
  def RecordDeliveryOrder(self):
    elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.elem)
    elem.click()
    time.sleep(1)
    
    ver = self.driver.find_element(by=AppiumBy.XPATH, value=self.ver)
    assert ver.text == "Record Delivery Order"
    print("ANOTHER TEST!")
    
  def SelectCustomer(self):
    select_customer = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_customer)
    select_customer.click()
    time.sleep(1)
    
  def AssetElement(self):
    asset_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.asset_el)
    asset_el.click()
    time.sleep(1)
    
    select_asset = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_asset)
    select_asset.click()
    time.sleep(1)
    
    asset_ell = self.driver.find_element(by=AppiumBy.XPATH, value=self.asset_ell)
    asset_ell.click()
    time.sleep(1)
    
    select_asset_ell = self.driver.find_element(by=AppiumBy.XPATH, value=self.asset_ell)
    select_asset_ell.click()
    time.sleep(1)
    
  def CustomerBranch(self):
    customer_branch = self.driver.find_element(by=AppiumBy.XPATH, value=self.customer_branch)
    customer_branch.click()
    time.sleep(1)
    
    select_branch = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_branch)
    select_branch.click()
    time.sleep(1)
    
  def DatTime(self):
    date_elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.date_elem)
    date_elem.click()
    time.sleep(1)
    
    select_date = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_date)
    select_date.click()
    time.sleep(1)
    
    date_ok = self.driver.find_element(by=AppiumBy.XPATH, value=self.date_ok)
    date_ok.click()
    time.sleep(1)
    
    time_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.time_el)
    time_el.click()
    time.sleep(1)
    
    time_ok = self.driver.find_element(by=AppiumBy.XPATH, value=self.time_ok)
    time_ok.click()
    time.sleep(1)
    
  def Search(self):
    search_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.search_el)
    search_el.send_keys("truck")
    time.sleep(1)
    
    select_search_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_search_el)
    select_search_el.click()
    time.sleep(1)
    
  def Click(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.clicked).click()
    time.sleep(1)
  
  
