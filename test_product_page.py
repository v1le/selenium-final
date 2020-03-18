import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time

URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
URL_mod = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

@pytest.mark.skip
@pytest.mark.parametrize('offers', [f'?promo=offer{offer}' for offer in range(10) if offer != 7] + [
    pytest.param('?promo=newYear2019', marks=pytest.mark.skip),
    pytest.param('?promo=offer7', marks=pytest.mark.xfail)
])
def test_guest_can_add_product_to_basket(browser, offers):
    page = ProductPage(browser, URL+offers)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.are_prices_equal_on_success()
    page.are_names_equal_on_success()

@pytest.mark.skip
@pytest.mark.smoke
def test_guest_cant_see_after_adding_product_to_basket(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.add_to_basket()
    page.should_not_dissappear_success_alert()

def test_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()