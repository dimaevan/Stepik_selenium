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

    def test_added_product_in_bucket(self):
        product_in_bucket = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT)
        product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        assert product.text == product_in_bucket.text
