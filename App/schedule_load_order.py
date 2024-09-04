from main import *


def Schedule_load():
  initial()
  
  elem = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Schedule Load Order"]')
  elem.click()
  time.sleep(1)
  
  ver = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Schedule Load Order"]')
  assert ver.text == "Schedule Load Order"
  print("WELCOME TO ANOTHER TEST!")
  
  select_terminal = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="AM - 6789"]')
  select_terminal.click()
  time.sleep(1)
  
  date_el = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text=""])[1]')
  date_el.click()
  time.sleep(1)
  
  select_date = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="06 September 2024"]')
  select_date.click()
  time.sleep(1)
  
  date_ok = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]')
  date_ok.click()
  time.sleep(1)
  
  time_el = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text=""])[2]')
  time_el.click()
  time.sleep(1)
  
  time_ok = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]')
  time_ok.click()
  time.sleep(1)
  
  product = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="product-0"]')
  product.click()
  time.sleep(1)
  
  product_elem = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="101010"]')
  product_elem.click()
  time.sleep(1)
  
  gross_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="vol-0"]')
  gross_el.send_keys("15")
  time.sleep(1)
  
  supplier_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="supplier-0"]')
  supplier_el.click()
  time.sleep(1)
  
  select_supplier = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="test test"]')
  select_supplier.click()
  time.sleep(1)
  
  carrier_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="carrier-0"]')
  carrier_el.click()
  time.sleep(1)
  
  select_carrier = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="3a / 3a"]')
  select_carrier.click()
  time.sleep(1)
  
  submit_elem = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="submit"]')
  submit_elem.click()
  time.sleep(1)


Schedule_load()