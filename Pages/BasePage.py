import time
import unittest
from selenium import webdriver
from threading import Thread, Barrier

class BasePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://web.telegram.org/k/")
        print("Test Started")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        # cls.driver.quit()
        print("Test Complete")
