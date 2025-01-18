
from page_object.base_page import Basepage
from selenium.webdriver.common.by import By


class LoginPageLocator:
    @staticmethod
    def get_xpath_locator(locator, **kwargs):
        login_page_locator = {
            "email_input": '//*[@id="username"]',
            'input_password': '//*[@id="password"]',
            'login_submit': '//*[@id="login-submit"]/span',
        }
        locator_str = login_page_locator[locator].format(**kwargs)
        return (By.XPATH, locator_str)


class LoginOperator(Basepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocator.get_xpath_locator

    def input_email_input(self, email):
        self.find_ele_after_visible(self.locator("email_input"), "email_input").send_keys(email)

    def input_password(self, password):
        self.find_ele_after_visible(self.locator("input_password"), "input_password").send_keys(password)

    def click_login_submit(self):
        self.find_ele_after_visible(self.locator("login_submit"), "login_submit").click()
