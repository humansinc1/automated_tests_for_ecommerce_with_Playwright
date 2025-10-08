from pages.base_page import BasePage
from pages.locators import product_listing_page_locators, header_locators
from playwright.sync_api import expect
import allure


class ProductListingPage(BasePage):
    page_url = '/category/desks-1'

    @allure.step('Adding product to cart from PLP')
    def add_product_to_the_cart_from_plp(self):
        product_card = self.find(product_listing_page_locators.product_card).first
        add_to_cart_icon = self.find(product_listing_page_locators.cart_icon).first
        product_card.hover()
        add_to_cart_icon.hover()
        add_to_cart_icon.click()

    @allure.step('Clicking continue shopping button in modal')
    def click_continue_shopping_in_modal(self):
        continue_shopping = self.find(product_listing_page_locators.continue_shopping_button)
        continue_shopping.click()

    @allure.step('Checking if popup is opened')
    def is_popup_opened(self):
        popup = self.find(product_listing_page_locators.modal_title)
        expect(popup).to_have_text('Add to cart')

    @allure.step('Checking if product is NOT added to cart')
    def is_product_not_added_to_cart(self):
        self.find(product_listing_page_locators.modal_close_button).click()
        expect(self.find(header_locators.cart_qty_badge).first).to_have_css('display', 'none')
