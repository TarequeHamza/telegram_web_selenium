from selenium.webdriver.common.by import By


class TelegramLocators(object):
    #send messagelocators:
    CLICK_LOGIN = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/button/div")
    CLICK_QR = (By.XPATH, "// *[ @ id = 'auth-pages'] / div / div[2] / div[1] / div / div[3] / button[2] / div")
    CLICK_SEARCH = (By.XPATH, "//*[@id='contacts-container']/div[1]/div/input")
    SEARCHS_BOX = (By.XPATH, "//*[@id='contacts-container']/div[1]/div/input")
    SEARCH_BOX = (By.XPATH, "//*[@id='column-left']/div/div/div[1]/div[2]/input")
    CLICK_PROFILE = (By.XPATH, "// *[ @ id = 'search-container'] / div[2] / div / div / div[1] / div / div[1] / ul / li / div[1]")
    CLICK_PROFILES = (By.XPATH, "// *[ @ id = 'contacts'] / li / div[1]")
    MASSAGE_BOX= (By.XPATH, "// *[ @ id = 'column-center'] / div / div / div[4] / div / div[1] / div / div[8] / div[1] / div[1]")
    SEND_BUTTON = (By.XPATH, "// *[ @ id = 'column-center'] / div / div / div[4] / div / div[5] / button / div")

    #create account:
    CLICK_BUTTON = (By.XPATH, "// *[ @ id = 'column-left'] / div / div / div[1] / div[1] / div[2] / div[1]")
    CLICK_CONTACT = (By.XPATH, "//*[@id='column-left']/div/div/div[1]/div[1]/div[2]/div[3]/div[3]")
    CLICK_CREATE = (By.XPATH, "//*[@id='contacts-container']/div[2]/button/div")
    FNAME_BOX = (By.XPATH, "/html/body/div[5]/div/div[2]/div[1]/div[1]")
    PHONE_BOX = (By.XPATH, "/html/body/div[5]/div/div[3]/div[1]")
    CLICK_ADD = (By.XPATH, "/html/body/div[5]/div/div[1]/button/div")

    #avilable or not avilable:
    AVILABLE= (By.XPATH, "// *[ @ id = 'column-center'] / div / div / div / div / canvas[2]")
    Not_AVILABLE = (By.XPATH, "/html/body/div[5]/div/div[1]/span")
    #BACK_BUTTON = (By.XPATH, "/html/body/div[5]/div/div[1]/span")


class CategoryPageLocators(object):
    WATCH_BTN = (By.XPATH, "/html/body/div/section[2]/div/div/div/div/div[1]/div/ul/li[8]")
    TABLE_BTN = (By.XPATH, "//*[@id='menu']/ul/li[8]/ul/li[7]/a")


#//*[@id="column-left"]/div/div/div[1]/div[2]/input
#// *[ @ id = "search-container"] / div[2] / div / div / div[1] / div / div[1] / ul / li / div[1]
#// *[ @ id = 'column-center'] / div / div / div[4] / div / div[1] / div / div[8] / div[1] / div[1]")
#// *[ @ id = 'column-center'] / div / div / div[4] / div / div[5] / button / div
#")
