from tests.test_dashboard import *
from pages.record_fuel_transfer import RecordFuel


class TestRecordFuelTransfer(TestDashBoard):
  def test_fuel_transfer(self, driver_setup):
    TestDashBoard.test_dashboard(self, driver_setup)
    
    record_fuel = RecordFuel(driver_setup)
    
    record_fuel.TransferFuel()
    record_fuel.Date()
    record_fuel.OkButton()
    record_fuel.Time()
    record_fuel.FromElement()
    record_fuel.ToElement()
    record_fuel.Element()
    record_fuel.Product()
    record_fuel.Gallon("20")
    record_fuel.Note("Record Fuel Transfer")
    record_fuel.Submit()
    record_fuel.VerifyText()