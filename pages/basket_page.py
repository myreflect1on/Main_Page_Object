from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from selenium.webdriver.common.by import By



class BasketPage(BasePage):
    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        self.should_be_no_goods_in_basket()
        self.should_be_text_in_basket_that_basket_is_empty()


    def should_be_no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket do not empty"

    def should_be_text_in_basket_that_basket_is_empty(self):
        #BASKET_EMPTY в наличии
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "No element basket present"
        #корзина пустая
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        assert "Your basket is empty." in basket_message, "no text 'Your basket is empty'"