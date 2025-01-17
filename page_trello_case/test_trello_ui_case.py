import pytest
from selenium import webdriver
from page_services.page_service import Service

def test_delete_board(setup_board):
    driver = setup_board
    A = Service(driver)
        # 如果看板不存在，跳過測試
    if not A.board_checking():
        pytest.skip("看板不存在，跳過此測試")
        
    A.delete_board("測試用看板1")

def test_delete_list(setup_list):
    driver = setup_list
    A = Service(driver)
    A.delete_list("測試用列表")

    







