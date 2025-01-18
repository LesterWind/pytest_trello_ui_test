
from selenium import webdriver


class BaseService:
    def __init__(self):
        pass

    @staticmethod
    def create_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver

    @staticmethod
    def visit_domain(driver, url):
        driver.get(url)
