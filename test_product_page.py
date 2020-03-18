import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from helpers import generate_email_and_password

BASE_URL = "http://selenium1py.pythonanywhere.com/"
PRODUCT_URL = "catalogue/coders-at-work_207"
NEW_PRODUCT_URL = "catalogue/the-city-and-the-stars_95"
LOGIN_PAGE_URL = "accounts/login"


@pytest.mark.smoke
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, BASE_URL + LOGIN_PAGE_URL)
        page.open()
        page.should_be_login_page()
        page.register_new_user(*generate_email_and_password())
        page.should_be_authorized_user()
        yield

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, BASE_URL + PRODUCT_URL)
        page.open()
        page.add_to_basket()
        page.are_prices_equal_on_success()
        page.are_names_equal_on_success()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, BASE_URL + PRODUCT_URL)
        page.open()
        page.should_not_be_success_message()


'''
    creating list of parameters for test using list comprehension
    promo with offer7 excluded from test cause of bug
'''
@pytest.mark.need_review
@pytest.mark.parametrize(
    'offers',
    [f'?promo=offer{offer}' for offer in range(10) if offer != 7] +
    [
        pytest.param('?promo=offer7', marks=pytest.mark.xfail(reason='Bug'))
    ]
)
def test_guest_can_add_product_to_basket(browser, offers):
    page = ProductPage(browser, BASE_URL + PRODUCT_URL + offers)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.are_prices_equal_on_success()
    page.are_names_equal_on_success()


@pytest.mark.xfail(
    reason="negative case. Actually success message should appear"
)
def test_guest_cant_see_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BASE_URL + PRODUCT_URL)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, BASE_URL + PRODUCT_URL)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="negative case. Actually should not disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BASE_URL + PRODUCT_URL)
    page.open()
    page.add_to_basket()
    page.should_not_dissappear_success_alert()


def test_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, BASE_URL + PRODUCT_URL)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, BASE_URL + PRODUCT_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, BASE_URL + PRODUCT_URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()
