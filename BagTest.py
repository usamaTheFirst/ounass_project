from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from BaseElement import BaseElement
from BasePage import BasePage
from locator import Locator
from selenium.webdriver.common.keys import Keys
import time

class BagTest(BasePage):
    url = "https://www.ounass.ae/shop-balenciaga-track-sneakers-in-mesh-nylon-for-men-214161242_245.html"

    @property
    def select_color(self):
        locator = Locator(By.CSS_SELECTOR, "button[title = 'Black']")
        return BaseElement(self.driver, locator=locator)


    def select_size(self):
        locator = Locator(By.CSS_SELECTOR, "span.Select-arrow-zone")
        element = BaseElement(self.driver, locator=locator)
        ActionChains(self.driver).move_to_element(element.web_element).click(element.web_element).send_keys(Keys.ENTER).perform()

    @property
    def add_to_bag(self):
        locator = Locator(By.CSS_SELECTOR, "button.AddToBag")
        return BaseElement(self.driver, locator=locator)

    @property
    def go_to_bag(self):
        locator = Locator(By.XPATH, "//div[text() = 'Bag']")
        return BaseElement(self.driver, locator=locator)

    @property
    def checkout(self):
        locator = Locator(By.CSS_SELECTOR, "button.CartTotal-secureCheckout")
        return BaseElement(self.driver, locator=locator)

    @property
    def enter_phone_number(self):
        locator = Locator(By.CSS_SELECTOR, "input#mobileNumber")
        return BaseElement(self.driver, locator=locator)

    def select_emirate(self):
        locator = Locator(By.CSS_SELECTOR, "#root > div > div.Base-content > div > div.Checkout-content > div.Delivery-signInAndShippingAddress > form > section.NewAddress > label:nth-child(5) > div > div > span")
        element = BaseElement(self.driver, locator=locator)
        ActionChains(self.driver).move_to_element(element.web_element).click(element.web_element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(10)


    def enter_area(self,area):
        locator = Locator(By.CSS_SELECTOR, "input[name = 'city']")
        element = BaseElement(self.driver, locator=locator)
        element.input_text(area)
        element.send_keys(Keys.TAB)

    @property
    def apartment(self):
        locator = Locator(By.CSS_SELECTOR, "input#additionalInformation")
        return BaseElement(self.driver, locator=locator)

    @property
    def enter_street(self):
        locator = Locator(By.CSS_SELECTOR, "input#street")
        return BaseElement(self.driver, locator=locator)

    @property
    def _continue(self):
        locator = Locator(By.CSS_SELECTOR, "button.ShippingInformationForm-submitButton")
        return BaseElement(self.driver, locator=locator)









