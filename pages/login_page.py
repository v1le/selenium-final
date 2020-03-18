from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.split("/")[-2] == 'login'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL_INPUT
        )
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_INPUT
        )
        reg_password.send_keys(password)
        reg_password_repeat = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_INPUT_REPEAT
        )
        reg_password_repeat.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
