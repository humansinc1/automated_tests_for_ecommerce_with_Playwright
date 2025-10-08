from playwright.sync_api import Page, Locator, expect
from pages.locators import header_locators
import allure


class BasePage:
    base_url = 'http://testshop.qa-practice.com/shop'
    page_url = None

    def __init__(self, page: Page):
        self.page = page
    @allure.step('Opening page')
    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened')

    @allure.step('Finding locator')
    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    @allure.step('Checking if product was added to cart')
    def was_product_added_to_the_cart(self):
        expect(self.find(header_locators.cart_qty_badge).nth(0)).to_have_text('1')
