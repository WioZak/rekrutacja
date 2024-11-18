class ProductPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.first_product_btn = page.locator("div:nth-child(1) > .pricebar > .btn_primary")
        self.counter_1 = page.get_by_role("link", name="1")
        