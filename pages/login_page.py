from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Is not Login link"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "email input is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "password input is not present"
        # assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BUTTON), "login submit button is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "reg email input is not present"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_1), "reg password1 is not present"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_2), "reg password2 is not present"
        assert self.is_element_present(*LoginPageLocators.REG_SUBMIT_BUTTON), "reg submit button is not present"
