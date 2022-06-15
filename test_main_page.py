from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import BasePageLocators
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link).open()

    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
        Гость открывает главную страницу, переходит в корзину по кнопке в шапке сайта.
        Ожидаем, что в корзине нет товаров.
        Ожидаем, что есть текст о том что корзина пуста.
    """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link).open()

    page.is_element_present(*BasePageLocators.BASKET)
    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.should_be_text_empty_basket()
