import time
import os
import pytest
from pathlib import Path
from appium import webdriver
from appium.options.common.base import AppiumOptions
from dotenv import load_dotenv
from pages.login import LoginPage


@pytest.fixture(scope="class")
def driver_setup(request):
  # Appium driver setup
  options = AppiumOptions()
  options.load_capabilities({
    "platformName": "android",
    "appium:automationName": "uiautomator2",
    "appium:platformVersion": "15",
    "appium:deviceName": "Pixel 7a API 35",
    "appium:app": "C:\\Users\\acer\\Downloads\\app-staging-release.apk",
  })
  
  # Load environment variables
  dotenv_path = Path('../.venv/.env')
  load_dotenv(dotenv_path=dotenv_path)
  
  # Initialize Appium driver
  driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
  
  # Teardown after test completes
  def teardown():
    driver.quit()
  
  request.addfinalizer(teardown)
  
  return driver


@pytest.mark.usefixtures("driver_setup")
class TestLogin:
  
  def test_valid_login(self, driver_setup):
    # Use driver_setup fixture
    login = LoginPage(driver_setup)
    
    login.ImageElement()
    login.URLText()
    login.BaseUrl("test.fleetpanda.com")
    login.Submit()
    login.SignInButton()
    login.MobileText()
    login.InputElement(os.getenv("NUMBER"))
    login.ContinueButton()
    login.PasswordText()
    login.Password(os.getenv("PASSWORD"))
    login.LoginButton()
    login.VerifyText()
