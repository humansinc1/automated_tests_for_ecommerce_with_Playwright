import pytest
import allure


@allure.title('Test Empty Cart has correct text')
@allure.epic('User journey')
@allure.feature('Cart page')
@allure.story('Empty Cart has correct text')
def test_empty_cart_title_and_text_is_correct(cart_page):
    cart_page.open_page()
    cart_page.is_cart_title_correct()
    cart_page.is_empty_cart_text_correct()


@pytest.mark.smoke
@allure.suite('Smoke tests')
@allure.severity('Blocker')
@allure.title('Test Added product correctly displayed in Cart')
@allure.epic('User journey')
@allure.feature('Cart page')
@allure.story('Added product is correctly displayed in cart')
def test_product_added_to_cart_is_correct(cart_page, add_to_cart_pdp):
    cart_page.open_page()
    cart_page.is_cart_title_correct()
    cart_page.is_product_title_correct(add_to_cart_pdp.product_name)
    cart_page.is_product_price_correct(add_to_cart_pdp.product_price)
    cart_page.is_product_qty_correct(add_to_cart_pdp.product_qty)


@pytest.mark.smoke
@allure.suite('Smoke tests')
@allure.severity('Blocker')
@allure.title('Test Checkout button redirects to Checkout page')
@allure.epic('User journey')
@allure.feature('Checkout')
@allure.story('Clicking Checkout button in the cart redirects a user to Checkout page')
def test_cart_checkout_button_redirects_to_checkout(cart_page, add_to_cart_pdp):
    cart_page.open_page()
    cart_page.is_checkout_button_clickable()
