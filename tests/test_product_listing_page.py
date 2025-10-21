import pytest
import allure

@pytest.mark.smoke
@allure.suite('Smoke tests')
@allure.severity('Blocker')
@allure.title('Test Add product to Cart')
@allure.epic('User journey')
@allure.feature('Add a product to cart')
@allure.story('Add a product to cart from PLP')
def test_add_product_to_cart(product_listing_page):
    product_listing_page.open_page()
    product_listing_page.add_product_to_the_cart_from_plp()
    product_listing_page.click_continue_shopping_in_modal()
    product_listing_page.was_product_added_to_the_cart()

@allure.title('Test Add to cart popup is appearing')
@allure.epic('User journey')
@allure.feature('Add a product to cart')
@allure.story('Add to cart popup is appearing on PLP')
def test_add_to_cart_popup(product_listing_page, add_to_cart_plp):
    product_listing_page.is_popup_opened()

@allure.title('Test product is not added to cart if popup closed')
@allure.epic('User journey')
@allure.feature('Add a product to cart')
@allure.story('Product is not added to cart on PLP if popup is closed')
def test_closing_popup_is_not_added_product_to_cart(product_listing_page, add_to_cart_plp):
    product_listing_page.is_product_not_added_to_cart()
