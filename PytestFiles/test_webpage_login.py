from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_google():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.implicitily_wait(10)
    driver.get("https://www.google.com")
    #assert driver.title=="google"
    driver.quit()
def test_facebook():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.implicitily_wait(10)
    driver.get("https://www.facebook.com")
    #assert driver.title=="Facebook - log in or sign up"
    driver.quit()
def test_insta():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.implicitily_wait(10)
    driver.get("https://www.instagram.com")
    #assert driver.title=="instagram"
    driver.quit()
def test_whatsapp():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.implicitily_wait(10)
    driver.get("https://web.whatsapp.com")
    #assert driver.title=="whatsapp"
    driver.quit()