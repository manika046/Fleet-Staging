from tests.test_dashboard import *
from pages.schedule_delivery_order import ScheduleDelivery


class TestScheduleDeliveryOrder(TestDashBoard):
  
  def test_schedule_delivery_order(self, driver_setup):
    TestDashBoard.test_dashboard(self, driver_setup)
    
    schedule_order = ScheduleDelivery(driver_setup)
    
    schedule_order.ScheduleDelivery()
    schedule_order.SelectCustomer()
    schedule_order.DateElem()
    schedule_order.TimeElem()
    schedule_order.CustomerSite()
    schedule_order.CreateOrder()