
from page_object.trello_partal.component.header import HeaderLocatorOperator


class BoardService:
    def __init__(self, driver):
        self.header = HeaderLocatorOperator(driver)
        self.work_space = None

    def join_work_space(self, workspace_name):
        self.header.click_workspace_switcher()
        self.work_space = self.header.click_into_workspace(workspace_name)

    def create_board(self, board_name):
        self.work_space.click_create_board_button()
        self.work_space.input_board_title(board_name)
        self.work_space.click_create_board_submit()
