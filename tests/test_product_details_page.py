def test_add_product_to_cart(product_details_page):
    product_details_page.open_page()
    product_details_page.add_product_to_cart()
    product_details_page.was_product_added_to_the_cart()


def test_add_to_cart_button_has_correct_color(product_details_page):
    product_details_page.open_page()
    product_details_page.is_add_to_cart_button_color_correct()
    product_details_page.is_add_to_cart_button_hover_color_correct()


def test_breadcrumbs_are_clickable(product_details_page):
    product_details_page.open_page()
    product_details_page.are_breadcrumbs_clickable()
