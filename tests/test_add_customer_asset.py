from tests.test_dashboard import *
from pages.add_customer_asset import AddCustomerAsset


class TestAddCustomerAsset(TestDashBoard):
  
  def test_add_customer(self, driver_setup):
    TestDashBoard.test_dashboard(self, driver_setup)
    
    add_customer = AddCustomerAsset(driver_setup)
    
    add_customer.AddCustomer()
    add_customer.ChooseCustomer()
    add_customer.CustomerVerify()
    add_customer.SelectCustomer()
    add_customer.ChooseLocation()
    add_customer.SelectVerify()
    add_customer.SelectItem()
    add_customer.ChooseAssetType()
    add_customer.SelectAssetType()
    add_customer.AssetName("truck")
    add_customer.FuelCapacity("75 liters")
    add_customer.LicenseNumber()
    add_customer.SelectProduct()
    add_customer.CreateButton()
    add_customer.ToastMessage()
    
    