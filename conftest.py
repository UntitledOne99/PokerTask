from selenium import webdriver
import pytest
link = 'https://poker.evenbetpoker.com/html5-evenbetpoker/d/?tables/all'

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    yield browser
    browser.close()
    browser.quit()