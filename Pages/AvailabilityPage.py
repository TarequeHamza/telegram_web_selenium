import time
from Locators.locators import TelegramLocators
from Pages.HomePage import HomePage


class AvailabilityPage(HomePage):

    def __init__(self, driver: object) -> object:
        self.locator = TelegramLocators
        self.driver = driver
        super(AvailabilityPage, self).__init__(driver)

    def is_avilable(self):
        return self.find_element(*self.locator.CLICK_ADD).is_displayed()

    def click_not_available(self):
        self.find_element(*self.locator.Not_AVILABLE).click()

    def click_search(self):
        self.find_element(*self.locator.CLICK_SEARCH).click()
        time.sleep(5)

    def set_searchs(self, name):
        self.find_element(*self.locator.SEARCHS_BOX).send_keys(name)
        time.sleep(5)

    def click_profiles(self):
        self.find_element(*self.locator.CLICK_PROFILES).click()
        time.sleep(5)

    def set_message(self, message):
        self.find_element(*self.locator.MASSAGE_BOX).send_keys(message)
        time.sleep(5)

    def click_send(self):
        self.find_element(*self.locator.SEND_BUTTON).click()
        time.sleep(5)

    def click_button(self):
        self.find_element(*self.locator.CLICK_BUTTON).click()
        time.sleep(5)

    def click_contact(self):
        self.find_element(*self.locator.CLICK_CONTACT).click()
        time.sleep(5)
