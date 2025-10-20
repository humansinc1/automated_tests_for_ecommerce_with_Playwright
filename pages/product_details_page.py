from pages.base_page import BasePage
from pages.locators import product_details_page_locators, header_locators
from pages import urls
from playwright.sync_api import expect
import allure


class ProductDetailsPage(BasePage):
    page_url = urls.product_pdp_link2
    product_name = None
    product_price = None
    product_qty = None

    @allure.step('Adding product to cart')
    def add_product_to_cart(self):
        self.product_name = self.find(product_details_page_locators.product_name).text_content()
        self.product_price = self.find(product_details_page_locators.product_price).text_content()
        self.product_qty = self.find(product_details_page_locators.product_qty).get_attribute('value')
        add_to_cart_button = self.find(product_details_page_locators.add_to_cart_button)
        add_to_cart_button.click()
        expect(self.find(header_locators.cart_qty_badge).nth(0)).to_have_text('1')

    @allure.step('Checking if add to cart button color is correct')
    def is_add_to_cart_button_color_correct(self):
        add_to_cart_button = self.find(product_details_page_locators.add_to_cart_button)
        expect(add_to_cart_button).to_have_css('background-color', 'rgb(17, 100, 102)')

    @allure.step('Checking if add to cart button color is correct on hover')
    def is_add_to_cart_button_hover_color_correct(self):
        add_to_cart_button = self.find(product_details_page_locators.add_to_cart_button)
        add_to_cart_button.hover()
        expect(add_to_cart_button).to_have_css('background-color', 'rgb(14, 85, 87)')

    @allure.step('Checking if breadcrumbs are clickable')
    def are_breadcrumbs_clickable(self):
        breadcrumb_1 = self.find(product_details_page_locators.breadcrumb_1)
        breadcrumb_1.click()
        expect(self.find(product_details_page_locators.page_body)).to_be_visible()
        print(self.page.url)
        self.page.wait_for_url('http://testshop.qa-practice.com/shop/category/multimedia-9')
        self.page.go_back()
        breadcrumb_2 = self.find(product_details_page_locators.breadcrumb_2)
        breadcrumb_2.click()
        self.page.wait_for_url('http://testshop.qa-practice.com/shop')
