from main import *


def ORDERWELL():
  initial()
  
  elem = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Order Well"]')
  elem.click()
  time.sleep(1)
  
  ver_text = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Order Well"]').text
  assert "Order" in ver_text
  print("STAGE: ORDER! ")
  
  
ORDERWELL()