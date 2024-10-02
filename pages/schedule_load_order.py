import time

from appium.webdriver.common.appiumby import AppiumBy


class ScheduleLoad:
  def __init__(self, driver):
    self.driver = driver
    
    self.elem = '//android.widget.TextView[@text="Schedule Load Order"]'
    self.ver = '//android.view.View[@text="Schedule Load Order"]'
    self.select_terminal = '//android.widget.TextView[@text="AM - 6789"]'
    self.date_el = '(//android.widget.TextView[@text=""])[1]'
    self.select_date = '//android.view.View[@content-desc="06 October 2024"]'
    self.date_ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.time_el = '(//android.widget.TextView[@text=""])[2]'
    self.time_ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.product = '//android.view.ViewGroup[@resource-id="product-0"]'
    self.product_elem = '//android.widget.TextView[@text="101010"]'
    self.gross_el = '//android.widget.EditText[@resource-id="vol-0"]'
    self.supplier_el = '//android.view.ViewGroup[@resource-id="supplier-0"]'
    self.select_supplier = '//android.widget.TextView[@text="test test"]'
    self.carrier_el = '//android.view.ViewGroup[@resource-id="carrier-0"]'
    self.select_carrier = '//android.widget.TextView[@text="3a / 3a"]'
    self.submit_elem = '//android.view.ViewGroup[@resource-id="submit"]'
    
  def ScheduleOrder(self):
    elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.elem)
    elem.click()
    time.sleep(1)
    
    ver = self.driver.find_element(by=AppiumBy.XPATH, value=self.ver)
    assert ver.text == "Schedule Load Order"
    print("WELCOME TO ANOTHER TEST!")
    
  def SelectTerminal(self):
    select_terminal = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_terminal)
    select_terminal.click()
    time.sleep(1)
    
  def DateElem(self):
    date_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.date_el)
    date_el.click()
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
    
  def Product(self):
    product = self.driver.find_element(by=AppiumBy.XPATH, value=self.product)
    product.click()
    time.sleep(1)
    
    product_elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.product_elem)
    product_elem.click()
    time.sleep(1)
    
  def GrossElem(self, gross):
    gross_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.gross_el)
    gross_el.send_keys(gross)
    time.sleep(1)
    
  def SupplierElem(self):
    supplier_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.supplier_el)
    supplier_el.click()
    time.sleep(1)
    
    select_supplier = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_supplier)
    select_supplier.click()
    time.sleep(1)
    
  def CarrierElem(self):
    carrier_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.carrier_el)
    carrier_el.click()
    time.sleep(1)
    
    select_carrier = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_carrier)
    select_carrier.click()
    time.sleep(1)
    
  def Submit(self):
    submit_elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.submit_elem)
    submit_elem.click()
    time.sleep(1)

