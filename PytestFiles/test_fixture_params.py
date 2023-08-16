from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if request.param=="chrome":
        web_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        request.cls.driver=web_driver
        yield
        web_driver.close()


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("https://iml.staging.apbexcise.in/login")
        assert self.driver.title=="AP P&E TNT"


