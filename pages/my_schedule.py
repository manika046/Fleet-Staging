from main import *


def MySchedule():
  initial()
  
  elem = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="My Schedule"]')
  elem.click()
  time.sleep(1)
  
  ver_text = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Weekly Schedule"]').text
  assert "Weekly" in ver_text
  print("ANOTHER TEST! ")
  
  text_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Your Tasks in this Week"]')
  assert text_el.text == "Your Tasks in this Week"
  print("YOUR TASK IN THIS WEEK: ")
  
  
MySchedule()