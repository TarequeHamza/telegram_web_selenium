import time

from Locators.locators import TelegramLocators
from Pages.HomePage import HomePage


class LoginPage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = TelegramLocators
        super(LoginPage, self).__init__(driver)

    def click_login(self):
        self.find_element(*self.locator.CLICK_LOGIN).click()
        time.sleep(5)

    def click_qr(self):
        self.find_element(*self.locator.CLICK_QR).click()
        time.sleep(5)

