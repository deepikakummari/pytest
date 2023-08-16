from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
driver=None

def setup_module(module):
    global driver
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.implicitily_wait(10)
    driver.delete_all_cookies()
    driver.get("https://iml.staging.apbexcise.in/login")
def teardown_module(module):
    driver.quit()
def test_apttitlename():
    get_title = driver.title
    print(get_title)

def test_google_title():
    assert driver.title=="AP P&E TNT"

def test_google_currenturl():
    assert driver.current_url=="https://iml.staging.apbexcise.in/login"



