import time

from Pages.BasePage import BasePage
from Pages.SendmessageexcelPage import SendmessageexcelPage
from Pages.ContactSavePage import ContactSavePage
from Pages.AvailabilityPage import AvailabilityPage
from utils.ExcelHandling import *
import os.path


class SendmessageexcelTest(BasePage):
    def test_SendmessageexcelPage(self):
        send = SendmessageexcelPage(self.driver)
        save = ContactSavePage(self.driver)
        available = AvailabilityPage(self.driver)
        excel = os.path.abspath('..\TestData\Contract_Number_List.xlsx')
        firstName = open_and_read_excel_file(excel, "Sheet1", 1)
        number = open_and_read_excel_file(excel, "Sheet1", 1)
        time.sleep(5)
        send.click_login()
        time.sleep(5)
        send.click_qr()
        time.sleep(10)
        send.click_button()
        time.sleep(5)
        send.click_contact()
        time.sleep(5)

        for i in range(len(number)):
            save.click_create()
            time.sleep(5)
            save.set_fname(firstName[i])
            time.sleep(5)
            save.set_phone(number[i])
            time.sleep(5)
            save.click_add()
            time.sleep(5)

            try:
                if available.is_avilable():
                    writeData(excel, "Sheet1", i + 2, 2, "   0")
                    available.click_not_available()
                else:
                    writeData(excel, "Sheet1", i + 2, 2, "   1")
                    time.sleep(2)

            except:
                print("This is not available")

