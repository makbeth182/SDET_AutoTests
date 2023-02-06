import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Используем Headless если не нужен UI браузера
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1900,1030')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    if driver.find_element(By.ID, 'tinybox'):
        close_link = driver.find_element(By.ID, 'closeButton')
        if close_link:
            close_link.click()
    yield driver
    driver.quit()

