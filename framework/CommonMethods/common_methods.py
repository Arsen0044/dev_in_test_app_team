import time
from data.data_container import DataContainer
from appium.webdriver.webdriver import AppiumBy
from framework.locators.locators import Locators


class CommonMethods:

    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators()
        self.data = DataContainer()

    def find_element_by_id(self, locator):
        element = self.driver.find_element(AppiumBy.ID, locator)
        return element

    def find_element_by_xpath(self, locator):
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        return element

    def click_element_by_id(self, id_):
        element = self.find_element_by_id(id_)
        element.click()

    def click_element_by_xpath(self, xpath):
        element = self.find_element_by_xpath(xpath)
        element.click()

    def input_by_xpath(self, xpath, value):
        element = self.find_element_by_xpath(xpath)
        element.clear()
        element.click()
        element.send_keys(value)

    @staticmethod
    def waiter(seconds):
        time.sleep(seconds)
