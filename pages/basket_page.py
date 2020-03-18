from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_title()

    def should_be_basket_url(self):
        assert  self.browser.current_url.split("/")[-2] == 'basket', "not basket page"
    
    def should_be_basket_title(self):
        assert  self.is_element_present(*BasketPageLocators.TITLE), "not basket title"

    def should_be_empty_basket(self):
        self.should_be_empty_title()
        self.should_not_contain_items_in_basket()
        self.should_not_contain_checkout_button()

    def should_be_empty_title(self):
        template = "Continue shopping"
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "No empty message"
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE)
        assert  empty_message.text == f"Your basket is empty. {template}", f"Empty message broken, actual {empty_message.text}"

    def should_not_contain_items_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS_FORM), "Form with items on basket on empty basket detected"

    def should_not_contain_checkout_button(self):
        assert not self.is_element_present(*BasketPageLocators.CHECKOUT_BUTTON), "Empty basket contains checkout button"