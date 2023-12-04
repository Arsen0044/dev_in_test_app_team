from framework.locators.buttons import ButtonLocators
from framework.locators.other import OtherLocators
from framework.locators.xpath import XpathLocators


class Locators(ButtonLocators, XpathLocators, OtherLocators):

    def locator_container(self):
        pass
