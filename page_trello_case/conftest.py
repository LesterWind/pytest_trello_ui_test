import pytest
from selenium import webdriver
from page_services.page_service import Service

@pytest.fixture(scope="session")
def setup_browser():
        
    driver = webdriver.Firefox()
    A = Service(driver)
    A.login("https://trello.com/login", "lesterjack93@yahoo.com.tw", "trello0968141018")
    A.into_workspace()

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def setup_board(setup_browser):
        
    A = Service(setup_browser)
    A.create_board("測試用看板1")
    A.wait_element_loading('create_list_button')
    A.into_workspace()

    yield setup_browser

@pytest.fixture(scope="function")
def setup_list(setup_browser):
        
    A = Service(setup_browser)
    A.into_board("測試用看板2")
    A.create_list("測試用列表")
    
    yield setup_browser

    A.into_workspace()