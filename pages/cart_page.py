from pages.base_page import BasePage
from pages.locators import cart_page_locators
from playwright.sync_api import expect
import allure


class CartPage(BasePage):
    page_url = '/cart'

    @allure.step('Checking if cart page title is correct')
    def is_cart_title_correct(self):
        title = self.find(cart_page_locators.page_title)
        expect(title).to_have_text('Order overview')

    @allure.step('Checking if cart page text is correct')
    def is_empty_cart_text_correct(self):
        text = self.find(cart_page_locators.empty_cart_text)
        expect(text).to_have_text('Your cart is empty!')

    @allure.step('Checking if product title is correct')
    def is_product_title_correct(self, product_name):
        cart_product_title = self.find(cart_page_locators.product_title)
        expect(cart_product_title).to_contain_text(product_name)

    @allure.step('Checking if product price is correct')
    def is_product_price_correct(self, product_price):
        cart_product_price = self.find(cart_page_locators.product_price)
        expect(cart_product_price).to_have_text(product_price)

    @allure.step('Checking if product qty is correct')
    def is_product_qty_correct(self, product_qty):
        cart_product_qty = self.find(cart_page_locators.product_qty)
        expect(cart_product_qty).to_have_attribute('value', product_qty)

    @allure.step('Checking if checkout button is clickable')
    def is_checkout_button_clickable(self):
        checkout_button = self.find(cart_page_locators.checkout_button)
        checkout_button.click()
        checkout_title = self.find(cart_page_locators.checkout_title)
        expect(checkout_title).to_have_text('Fill in your address or Sign in')
