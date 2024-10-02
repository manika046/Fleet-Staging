import time

from appium.webdriver.common.appiumby import AppiumBy


class RecordDelivery:
  def __init__(self, driver):
    self.driver = driver
  
  def RecordDeliveryOrder(self):
    elem = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Record Delivery Order"]')
    elem.click()
    time.sleep(1)
    
    ver = self.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text="Record Delivery Order"])[1]')
    assert ver.text == "Record Delivery Order"
    print("ANOTHER TEST!")
    
  def SelectCustomer(self):
    select_customer = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="cell-0"]')
    select_customer.click()
    time.sleep(1)
    
  def AssetElement(self):
    asset_el = self.driver.find_element(by=AppiumBy.XPATH, value='(//android.view.ViewGroup[@resource-id="asset-0"])[1]')
    asset_el.click()
    time.sleep(1)
    
    select_asset = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="107 - LCR"]')
    select_asset.click()
    time.sleep(1)
    
    asset_ell = self.driver.find_element(by=AppiumBy.XPATH, value='(//android.view.ViewGroup[@resource-id="asset-1"])[1]')
    asset_ell.click()
    time.sleep(1)
    
    select_asset_ell = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="AG Trailer 1"]')
    select_asset_ell.click()
    time.sleep(1)
    
  def CustomerBranch(self):
    customer_branch = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="branch"]')
    customer_branch.click()
    time.sleep(1)
    
    select_branch = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="100 Assets -customer -shipto"]')
    select_branch.click()
    time.sleep(1)
    
  def DatTime(self):
    date_elem = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="date"]')
    date_elem.click()
    time.sleep(1)
    
    select_date = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="06 September 2024"]')
    select_date.click()
    time.sleep(1)
    
    date_ok = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]')
    date_ok.click()
    time.sleep(1)
    
    time_el = self.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text=""])[2]')
    time_el.click()
    time.sleep(1)
    
    time_ok = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]')
    time_ok.click()
    time.sleep(1)
    
  def Search(self):
    search_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="search"]')
    search_el.send_keys("truck")
    time.sleep(1)
    
    select_search_el = self.driver.find_element(by=AppiumBy.XPATH, value='(//android.view.ViewGroup[@resource-id="asset-0"])[2]')
    select_search_el.click()
    time.sleep(1)
    
  def Click(self):
    self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-0"]').click()
    time.sleep(1)
  
  
