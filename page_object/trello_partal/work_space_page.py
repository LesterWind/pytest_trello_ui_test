
from page_object.base_page import Basepage
from selenium.webdriver.common.by import By


class WorkSpaceLocator:
    @staticmethod
    def get_xpath_locator(locator, **kwargs):
        work_space_locator = {
            'create_board_button': '//button[contains(@data-testid,"create-board-tile")]',
            'input_board_title': '//input[contains(@data-testid,"create-board-title-input")]',
            'create_board_submit': '//button[contains(@data-testid,"create-board-submit-button")]',
        }
        locator_str = work_space_locator[locator].format(**kwargs)
        return (By.XPATH, locator_str)


class WorkSpacePageOperator(Basepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = WorkSpaceLocator.get_xpath_locator

    def click_create_board_button(self):
        self.find_ele_after_clickable(self.locator("create_board_button"), "create_board_button").click()

    def input_board_title(self, board_name):
        self.find_ele_after_visible(self.locator("input_board_title"), "input_board_title").send_keys(board_name)

    def click_create_board_submit(self):
        self.find_ele_after_clickable(self.locator("create_board_submit"), "create_board_submit").click()
