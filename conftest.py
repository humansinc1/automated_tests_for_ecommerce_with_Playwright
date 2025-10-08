import pytest

from playwright.sync_api import Browser
from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage
from pages.product_listing_page import ProductListingPage


@pytest.fixture()
def page(browser: Browser):
    context = browser.new_context(
        ignore_https_errors=True
    )
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    yield page
    context.close()


@pytest.fixture()
def cart_page(page):
    return CartPage(page)


@pytest.fixture()
def product_details_page(page):
    return ProductDetailsPage(page)


@pytest.fixture()
def product_listing_page(page):
    return ProductListingPage(page)


@pytest.fixture()
def add_to_cart_pdp(product_details_page):
    product_details_page.open_page()
    product_details_page.add_product_to_cart()
    return product_details_page


@pytest.fixture()
def add_to_cart_plp(product_listing_page):
    product_listing_page.open_page()
    product_listing_page.add_product_to_the_cart_from_plp()
    return product_listing_page
