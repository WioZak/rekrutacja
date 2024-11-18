from playwright.sync_api import Page, expect
from pageObjects.LoginPage import LoginPage
import locale
import pytest


@pytest.mark.parametrize("locale_code", ['en_GB', 'es_ES'])
def test_login_with_incorrect_credentials(page: Page, locale_code):
    page.goto("")
    locale.setlocale(locale.LC_ALL , locale_code)
    login_page = LoginPage(page)

    login_page.login(login_page.standard_username, login_page.incorrect_password)

    expect(login_page.error_incorrect_credentials).to_be_visible()	
    expect(login_page.error_incorrect_credentials).to_contain_text(login_page.translations[locale_code]['error_message'])

    
@pytest.mark.parametrize("locale_code", ['en_GB', 'es_ES'])
def test_login_as_a_standard_user(page: Page, locale_code):
    page.goto("")
    locale.setlocale(locale.LC_ALL , locale_code)
    login_page = LoginPage(page)

    login_page.login(login_page.standard_username, login_page.standard_password)

    expect(login_page.homepage_title).to_contain_text(login_page.translations[locale_code]['homepage_title'])
