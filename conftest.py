import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('+headless')
    driver = webdriver.Firefox(options)
    yield driver
    driver.quit()

