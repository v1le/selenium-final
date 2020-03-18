from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ), "No basket button"
        add_to_basket = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_to_basket.click()

    def get_price_from_success_alert(self):
        assert self.is_element_present(
            *ProductPageLocators.ITEM_ADDED_SUCCESS_ALERT_BASKET_TOTAL_PRICE
        ), "No price success alert after adding item"
        price = self.browser.find_element(
            *ProductPageLocators.ITEM_ADDED_SUCCESS_ALERT_BASKET_TOTAL_PRICE
        )
        return price.text

    def get_item_name_from_success_alert(self):
        assert self.is_element_present(
            *ProductPageLocators.ITEM_ADDED_SUCCESS_ALERT_BASKET_TOTAL_PRICE
        ), "No item name success alert after adding item"
        item_name = self.browser.find_element(
            *ProductPageLocators.ITEM_ADDED_SUCCESS_ALERT_ITEM
        )
        return item_name.text

    def are_prices_equal_on_success(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text == self.get_price_from_success_alert(), "prices aren't equal"

    def are_names_equal_on_success(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text == self.get_item_name_from_success_alert(), "names aren't equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ITEM_ADDED_SUCCESS_ALERT
        ), "Success message is presented, but should not be"

    def should_not_dissappear_success_alert(self):
        assert self.is_disappeared(
            *ProductPageLocators.ITEM_ADDED_SUCCESS_ALERT
        )
