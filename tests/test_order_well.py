from tests.test_dashboard import *
from pages.order_well import OrderWell


class TestOrderWell(TestDashBoard):
  
  def test_order(self, driver_setup):
    TestDashBoard.test_dashboard(self, driver_setup)
    
    order = OrderWell(driver_setup)
    
    order.Order()
    order.VerifyText()
    
    