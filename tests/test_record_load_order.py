from tests.test_dashboard import *
from pages.record_load_order import RecordLoadOrder


class TestRecordLoadOrder(TestDashBoard):
  
  def test_record_load(self, driver_setup):
    TestDashBoard.test_dashboard(self, driver_setup)
    
    record_load = RecordLoadOrder(driver_setup)
    
    record_load.ChooseElem()
    record_load.DateElem()
    record_load.TimeElem()
    record_load.TruckElem()
    record_load.TrailerElem()
    record_load.Terminal()
    record_load.AddBOLDetail()
    record_load.OnlyThisTime()
    record_load.BOLElem("255")
    record_load.Image()
    record_load.CardDate()
    record_load.Anywhere()
    record_load.SupplierElem()
    record_load.ProductElem()
    record_load.GrossElem("2000")
    record_load.NetElem("1500")
    record_load.CompElem()
    record_load.NextElem()
    record_load.DelayYes()
    record_load.VerifyText()
    
    