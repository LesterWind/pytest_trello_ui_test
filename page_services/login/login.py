
from page_object.trello_partal.lobby_page import LobbyOperator
from page_object.trello_partal.login_page import LoginOperator


class LoginService:
    def __init__(self, driver):
        self.lobby_operator = LobbyOperator(driver)
        self.login_operator = LoginOperator(driver)

    def login(self, email, password):
        self.lobby_operator.click_login_button()
        self.login_operator.input_email_input(email)
        self.login_operator.click_login_submit()
        self.login_operator.input_password(password)
        self.login_operator.click_login_submit()
