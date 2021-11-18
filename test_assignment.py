from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestSwagLabs(BaseTest):
    def test_title(self):
        self.driver.get("https://www.saucedemo.com/")
        assert self.driver.title == "Swag Labs"

    @pytest.mark.parametrize(
                                "username, password",
                                [
                                    ("admin@gmail.com", "admin123"),
                                    ("standard_user", "secret_sauce")
                                ]
                            )
    def test_login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        time.sleep(5)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="login-button"]').click()
        time.sleep(5)











