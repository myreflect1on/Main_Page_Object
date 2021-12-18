from .base_page import BasePage
from .locators import ProductPageLocator
import math
from selenium.common.exceptions import NoAlertPresentException
import time

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_product_key()
        self.should_be_add_product_key_click()
        self.should_be_message_about_adding()
        self.should_be_message_basket_total()


    def should_be_add_product_key(self):
        assert self.is_element_present(*ProductPageLocator.ADD_SUBMITT_BUTTON), "ADD_SUBMITT_BUTTON is not present"

    def should_be_add_product_key_click(self):
        link = self.browser.find_element(*ProductPageLocator.ADD_SUBMITT_BUTTON)
        link.click()
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(5)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_message_about_adding(self):
        #Элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocator.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocator.MESSAGE_ABOUT_ADD), "Message add is not presented"
        #Сверяем названия
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocator.MESSAGE_ABOUT_ADD).text
        assert product_name == message, f"{product_name} in the message"

    def should_be_message_basket_total(self):
        #Элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocator.MESSAGE_BASKET_TOTAL), "Message basket total is not presented"
        assert self.is_element_present(*ProductPageLocator.PRODUCT_PRICE), "Product price is not presented"
        #Сверяем названия
        message_basket_total = self.browser.find_element(*ProductPageLocator.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE).text
        # Присутствует стоимостью корзины
        assert product_price in message_basket_total, "No summ product in basket"
        time.sleep(5)