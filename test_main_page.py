from pages.main_page import MainPage
import time


URL = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, URL)
    main_page.open()
    main_page.go_to_login_page()
