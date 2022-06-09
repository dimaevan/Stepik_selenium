from .pages.product_page import ProductPage
import pytest

url_pattern = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [f"{url_pattern}{x}" for x in range(2)]
links[1] = pytest.param(url_pattern+'7', marks=pytest.mark.xfail)


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    page.test_guest_cant_see_success_message()
    page.add_to_cart()
    page.solve_quiz()
    page.test_added_product_in_bucket()
    page.test_message_disappeared_after_adding_product_to_basket()
