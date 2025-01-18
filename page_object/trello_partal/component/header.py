
from page_object.base_page import Basepage
from selenium.webdriver.common.by import By
from page_object.trello_partal.work_space_page import WorkSpacePageOperator


class HeaderLocator:
    @staticmethod
    def get_xpath_locator(locator, **kwargs):
        header_locator = {
            'workspace_switcher': '//*[contains(@data-testid,"workspace-switcher")]',
            'into_workspace': '//*[contains(@data-testid,"workspace-switcher-popover-tile")]//*[contains(normalize-space(),"{workspace_name}")]'
        }
        locator_str = header_locator[locator].format(**kwargs)
        return (By.XPATH, locator_str)


class HeaderLocatorOperator(Basepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = HeaderLocator.get_xpath_locator

    def click_workspace_switcher(self):
        self.find_ele_after_clickable(self.locator("workspace_switcher"), "workspace_switcher").click()

    def click_into_workspace(self, workspace_name):
        self.find_ele_after_clickable(self.locator("into_workspace", workspace_name=workspace_name), "into_workspace").click()
        return WorkSpacePageOperator(self.driver)
