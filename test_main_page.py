from pages.main_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)  # инициализируем Page Object,
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы -
    # переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)  # инициализация перехода на другую
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # oткрываеm главную страницу
    # переходиь в корзину по кнопке в шапке сайта
    # в корзине нет товаров
    # есть текст о том что корзина пуста
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_no_goods_in_basket()
    page.should_be_text_in_basket_that_basket_is_empty()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)  # инициализируем Page Object,
        # передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы -
        # переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # инициализация перехода на другую
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()