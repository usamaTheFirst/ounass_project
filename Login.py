from selenium.webdriver.common.by import By
from BaseElement import BaseElement
from BasePage import BasePage
from locator import Locator
from selenium.webdriver.common.alert import Alert
import time
class Login(BasePage):
    url = "https://www.ounass.ae/"

    def __init__(self,driver):
        super().__init__(driver)
        self.go()

        locator = Locator(By.CSS_SELECTOR, "button#wzrk-cancel")
        button = BaseElement(self.driver, locator=locator)
        button.click_button()



        locator = Locator(By.CSS_SELECTOR, "button.Popup-button")
        button = BaseElement(self.driver, locator=locator)
        button.click_button()

    @property
    def email(self):
        locator = Locator(By.CSS_SELECTOR, "input.SignInForm-email")
        return BaseElement(self.driver, locator=locator)

    @property
    def password(self):
        locator = Locator(By.CSS_SELECTOR, "input[type = 'password']")
        return BaseElement(self.driver, locator=locator)

    @property
    def login_button(self):
        locator = Locator(By.CSS_SELECTOR, "button[type = 'submit']")
        return BaseElement(self.driver, locator=locator)

    @property
    def customer_setting(self):
        locator = Locator(By.CSS_SELECTOR, "a[href $= '/customer']")
        return BaseElement(self.driver, locator=locator)

    @property
    def edit(self):
        locator = Locator(By.XPATH, "//a[text() = 'Edit']")
        return BaseElement(self.driver, locator=locator)



    @property
    def email_verification(self):
        locator = Locator(By.CSS_SELECTOR, "input[type = 'email']")
        return BaseElement(self.driver, locator=locator)


    @property
    def update_number(self):
        pass








