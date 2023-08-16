from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
driver=None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("--------------------setup-----------------------------------")
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.implicitily_wait(10)
    driver.delete_all_cookies()
    driver.get("https://iml.staging.apbexcise.in/login")
    yield
    print("------------------teardown--------------------------------")
    driver.quit()
@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title=="AP P&E TNT"

@pytest.mark.usefixtures("init_driver")
def test_google_currenturl():
    assert driver.current_url=="https://iml.staging.apbexcise.in/login"



