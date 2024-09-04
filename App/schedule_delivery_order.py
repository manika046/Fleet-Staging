from main import *


def ScheduleDelivery():
  initial()
  
  elem = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Schedule Delivery Order"]')
  elem.click()
  time.sleep(1)
  
  select_customer = driver.find_element(by=AppiumBy.XPATH,
                                        value='//android.widget.TextView[@text="100 ASSETS CUSTOMER - 100-AC"]')
  select_customer.click()
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
  
  customer_site = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="customer"]')
  customer_site.click()
  time.sleep(1)
  
  select_customer = driver.find_element(by=AppiumBy.XPATH,
                                        value='//android.widget.TextView[@text="100 Assets -customer -shipto"]')
  select_customer.click()
  time.sleep(1)
  
  create_order = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Create Order"]')
  create_order.click()
  time.sleep(1)


ScheduleDelivery()