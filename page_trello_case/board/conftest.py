import pytest
from page_services.board.board import BoardService
from page_services.login.login import LoginService


@pytest.fixture(scope="session", autouse=True)
def board_account(visit_trello, setup_account_config):
    email = setup_account_config.get("account_common", "email")
    password = setup_account_config.get("account_common", "password")
    LoginService
    return email, password


@pytest.fixture(scope='session')
def board_service(create_driver):
    return BoardService(create_driver)
