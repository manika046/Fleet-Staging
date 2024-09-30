import time
import random

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PlateNum = [393, 646, 557, 455, 444, 809, 222]


class AddCustomerAsset:
  def __init__(self, driver):
    self.driver = driver
    
  def AddCustomer(self):
    add_customer = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Add Customer Assets"]')
    add_customer.click()
    time.sleep(2)
    
  def ChooseCustomer(self):
    choose_customer = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Choose customer"]')
    choose_customer.click()
    time.sleep(2)
    
  def CustomerVerify(self):
    ver = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Select a Customer"]')
    assert ver.text == "Select a Customer"
    print("ANOTHER STAGE!")
    
  def SelectCustomer(self):
    select_customer = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="default-100 ASSETS CUSTOMER"]/android.view.ViewGroup')
    select_customer.click()
    time.sleep(2)
    
  def ChooseLocation(self):
    choose_location = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Choose location"]')
    choose_location.click()
    time.sleep(2)
    
  def SelectVerify(self):
    sel_ver = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Select an Item"]')
    assert sel_ver.text == "Select an Item"
    print("SELECT AN ITEM! ")
    
  def SelectItem(self):
    select_item = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="100 Assets -customer -shipto"]')
    select_item.click()
    time.sleep(2)
    
  def ChooseAssetType(self):
    choose_asset_type = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Choose asset type"]')
    choose_asset_type.click()
    time.sleep(2)
    
  def SelectAssetType(self):
    # for vehicle
    select_asset_type = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="vehicle"]')
    select_asset_type.click()
    time.sleep(2)
    
    # vehicle = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="vehicle"]').text
    # assert "Vehicle" in vehicle
    # print("VEHICLE SELECTED SUCCESSFUL! ")
    
  def AssetName(self, asset):
    asset_name = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter asset name"]')
    asset_name.send_keys(asset)
    time.sleep(2)
    
  def FuelCapacity(self, capacity):
    fuel_capacity = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter capacity"]')
    fuel_capacity.send_keys(capacity)
    time.sleep(2)
    
  def LicenseNumber(self):
    license_num = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter Licenseplate No."]')
    license_num.send_keys(random.choice(PlateNum))
    time.sleep(2)
    
  def SelectProduct(self):
    select_product = self.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text=""])[4]')
    select_product.click()
    time.sleep(2)
    
  def Product(self):
    product = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="101- Package product"]')
    product.click()
    time.sleep(2)
    
  def CreateButton(self):
    create_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Create"]')
    create_button.click()
    time.sleep(2)
    
  def ToastMessage(self):
    try:
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Asset')]"))
      )
      
      toast_message_text = toast_message_element.text
      
      assert "Asset" in toast_message_text
      print("Toast message verified, new order schedule created!")
    
    except Exception as e:
      print("Failed to verify toast message: {str(e)}")