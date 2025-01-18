
from selenium.webdriver.common.by import By
from page_object.base_page import Basepage


class LobbyPageLocator:
    @staticmethod
    def get_xpath_locator(locator, **kwargs):
        trello_portal_lobby_page_locator = {
            "login_button": "//*[contains(@data-uuid,'MJFtCCgVhXrVl7v9HA7EH_login')]",
            }
        locator_str = trello_portal_lobby_page_locator[locator].format(**kwargs)
        return (By.XPATH, locator_str)


class LobbyOperator(Basepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LobbyPageLocator.get_xpath_locator

    def click_login_button(self):
        self.find_ele_after_visible(self.locator("login_button"), "login_button").click()
