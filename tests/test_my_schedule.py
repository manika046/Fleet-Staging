from tests.test_dashboard import *
from pages.my_schedule import MySchedule


class TestMySchedule(TestDashBoard):
  
  def test_schedule(self, driver_setup):
    TestDashBoard.test_dashboard(self, driver_setup)
    
    schedule = MySchedule(driver_setup)
    
    schedule.Schedule()
    schedule.TextElement()
    
    