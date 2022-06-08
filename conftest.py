import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose interface of browser')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption('language')

    match browser_name:
        case 'chrome':
            print("\nstart chrome browser for test..")

            from selenium.webdriver.chrome.options import Options
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            browser = webdriver.Chrome(options=options)

        case 'firefox':
            print("\nstart firefox browser for test..")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language)
            browser = webdriver.Firefox(firefox_profile=fp)

        case _:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser

    print("\nquit browser..")
    browser.quit()
