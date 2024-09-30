from tests.test_dashboard import *
from pages.record_delivery_order import RecordDelivery


class TestRecordDeliveryOrder(TestDashBoard):
  
  def test_record_delivery(self, driver_setup):
    TestDashBoard.test_dashboard(self, driver_setup)
    
    delivery = RecordDelivery(driver_setup)
    
    delivery.RecordDeliveryOrder()
    delivery.SelectCustomer()
    delivery.AssetElement()
    delivery.CustomerBranch()
    delivery.DatTime()
    delivery.Search()
    delivery.Click()
    
    
    