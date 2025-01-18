import pytest
from common.common_utils import CommonUtils
from page_services.base_service import BaseService


@pytest.fixture(scope="session")
def set_common_utils():
    return CommonUtils()


@pytest.fixture(scope='session', autouse=True)
def setup_account_config(set_common_utils):
    return set_common_utils.get_account()


@pytest.fixture(scope='session', autouse=True)
def setup_domain_config(set_common_utils):
    return set_common_utils.get_domain()


@pytest.fixture(scope="session")
def create_driver(setup_domain_config):
    driver = BaseService.create_driver()
    BaseService.visit_domain(create_driver, setup_domain_config.get("trello_url", "trello_url"))
    yield driver
    driver.quit()
