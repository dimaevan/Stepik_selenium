from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url: str):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(5)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_presented(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_basket_page(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET)
        basket.click()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, "It`s not basket page"

    def basket_should_be_empty(self):
        assert self.is_not_element_presented(*BasePageLocators.BASKET_ITEMS)

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.TEXT_EMPTY_BASKET)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def open(self):
        self.browser.get(self.url)

    def find_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return None
        return element

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
