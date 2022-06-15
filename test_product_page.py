from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators, BasePageLocators
import pytest

url_pattern = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [f"{url_pattern}{x}" for x in range(10)] # Формирование ссылок для параметризации
links[7] = pytest.param(url_pattern + '7', marks=pytest.mark.xfail)  # Сразу отметитим непроходимый тест
link_for_tests = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.parametrize('link', links)
@pytest.mark.big
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link).open()

    page.add_to_cart()
    page.solve_quiz()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_for_tests).open()

    page.add_to_cart()
    assert not page.is_not_element_presented(*ProductPageLocators.ALERT_PRODUCT)


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_for_tests).open()

    assert page.is_not_element_presented(*ProductPageLocators.ALERT_PRODUCT)


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_for_tests).open()

    assert page.is_disappeared(*ProductPageLocators.ALERT_PRODUCT)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link).open()

    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link).open()

    page.is_element_present(*BasePageLocators.LOGIN_LINK)


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link).open()

    page.is_element_present(*BasePageLocators.BASKET)
    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.should_be_text_empty_basket()
