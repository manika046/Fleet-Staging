from tests.test_dashboard import *
from pages.schedule_load_order import ScheduleLoad


class TestScheduleLoadOrder(TestDashBoard):
  
  def test_schedule_load_order(self, driver_setup):
    TestDashBoard.test_dashboard(self, driver_setup)
    
    schedule_load = ScheduleLoad(driver_setup)
    
    schedule_load.ScheduleOrder()
    schedule_load.SelectTerminal()
    schedule_load.DateElem()
    schedule_load.TimeElem()
    schedule_load.Product()
    schedule_load.GrossElem("20")
    schedule_load.SupplierElem()
    schedule_load.CarrierElem()
    schedule_load.Submit()