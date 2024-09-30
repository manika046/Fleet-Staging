import time

from appium.webdriver.common.appiumby import AppiumBy


class MySchedule:
  def __init__(self, driver):
    self.driver = driver

  def Schedule(self):
    elem = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="My Schedule"]')
    elem.click()
    time.sleep(1)
    
    ver_text = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Weekly Schedule"]').text
    assert "Weekly" in ver_text
    print("ANOTHER TEST! ")
    
  def TextElement(self):
    text_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Your Tasks in this Week"]')
    assert text_el.text == "Your Tasks in this Week"
    print("YOUR TASK IN THIS WEEK: ")
  
  