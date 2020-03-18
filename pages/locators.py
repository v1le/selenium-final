from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default[href$='/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_INPUT_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_ADDED_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    ITEM_ADDED_SUCCESS_ALERT_ITEM = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ITEM_ADDED_SUCCESS_ALERT_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")

class BasketPageLocators():
    TITLE = (By.CSS_SELECTOR, ".action h1")
    EMPTY_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p')
    BASKET_ITEMS_FORM = (By.CSS_SELECTOR, ".basket_summary")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a[href$='/checkout']")