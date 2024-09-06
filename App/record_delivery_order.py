import time

from main import *


def RecordDelivery():
  initial()
  
  elem = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Record Delivery Order"]')
  elem.click()
  time.sleep(1)
  
  ver = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text="Record Delivery Order"])[1]')
  assert ver.text == "Record Delivery Order"
  print("ANOTHER TEST!")
  
  select_customer = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="cell-0"]')
  select_customer.click()
  time.sleep(1)
  
  asset_el = driver.find_element(by=AppiumBy.XPATH, value='(//android.view.ViewGroup[@resource-id="asset-0"])[1]')
  asset_el.click()
  time.sleep(1)
  
  select_asset = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="107 - LCR"]')
  select_asset.click()
  time.sleep(1)
  
  asset_ell = driver.find_element(by=AppiumBy.XPATH, value='(//android.view.ViewGroup[@resource-id="asset-1"])[1]')
  asset_ell.click()
  time.sleep(1)
  
  select_asset_ell = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="AG Trailer 1"]')
  select_asset_ell.click()
  time.sleep(1)
  
  customer_branch = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="branch"]')
  customer_branch.click()
  time.sleep(1)
  
  select_branch = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="100 Assets -customer -shipto"]')
  select_branch.click()
  time.sleep(1)
  
  date_elem = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="date"]')
  date_elem.click()
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
  
  search_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="search"]')
  search_el.send_keys("car")
  time.sleep(1)
  
  select_search_el = driver.find_element(by=AppiumBy.XPATH, value='(//android.view.ViewGroup[@resource-id="asset-0"])[2]')
  select_search_el.click()
  time.sleep(1)
  
  driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-0"]').click()
  time.sleep(1)
  
  
RecordDelivery()