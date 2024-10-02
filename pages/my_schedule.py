import time

from appium.webdriver.common.appiumby import AppiumBy


class MySchedule:
  def __init__(self, driver):
    self.driver = driver
    
    self.elem = '//android.widget.TextView[@text="My Schedule"]'
    self.ver_text = '//android.view.View[@text="Weekly Schedule"]'
    self.text_el = '//android.widget.TextView[@text="Your Tasks in this Week"]'

  def Schedule(self):
    elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.elem)
    elem.click()
    time.sleep(1)
    
    ver_text = self.driver.find_element(by=AppiumBy.XPATH, value=self.ver_text).text
    assert "Weekly" in ver_text
    print("ANOTHER TEST! ")
    
  def TextElement(self):
    text_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.text_el)
    assert text_el.text == "Your Tasks in this Week"
    print("YOUR TASK IN THIS WEEK: ")
  
  