import time

from main import *


def RecordLoadOrder():
  initial()
  
  choose_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Record Load Order"]')
  choose_el.click()
  time.sleep(1)
  
  date_elem = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="date"]')
  date_elem.click()
  time.sleep(1)
  
  select_date = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="07 September 2024"]')
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
  
  truck_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="asset-0"]')
  truck_el.click()
  time.sleep(1)
  
  select_truck = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="1077"]')
  select_truck.click()
  time.sleep(1)
  
  trailer_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="asset-1"]')
  trailer_el.click()
  time.sleep(1)
  
  select_trailer_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="AG Trailer 1"]')
  select_trailer_el.click()
  time.sleep(1)
  
  trailer_elem = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="asset-2"]')
  trailer_elem.click()
  time.sleep(1)
  
  select_trailer_elem = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="AG Trailer 101"]')
  select_trailer_elem.click()
  time.sleep(1)
  
  terminal_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="cell-2"]')
  terminal_el.click()
  time.sleep(1)
  
  add_bol_detail = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="submit"]')
  add_bol_detail.click()
  time.sleep(1)


RecordLoadOrder()