from main import *


def RecordLoadOrder():
  initial()
  
  choose_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Record Load Order"]')
  choose_el.click()
  time.sleep(1)


RecordLoadOrder()