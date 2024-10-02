import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RecordFuel:
  
  def __init__(self, driver):
    self.driver = driver
    
    self.el = '//android.widget.TextView[@text="Record Fuel Transfer"]'
    self.ver_el = '//android.view.View[@text="Record Fuel Transfer"]'
    self.date_el = '//android.view.ViewGroup[@resource-id="date"]'
    self.ok_button = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.cancel_button = '//android.widget.Button[@resource-id="android:id/button2"]'
    self.time_el = '//android.view.ViewGroup[@resource-id="time"]'
    self.time_ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.from_el = '(//android.widget.TextView[@text=""])[1]'
    self.select_from_el = '//android.widget.TextView[@text="Box Truck BT Truck #123"]'
    self.to_el = '(//android.widget.TextView[@text=""])[2]'
    self.select_to_el = '//android.widget.TextView[@text="Box Truck New Asset"]'
    self.product_el = '(//android.widget.TextView[@text=""])[5]'
    self.select_product_el = '//android.widget.TextView[@text="101010"]'
    self.element = '(//android.widget.TextView[@text="-"])[1]'
    self.select_element = '//android.widget.TextView[@text="Comp 1"]'
    self.elements = '//android.view.ViewGroup[@resource-id="toComp_0"]'
    self.select_elements = '//android.widget.TextView[@text="Comp 1"]'
    self.gallon_el = '//android.widget.EditText[@resource-id="gal_0"]'
    self.note_el = '//android.widget.EditText[@resource-id="notes"]'
    self.submit_el = '//android.view.ViewGroup[@resource-id="submit"]'
  
  def TransferFuel(self):
    el = self.driver.find_element(by=AppiumBy.XPATH, value=self.el)
    el.click()
    time.sleep(2)
    
    ver_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.ver_el)
    assert ver_el.text == "Record Fuel Transfer"
    print("YOU ARE ON ANOTHER TEST! ")
    
  def Date(self):
    date_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.date_el)
    date_el.click()
    time.sleep(2)
    
  def OkButton(self):
    # For Ok
    ok_button = self.driver.find_element(by=AppiumBy.XPATH, value=self.ok_button)
    ok_button.click()
    time.sleep(2)
    
  def CancelButton(self):
    # For Cancel
    cancel_button = self.driver.find_element(by=AppiumBy.XPATH, value=self.cancel_button)
    cancel_button.click()
    time.sleep(2)
    
  def Time(self):
    time_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.time_el)
    time_el.click()
    time.sleep(2)
    
    time_ok = self.driver.find_element(by=AppiumBy.XPATH, value=self.time_ok)
    time_ok.click()
    time.sleep(1)
    
  def FromElement(self):
    from_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.from_el)
    from_el.click()
    time.sleep(1)
    
    select_from_el = self.driver.find_element(by=AppiumBy.XPATH, value= self.select_from_el)
    select_from_el.click()
    time.sleep(1)
    
  def ToElement(self):
    to_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.to_el)
    to_el.click()
    time.sleep(1)
    
    select_to_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_to_el)
    select_to_el.click()
    time.sleep(1)
    
  def Element(self):
    element = self.driver.find_element(by=AppiumBy.XPATH, value=self.element)
    element.click()
    time.sleep(1)
    
    select_element = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_element)
    select_element.click()
    time.sleep(1)
    
    elements = self.driver.find_element(by=AppiumBy.XPATH, value=self.elements)
    elements.click()
    time.sleep(1)
    
    select_elements = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_elements)
    select_elements.click()
    time.sleep(1)
    
  def Product(self):
    product_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.product_el)
    product_el.click()
    time.sleep(1)
    
    select_product_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_product_el)
    select_product_el.click()
    time.sleep(1)
    
  def Gallon(self, gallon):
    gallon_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.gallon_el)
    gallon_el.send_keys(gallon)
    time.sleep(2)
    
  def Note(self, note):
    note_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.note_el)
    note_el.send_keys(note)
    time.sleep(1)
    
  def Submit(self):
    submit_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.submit_el)
    submit_el.click()
    time.sleep(2)
    
  def VerifyText(self):
    try:
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Transfer')]"))
      )
      
      toast_message_text = toast_message_element.text
      
      assert "Transfer" in toast_message_text
      print("Toast message verified, Transfer order has been succesfully created")
    
    except Exception as e:
      print("Failed to verify toast message: {str(e)}")
