class CheckoutPage:
    def __init__(self, page):
        self.page = page
        #Locators
        self.first_name = page.locator("[data-test=\"firstName\"]")
        self.last_name = page.locator("[data-test=\"lastName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.checkout_btn = page.locator(("[class=\"btn_action checkout_button\"]"))
        self.continue_btn = page.locator(("[class=\"btn_primary cart_button\"]"))
        self.finish_btn = page.locator(("[class=\"btn_action cart_button\"]"))
        self.finish_title = page.locator(("#contents_wrapper > div.subheader"))
        self.thank_you_header = page.locator(("[class=\"complete-header\"]"))
        self.overview_cancel_btn = page.locator(("[class=\"cart_cancel_link btn_secondary\"]"))
        self.form_error = page.locator("[data-test=\"error\"]")

        # Dictionary to hold text based on selected locale
        self.translations = {
        'en_GB': {
            'finish_title': 'Finish',
            'thank_you_header': 'THANK YOU FOR YOUR ORDER',
            'first_name_required': 'Error: First Name is required',
            'last_name_required': 'Error: Last Name is required',
            'postal_code_required':'Error: Postal Code is required'
        },
        'es_ES': {
            'finish_title': 'Finito',
            'thank_you_header': 'GRACIAS POR SU PEDIDO',
            'first_name_required': 'Error: El nombre es obligatorio',
            'last_name_required': 'Error: El apellido es obligatorio',
            'postal_code_required':'Error: Se requiere código postal'
        }
        }


    def fill_the_form(self,firstname,lastname,postalcode):
        self.first_name.fill(firstname)
        self.last_name.fill(lastname)
        self.postal_code.fill(postalcode)