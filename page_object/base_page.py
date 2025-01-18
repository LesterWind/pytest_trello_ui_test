from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CustomTimeoutException(Exception):

    def __init__(self, message):
        super().__init__(message)


class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def find_ele_after_visible(self, locator, element_name, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            if element:
                return element
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            if element:
                self.driver.execute_script('arguments[0].scrollIntoView({ block: "center", inline: "center" });',
                                           element)
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(locator))
                return element
        except TimeoutException:
            raise CustomTimeoutException(f"Element [{element_name}]was unvisiable within {timeout} seconds.")

    def find_ele_after_clickable(self, locator, element_name, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

            if element:
                return element
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

            if element:
                self.driver.execute_script('arguments[0].scrollIntoView({ block: "center", inline: "center" });',
                                           element)
                element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
                return element
        except TimeoutException:
            raise CustomTimeoutException(f"Element [{element_name}]was unclickable within {timeout} seconds.")

    def find_ele_after_presence(self, locator, element, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            if element:
                return element
        except TimeoutException:
            raise CustomTimeoutException(f"Element [{element}]was not presence within {timeout} seconds.")

