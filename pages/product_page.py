from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD)
        button.click()

    def solve_quiz(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split()[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()

        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def no_alert_product_in_basket(self):
        assert self.is_not_element_presented(*ProductPageLocators.ALERT_PRODUCT), "Alert on page!"

    def alert_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT), 'No alert adding product'

    def alert_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_PRODUCT), 'Alert is not disappeared'
