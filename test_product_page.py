from pages.product_page import ProductPage

URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.are_prices_equal_on_success()
    page.are_names_equal_on_success()
