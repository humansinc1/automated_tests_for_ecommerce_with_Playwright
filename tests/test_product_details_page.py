import allure
import pytest


@pytest.mark.smoke
@allure.suite('Smoke tests')
@allure.severity('Blocker')
@allure.title('Test Add product to Cart from PDP')
@allure.epic('User journey')
@allure.feature('Add a product to cart')
@allure.story('Add a product to cart from PDP')
def test_add_product_to_cart(product_details_page):
    product_details_page.open_page()
    product_details_page.add_product_to_cart()
    product_details_page.was_product_added_to_the_cart()

@allure.title('Test Add to cart button has correct color')
@allure.epic('UI')
@allure.feature('Cart')
@allure.story('Add to cart button has correct color')
def test_add_to_cart_button_has_correct_color(product_details_page):
    product_details_page.open_page()
    product_details_page.is_add_to_cart_button_color_correct()
    product_details_page.is_add_to_cart_button_hover_color_correct()

@allure.title('Test Navigating through breadcrumbs')
@allure.epic('User journey')
@allure.feature('Navigation')
@allure.story('Navigate through breadcrumbs')
def test_breadcrumbs_are_clickable(product_details_page):
    product_details_page.open_page()
    product_details_page.are_breadcrumbs_clickable()
