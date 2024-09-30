from tests.test_login import *
from pages.dashboard import DashBoard


class TestDashBoard(TestLogin):
  def test_dashboard(self, driver_setup):
    TestLogin.test_valid_login(self, driver_setup)
    
    dashboard = DashBoard(driver_setup)
    dashboard.AllowElem()
    dashboard.LocationText()
    dashboard.LocationDeny()
    dashboard.MenuBar()