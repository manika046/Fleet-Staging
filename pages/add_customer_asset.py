import time
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main import *

PlateNum = [393, 646, 557, 455, 444, 809, 222]


def Add_customer_asset():
  initial()
  
  add_customer = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Add Customer Assets"]')
  add_customer.click()
  time.sleep(2)
  
  choose_customer = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Choose customer"]')
  choose_customer.click()
  time.sleep(2)
  
  ver = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Select a Customer"]')
  assert ver.text == "Select a Customer"
  print("ANOTHER STAGE!")
  
  select_customer = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="default-100 ASSETS CUSTOMER"]/android.view.ViewGroup')
  select_customer.click()
  time.sleep(2)
  
  choose_location = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Choose location"]')
  choose_location.click()
  time.sleep(2)
  
  sel_ver = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Select an Item"]')
  assert sel_ver.text == "Select an Item"
  print("SELECT AN ITEM! ")
  
  select_item = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="100 Assets -customer -shipto"]')
  select_item.click()
  time.sleep(2)
  
  choose_asset_type = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Choose asset type"]')
  choose_asset_type.click()
  time.sleep(2)
  
  # for vehicle
  select_asset_type = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="vehicle"]')
  select_asset_type.click()
  time.sleep(2)
  
  # vehicle = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="vehicle"]').text
  # assert "Vehicle" in vehicle
  # print("VEHICLE SELECTED SUCCESSFUL! ")
  
  asset_name = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter asset name"]')
  asset_name.send_keys("car")
  time.sleep(2)
  
  fueL_capacity = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter capacity"]')
  fueL_capacity.send_keys("50 liters")
  time.sleep(2)
  
  license_num = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter Licenseplate No."]')
  license_num.send_keys(random.choice(PlateNum))
  time.sleep(2)
  
  select_product = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text=""])[4]')
  select_product.click()
  time.sleep(2)
  
  product = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="101- Package product"]')
  product.click()
  time.sleep(2)
  
  create_button = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Create"]')
  create_button.click()
  time.sleep(2)
  
  # alert = driver.switch_to.alert
  # alert_el = alert.accept()
  # print(alert_el)
  
  try:
    # Wait for the toast message to appear with explicit wait
    toast_message_element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Asset')]"))
    )
    
    # Get the text from the toast message
    toast_message_text = toast_message_element.text
    
    # Verify that the toast message contains the word "Transfer"
    assert "Asset" in toast_message_text
    print("Toast message verified, new order schedule created!")
  
  except Exception as e:
    print("Failed to verify toast message: {str(e)}")


Add_customer_asset()