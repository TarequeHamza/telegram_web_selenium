import time

from Locators.locators import TelegramLocators
from Pages.HomePage import HomePage


class SendmessagePage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = TelegramLocators
        super(SendmessagePage, self).__init__(driver)

    def click_login(self):
        self.find_element(*self.locator.CLICK_LOGIN).click()
        time.sleep(5)

    def click_qr(self):
        self.find_element(*self.locator.CLICK_QR).click()
        time.sleep(5)

    def set_search(self, name):
        self.find_element(*self.locator.SEARCH_BOX).send_keys(name)
        time.sleep(5)

    def click_profile(self):
        self.find_element(*self.locator.CLICK_PROFILE).click()
        time.sleep(5)

    def set_message(self, message):
        self.find_element(*self.locator.MASSAGE_BOX).send_keys(message)
        time.sleep(5)

    def click_send(self):
        self.find_element(*self.locator.SEND_BUTTON).click()
        time.sleep(5)