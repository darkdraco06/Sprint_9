import pytest
from selenium import webdriver
import curl
import data


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(curl.MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture
def address():
    address_data = [data.ADDRESS_HAMOVSLIY_VAL, data.ADDRESS_ZUBOVSKIY_BULVAR]
    return address_data
