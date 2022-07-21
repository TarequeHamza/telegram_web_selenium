import time

from Pages.SendmessagePage import SendmessagePage
from Pages.BasePage import BasePage


class LoginTest(BasePage):
    def test_Login_page(self):
        Login = SendmessagePage(self.driver)
        time.sleep(15)
        Login.click_login()
        Login.click_qr()
        time.sleep(10)


