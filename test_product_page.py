from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import time

url_pattern = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [f"{url_pattern}{x}" for x in range(10)]  # Формирование ссылок для параметризации
links[7] = pytest.param(url_pattern + '7', marks=pytest.mark.xfail)  # Сразу отметитим непроходимый тест
link_for_tests = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.parametrize('link', links)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz()


@pytest.mark.xfail(reason="need 2 fix this bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_for_tests)
    page.open()

    page.add_to_cart()
    page.no_alert_product_in_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_for_tests)
    page.open()
    page.no_alert_product_in_basket()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_for_tests)
    page.open()
    page.alert_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_for_tests)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_for_tests)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_for_tests)
    page.open()

    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.should_be_text_empty_basket()


@pytest.mark.new
class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, self.link)
        page.open()
        page.go_to_login_page()

        rand = str(time.time())

        page.register_new_user(rand + "@fakemail.org", rand)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.no_alert_product_in_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_to_cart()
        page.alert_product_in_basket()
