import pytest
from page_services.board.board import BoardService
from page_services.login.login import LoginService


@pytest.fixture(scope="session", autouse=True)
def delete_board_setup(create_driver, setup_account_config):
    email = setup_account_config.get("account_common", "email")
    password = setup_account_config.get("account_common", "password")
    login_service = LoginService(create_driver)
    login_service.login(email, password)
    return create_driver
