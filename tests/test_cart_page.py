def test_empty_cart_title_and_text_is_correct(cart_page):
    cart_page.open_page()
    cart_page.is_cart_title_correct()
    cart_page.is_empty_cart_text_correct()


def test_product_added_to_cart_is_correct(cart_page, add_to_cart_pdp):
    cart_page.open_page()
    cart_page.is_cart_title_correct()
    cart_page.is_product_title_correct(add_to_cart_pdp.product_name)
    cart_page.is_product_price_correct(add_to_cart_pdp.product_price)
    cart_page.is_product_qty_correct(add_to_cart_pdp.product_qty)


def test_cart_checkout_button_redirects_to_checkout(cart_page, add_to_cart_pdp):
    cart_page.open_page()
    cart_page.is_checkout_button_clickable()
