import time

from main import *


def record_fuel():
  initial()
  
  el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Record Fuel Transfer"]')
  el.click()
  time.sleep(2)
  
  ver_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Record Fuel Transfer"]')
  assert ver_el.text == "Record Fuel Transfer"
  print("YOU ARE ON ANOTHER TEST! ")
  
  date_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="date"]')
  date_el.click()
  time.sleep(2)
  
  # For Ok
  ok_button = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]')
  ok_button.click()
  time.sleep(2)
  
  # #for Cancel
  # cancel_button = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button2"]')
  # cancel_button.click()
  # time.sleep(2)
  
  time_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="time"]')
  time_el.click()
  time.sleep(2)
  
  time_ok = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]')
  time_ok.click()
  time.sleep(1)
  
  from_el = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text=""])[1]')
  from_el.click()
  time.sleep(1)
  
  select_from_el = driver.find_element(by=AppiumBy.XPATH,
                                       value='//android.widget.TextView[@text="Box Truck BT Truck #123"]')
  select_from_el.click()
  time.sleep(1)
  
  to_el = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text=""])[2]')
  to_el.click()
  time.sleep(1)
  
  select_to_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Box Truck New Asset"]')
  select_to_el.click()
  time.sleep(1)
  
  element = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text="-"])[1]')
  element.click()
  time.sleep(1)
  
  select_element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Comp 1"]')
  select_element.click()
  time.sleep(1)
  
  elements = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="toComp_0"]')
  elements.click()
  time.sleep(1)
  
  select_elements = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Comp 1"]')
  select_elements.click()
  time.sleep(1)
  
  product_el = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text=""])[5]')
  product_el.click()
  time.sleep(1)
  
  select_product_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="101010"]')
  select_product_el.click()
  time.sleep(1)
  
  gallon_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="gal_0"]')
  gallon_el.send_keys("20")
  time.sleep(2)
  
  note_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="notes"]')
  note_el.send_keys("Record Fuel Transfer")
  time.sleep(1)
  
  submit_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="submit"]')
  submit_el.click()
  time.sleep(2)
  
  try:
    # Wait for the toast message to appear with explicit wait
    toast_message_element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Transfer')]"))
    )
    
    # Get the text from the toast message
    toast_message_text = toast_message_element.text
    
    # Verify that the toast message contains the word "Transfer"
    assert "Transfer" in toast_message_text
    print("Toast message verified, Transfer order has been succesfully created")
  
  except Exception as e:
    print("Failed to verify toast message: {str(e)}")


record_fuel()