from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def get_price_from_success_alert(self):
        price = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_SUCCESS_ALERT_BASKET_TOTAL_PRICE)
        return price.text

    def get_item_name_from_success_alert(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_SUCCESS_ALERT_ITEM)
        return item_name.text
    
    def are_prices_equal_on_success(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.get_price_from_success_alert(), "prices are not equal"

    def are_names_equal_on_success(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text in self.get_item_name_from_success_alert(), "names are not equal"