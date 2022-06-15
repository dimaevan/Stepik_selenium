from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login url is not founded"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not founded"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not founded"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_INPUT), "Not found email input"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT_1), "Not found password1 input"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT_2), "Not found password2 input"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BTN), "Not found button submit input"

        email_input = self.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        password_input = self.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT_1)
        password_input_2 = self.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT_2)
        submit_btn = self.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BTN)

        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input_2.send_keys(password)

        submit_btn.click()
