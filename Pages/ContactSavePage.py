import time
from Locators.locators import TelegramLocators
from Pages.HomePage import HomePage

class ContactSavePage(HomePage):

    def __init__(self, driver: object) -> object:
        self.locator = TelegramLocators
        self.driver = driver
        super(ContactSavePage, self).__init__(driver)

    def click_login(self):
        self.find_element(*self.locator.CLICK_LOGIN).click()
        time.sleep(5)

    def click_qr(self):
        self.find_element(*self.locator.CLICK_QR).click()
        time.sleep(5)

    def click_button(self):
        self.find_element(*self.locator.CLICK_BUTTON).click()
        time.sleep(5)

    def click_contact(self):
        self.find_element(*self.locator.CLICK_CONTACT).click()
        time.sleep(5)


    def click_create(self):
        self.find_element(*self.locator.CLICK_CREATE).click()
        time.sleep(5)

    def set_fname(self, fname):
        self.find_element(*self.locator.FNAME_BOX).send_keys(fname)
        time.sleep(5)

    def set_phone(self, phone):
        self.find_element(*self.locator.PHONE_BOX).send_keys(phone)
        time.sleep(5)

    def click_add(self):
        self.find_element(*self.locator.CLICK_ADD).click()
        time.sleep(5)

    def click_back(self):
        self.find_element(*self.locator.BACK_BUTTON).click()
        time.sleep(5)
