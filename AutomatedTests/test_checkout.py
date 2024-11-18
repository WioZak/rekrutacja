from playwright.sync_api import Page, expect
from pageObjects.LoginPage import LoginPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ProductPage import ProductPage
import locale
import pytest
import re



@pytest.mark.parametrize("locale_code", ['en_GB', 'es_ES'])
def test_successfully_order_one_product(page: Page, locale_code):
    page.goto("")
    locale.setlocale(locale.LC_ALL , locale_code)
    login_page = LoginPage(page)
    checkout_page = CheckoutPage(page)
    product_page = ProductPage(page)

    login_page.login(login_page.standard_username, login_page.standard_password)
    product_page.first_product_btn.click()

    # Assert that the cart counter has changed
    expect(product_page.counter_1).to_be_visible()

    product_page.counter_1.click()
    checkout_page.checkout_btn.click()
    checkout_page.fill_the_form("abc", "def", "123")
    checkout_page.continue_btn.click()
    checkout_page.finish_btn.click()

    # Check translation
    expect(checkout_page.finish_title).to_contain_text(checkout_page.translations[locale_code]['finish_title'])
    expect(checkout_page.thank_you_header).to_contain_text(checkout_page.translations[locale_code]['thank_you_header'])


def test_add_one_product_and_cancel_in_overview(page: Page):
    page.goto("")
    login_page = LoginPage(page)
    checkout_page = CheckoutPage(page)
    product_page = ProductPage(page)

    login_page.login(login_page.standard_username, login_page.standard_password)
    product_page.first_product_btn.click()

    product_page.counter_1.click()
    checkout_page.checkout_btn.click()
    checkout_page.fill_the_form("abc", "def", "123")
    checkout_page.continue_btn.click()
    checkout_page.overview_cancel_btn.click()

    expect(page).to_have_url(re.compile(".*inventory"))


@pytest.mark.parametrize("locale_code", ['en_GB', 'es_ES'])
def test_checkout_form_missing_first_name(page: Page, locale_code):
    page.goto("")
    locale.setlocale(locale.LC_ALL , locale_code)
    login_page = LoginPage(page)
    checkout_page = CheckoutPage(page)
    product_page = ProductPage(page)

    login_page.login(login_page.standard_username, login_page.standard_password)
    product_page.first_product_btn.click()

    product_page.counter_1.click()
    checkout_page.checkout_btn.click()
    checkout_page.fill_the_form("", "def", "123")
    checkout_page.continue_btn.click()

    # Check translation of an error message
    expect(checkout_page.form_error).to_contain_text(checkout_page.translations[locale_code]['first_name_required'])

@pytest.mark.parametrize("locale_code", ['en_GB', 'es_ES'])
def test_checkout_form_missing_last_name(page: Page, locale_code):
    page.goto("")
    locale.setlocale(locale.LC_ALL , locale_code)
    login_page = LoginPage(page)
    checkout_page = CheckoutPage(page)
    product_page = ProductPage(page)

    login_page.login(login_page.standard_username, login_page.standard_password)
    product_page.first_product_btn.click()

    product_page.counter_1.click()
    checkout_page.checkout_btn.click()
    checkout_page.fill_the_form("abc", "", "123")
    checkout_page.continue_btn.click()

    # Check translation of an error message
    expect(checkout_page.form_error).to_contain_text(checkout_page.translations[locale_code]['last_name_required'])

@pytest.mark.parametrize("locale_code", ['en_GB', 'es_ES'])
def test_checkout_form_missing_postal_code(page: Page, locale_code):
    page.goto("")
    locale.setlocale(locale.LC_ALL , locale_code)
    login_page = LoginPage(page)
    checkout_page = CheckoutPage(page)
    product_page = ProductPage(page)

    login_page.login(login_page.standard_username, login_page.standard_password)
    product_page.first_product_btn.click()

    product_page.counter_1.click()
    checkout_page.checkout_btn.click()
    checkout_page.fill_the_form("abc", "def", "")
    checkout_page.continue_btn.click()

    # Check translation of an error message
    expect(checkout_page.form_error).to_contain_text(checkout_page.translations[locale_code]['postal_code_required'])
