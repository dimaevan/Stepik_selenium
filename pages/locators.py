from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SUBMIT_BUTTON = (By.NAME, "login_submit")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CARD = (By.CLASS_NAME, "btn-add-to-basket")
    ALERT_PRODUCT = (By.CSS_SELECTOR, 'div#messages div.alert:nth-child(1) strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div.product_main h1:nth-child(1)')
