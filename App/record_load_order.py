import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
  
  only_this_time = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_one_time_button"]')
  only_this_time.click()
  time.sleep(1)
  
  bol_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="bol-number"]')
  bol_el.send_keys("254")
  time.sleep(1)
  
  image_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text=""]')
  image_el.click()
  time.sleep(1)
  
  choose_img = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Choose from Library"]')
  choose_img.click()
  time.sleep(1)
  
  image = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')
  image.click()
  time.sleep(1)
  
  card_in = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="card-in-time"]')
  card_in.send_keys("0950")
  time.sleep(1)
  
  card_out = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="card-out-time"]')
  card_out.send_keys("1800")
  time.sleep(1)
  
  card_date = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="card-in-date"]')
  card_date.click()
  time.sleep(1)
  
  date_ok_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]')
  date_ok_el.click()
  time.sleep(1)
  
  supplier_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="supplier"]')
  supplier_el.click()
  time.sleep(1)
  
  select_supplier = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Dummy Supplier II"]')
  select_supplier.click()
  time.sleep(1)
  
  product_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="select-product"]')
  product_el.click()
  time.sleep(1)
  
  select_product = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="15-ppm sulfer diesel- dyed"]')
  select_product.click()
  time.sleep(1)
  
  gross_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="total-gross"]')
  gross_el.send_keys("2000")
  time.sleep(1)
  
  net_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="total-net"]')
  net_el.send_keys("1500")
  time.sleep(1)
  
  comp_5_net = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-0"]')
  comp_5_net.send_keys("200")
  time.sleep(1)
  
  comp_1_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-1"]')
  comp_1_el.send_keys("200")
  time.sleep(1)
  
  comp_2_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-2"]')
  comp_2_el.send_keys("200")
  time.sleep(1)
  
  comp_3_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-3"]')
  comp_3_el.send_keys("200")
  time.sleep(1)
  
  comp_6_net = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-4"]')
  comp_6_net.send_keys("200")
  time.sleep(1)
  
  comp_1_net = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-5"]')
  comp_1_net.send_keys("200")
  time.sleep(1)
  
  comp_2_net = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-6"]')
  comp_2_net.send_keys("100")
  time.sleep(1)
  
  comp_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-7"]')
  comp_el.send_keys("200")
  time.sleep(1)
  
  next_el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="next"]')
  next_el.click()
  time.sleep(1)
  
  # delay_no = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="delay-no"]')
  # delay_no.click()
  # time.sleep(1)
  
  delay_yes = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Yes"]')
  delay_yes.click()
  time.sleep(1)
  
  types_delay = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="delay-reason"]')
  types_delay.send_keys("Anything")
  time.sleep(1)
  
  done_loading = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="done-loading"]')
  done_loading.click()
  time.sleep(1)
  
  try:
    # Wait for the toast message to appear with explicit wait
    toast_message_element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Record')]"))
    )
    
    # Get the text from the toast message
    toast_message_text = toast_message_element.text
    
    # Verify that the toast message contains the word "Transfer"
    assert "Record" in toast_message_text
    print("Toast message verified, new order schedule created!")
  
  except Exception as e:
    print("Failed to verify toast message: {str(e)}")


RecordLoadOrder()