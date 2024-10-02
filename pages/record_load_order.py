from datetime import datetime, timedelta
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RecordLoadOrder:
  def __init__(self, driver):
    self.driver = driver
    
    self.choose_el = '//android.widget.TextView[@text="Record Load Order"]'
    self.date_elem = '//android.view.ViewGroup[@resource-id="date"]'
    self.date_ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.time_el = '(//android.widget.TextView[@text=""])[2]'
    self.time_ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.truck_el = '//android.view.ViewGroup[@resource-id="asset-0"]'
    self.select_truck = '//android.widget.TextView[@text="1077"]'
    self.trailer_el = '//android.view.ViewGroup[@resource-id="asset-1"]'
    self.select_trailer_el = '//android.widget.TextView[@text="AG Trailer 1"]'
    self.trailer_elem = '//android.view.ViewGroup[@resource-id="asset-2"]'
    self.select_trailer_elem = '//android.widget.TextView[@text="AG Trailer 101"]'
    self.terminal_el = '//android.view.ViewGroup[@resource-id="cell-2"]'
    self.add_bol_detail = '//android.view.ViewGroup[@resource-id="submit"]'
    self.only_this_time = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_one_time_button"]'
    self.bol_el = '//android.widget.EditText[@resource-id="bol-number"]'
    self.image_el = '//android.widget.TextView[@text=""]'
    self.choose_img = '//android.widget.TextView[@text="Choose from Library"]'
    self.image = '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]'
    self.card_date = '//android.view.ViewGroup[@resource-id="card-in-date"]'
    self.date_ok_el = '//android.widget.Button[@resource-id="android:id/button1"]'
    self.anywhere = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup'
    self.supplier_el = '//android.view.ViewGroup[@resource-id="supplier"]'
    self.select_supplier = '//android.widget.TextView[@text="Dummy Supplier II"]'
    self.product_el = '//android.view.ViewGroup[@resource-id="select-product"]'
    self.select_product = '//android.widget.TextView[@text="15-ppm sulfer diesel- dyed"]'
    self.gross_el = '//android.widget.EditText[@resource-id="total-gross"]'
    self.net_el = '//android.widget.EditText[@resource-id="total-net"]'

  def ChooseElem(self):
    choose_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.choose_el)
    choose_el.click()
    time.sleep(1)
    
  def DateElem(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.date_elem).click()
    time.sleep(1)
    
    # select_date = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="11 September 2024"]')
    # select_date.click()
    # time.sleep(1)
    
    date_ok = self.driver.find_element(by=AppiumBy.XPATH, value=self.date_ok)
    date_ok.click()
    time.sleep(1)
    
  def TimeElem(self):
    time_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.time_el)
    time_el.click()
    time.sleep(1)
    
    time_ok = self.driver.find_element(by=AppiumBy.XPATH, value=self.time_ok)
    time_ok.click()
    time.sleep(1)
    
  def TruckElem(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.truck_el).click()
    time.sleep(1)
    
    select_truck = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_truck)
    select_truck.click()
    time.sleep(1)
    
  def TrailerElem(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.trailer_el).click()
    time.sleep(1)
    
    select_trailer_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_trailer_el)
    select_trailer_el.click()
    time.sleep(1)
    
    self.driver.find_element(by=AppiumBy.XPATH, value=self.trailer_elem).click()
    time.sleep(1)
    
    select_trailer_elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_trailer_el)
    select_trailer_elem.click()
    time.sleep(1)
    
  def Terminal(self):
    terminal_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.terminal_el)
    terminal_el.click()
    time.sleep(1)
    
  def AddBOLDetail(self):
    add_bol_detail = self.driver.find_element(by=AppiumBy.XPATH, value=self.add_bol_detail)
    add_bol_detail.click()
    time.sleep(1)
   
  def OnlyThisTime(self):
    only_this_time = self.driver.find_element(by=AppiumBy.XPATH, value=self.only_this_time)
    only_this_time.click()
    time.sleep(1)
    
  def BOLElem(self, bol):
    bol_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.bol_el)
    bol_el.send_keys(bol)
    time.sleep(1)
    
  def Image(self):
    image_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.image_el)
    image_el.click()
    time.sleep(1)
    
    choose_img = self.driver.find_element(by=AppiumBy.XPATH, value=self.choose_img)
    choose_img.click()
    time.sleep(1)
    
    image = self.driver.find_element(by=AppiumBy.XPATH, value=self.image)
    image.click()
    time.sleep(1)
    
  def CardDate(self):
    card_date = self.driver.find_element(by=AppiumBy.XPATH, value=self.card_date)
    card_date.click()
    time.sleep(1)
    
    date_ok_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.date_ok_el)
    date_ok_el.click()
    time.sleep(1)
    
    current_time = datetime.now()
    print(current_time)
    target_time = current_time + timedelta(hours=5)  # add 5 hour
    print(target_time)
    out_time = target_time.strftime("%H%M")
    print(out_time)
    
    # card_in = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="card-in-time"]')
    # card_in.send_keys(current_time)
    # time.sleep(1)
    
    self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="card-out-time"]').click()
    card_out = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="card-out-time"]')
    card_out.send_keys(out_time)
    time.sleep(1)
    
  def Anywhere(self):
    anywhere = self.driver.find_element(by=AppiumBy.XPATH, value=self.anywhere)
    anywhere.click()
    time.sleep(1)
    
  def SupplierElem(self):
    supplier_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.supplier_el)
    supplier_el.click()
    time.sleep(1)
    
    select_supplier = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_supplier)
    select_supplier.click()
    time.sleep(1)
    
  def ProductElem(self):
    product_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.product_el)
    product_el.click()
    time.sleep(1)
    
    select_product = self.driver.find_element(by=AppiumBy.XPATH, value=self.select_product)
    select_product.click()
    time.sleep(1)
    
  def GrossElem(self, gross):
    gross_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.gross_el)
    gross_el.send_keys(gross)
    time.sleep(1)
    
  def NetElem(self, net):
    net_el = self.driver.find_element(by=AppiumBy.XPATH, value=self.net_el)
    net_el.send_keys(net)
    time.sleep(1)
    
  def CompElem(self):
    comp_5_net = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-0"]')
    comp_5_net.send_keys("200")
    time.sleep(1)
    
    comp_1_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-1"]')
    comp_1_el.send_keys("200")
    time.sleep(1)
    
    comp_2_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-2"]')
    comp_2_el.send_keys("200")
    time.sleep(1)
    
    comp_3_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-3"]')
    comp_3_el.send_keys("200")
    time.sleep(1)
    
    comp_6_net = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-4"]')
    comp_6_net.send_keys("200")
    time.sleep(1)
    
    comp_1_net = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-5"]')
    comp_1_net.send_keys("200")
    time.sleep(1)
    
    comp_2_net = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-6"]')
    comp_2_net.send_keys("100")
    time.sleep(1)
    
    comp_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="comp-7"]')
    comp_el.send_keys("200")
    time.sleep(1)
    
  def NextElem(self):
    next_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="next"]')
    next_el.click()
    time.sleep(1)
    
  def DelayNo(self):
    delay_no = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="delay-no"]')
    delay_no.click()
    time.sleep(1)
    
  def DelayYes(self):
    delay_yes = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Yes"]')
    delay_yes.click()
    time.sleep(1)
    
    types_delay = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="delay-reason"]')
    types_delay.send_keys("Anything")
    time.sleep(1)
    
    done_loading = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="done-loading"]')
    done_loading.click()
    time.sleep(1)
    
  def VerifyText(self):
    try:
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Record')]"))
      )
      
      toast_message_text = toast_message_element.text
      
      assert "Record" in toast_message_text
      print("Toast message verified, new order schedule created!")
    
    except Exception as e:
      print("Failed to verify toast message: {str(e)}")
