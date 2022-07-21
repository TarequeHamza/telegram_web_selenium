import time

from Pages.SendmessagePage import SendmessagePage
from Pages.BasePage import BasePage


class SendmessageTest(BasePage):
    def test_Sendmassage_page(self):
        Sendmassagepage = SendmessagePage(self.driver)
        time.sleep(15)
        Sendmassagepage.click_login()
        Sendmassagepage.click_qr()
        time.sleep(10)
        Sendmassagepage.set_search("NAIMUL")
        Sendmassagepage.click_profile()
        Sendmassagepage.set_message("bilibiliakkha")
        Sendmassagepage.click_send()


