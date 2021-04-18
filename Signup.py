from selenium.webdriver.common.by import By
from BaseElement import BaseElement
from BasePage import BasePage
from locator import Locator
class Signup(BasePage):
    url = 'https://www.ounass.ae/customer/register'

    @property
    def first_name(self):
        locator = Locator(By.CSS_SELECTOR,"input[name = 'firstName']")
        return BaseElement(self.driver, locator=locator)

    @property
    def last_name(self):
        locator = Locator(By.CSS_SELECTOR,"input[name = 'lastName']" )
        return BaseElement(self.driver, locator=locator)

    @property
    def email(self):
        locator = Locator(By.CSS_SELECTOR, "input[name = 'email']")
        return BaseElement(self.driver, locator=locator)

    @property
    def password(self):
        locator = Locator(By.CSS_SELECTOR, "input[name = 'password']")
        return BaseElement(self.driver, locator=locator)

    @property
    def create_account(self):
        locator = Locator(By.CSS_SELECTOR, "button[type = 'submit']")
        return BaseElement(self.driver, locator=locator)


