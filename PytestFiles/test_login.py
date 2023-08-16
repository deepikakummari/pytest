import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
class Apt(BaseTest):
    @pytest.mark.parametrize("username,password",[("mm_section","password")])
    def test_first(self,username,password):
        self.driver.get("https://iml.staging.apbexcise.in/login")
        self.driver.find_element(By.ID,"mat-input-0").send_keys(username)
        self.driver.find_element(By.ID,"mat-input-3").send_keys(password)

