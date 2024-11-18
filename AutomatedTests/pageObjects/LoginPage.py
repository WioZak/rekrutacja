class LoginPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.user_name = page.locator("[data-test=\"username\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.login_btn = page.locator("#login-button")
        self.error_incorrect_credentials = page.locator("[data-test=\"error\"]")
        self.homepage_title = page.locator(("[class=\"product_label\"]"))

        # Credentials
        self.standard_username = "standard_user"
        self.standard_password = "secret_sauce"
        self.incorrect_password = "aaovnajovndn"

        # Dictionary to hold text based on selected locale
        self.translations = {
        'en_GB': {
            'error_message': 'Epic sadface: Username and password do not match any user in this service',
            'homepage_title': 'Products',
        },
        'es_ES': {
            'error_message': 'Epic sadface: El nombre de usuario y la contraseña no coinciden con ningún usuario en este servicio',
            'homepage_title': 'Productos',
        }
        }

    def login(self, username, password):
        self.user_name.fill(username)
        self.password.fill(password)
        self.login_btn.click()