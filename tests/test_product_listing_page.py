def test_add_product_to_cart(product_listing_page):
    product_listing_page.open_page()
    product_listing_page.add_product_to_the_cart_from_plp()
    product_listing_page.click_continue_shopping_in_modal()
    product_listing_page.was_product_added_to_the_cart()


def test_add_to_cart_popup(product_listing_page, add_to_cart_plp):
    product_listing_page.is_popup_opened()


def test_closing_popup_is_not_added_product_to_cart(product_listing_page, add_to_cart_plp):
    product_listing_page.is_product_not_added_to_cart()
