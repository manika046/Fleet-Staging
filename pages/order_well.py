import time

from appium.webdriver.common.appiumby import AppiumBy


class OrderWell:
  def __init__(self, driver):
    self.driver = driver
  
  def Order(self):
    elem = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Order Well"]')
    elem.click()
    time.sleep(1)
    
  def VerifyText(self):
    ver_text = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Order Well"]').text
    assert "Order" in ver_text
    print("STAGE: ORDER! ")
  
  
