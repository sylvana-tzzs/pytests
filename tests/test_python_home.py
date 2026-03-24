import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.python_home_page import PythonHomePage

@pytest.fixture
def driver():
    service = Service("C:/tools/chromedriver-win64/chromedriver.exe")  # твой путь к драйверу
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_search_python_org(driver):
    page = PythonHomePage(driver)
    page.open()
    page.search("pytest")
    assert "Python" in driver.title  # стабильная проверка заголовка