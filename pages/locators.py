from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SUBMIT_BUTTON = (By.NAME, "login_submit")
    BASKET = (By.XPATH, '//a[contains(@href,"basket")]')
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, 'div#content_inner p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_INPUT = (By.NAME, 'registration-email')
    REGISTRATION_PASSWORD_INPUT_1 = (By.NAME, 'registration-password1')
    REGISTRATION_PASSWORD_INPUT_2 = (By.NAME, 'registration-password2')
    REGISTRATION_SUBMIT_BTN = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_TO_CARD = (By.CLASS_NAME, "btn-add-to-basket")
    ALERT_PRODUCT = (By.CSS_SELECTOR, 'div#messages div.alert:nth-child(1) strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div.product_main h1:nth-child(1)')
