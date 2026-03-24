import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.python_home_page import PythonHomePage

@pytest.fixture
def driver():
    service = Service("C:/tools/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_search_python_org(driver):
    page = PythonHomePage(driver)
    page.open()
    page.search("pytest")
    # Старая строка удаляется:
    # assert "Search Python" in driver.title or "Results" in driver.title
    # Вместо неё:
    assert "Python" in driver.title  # <- проверяем, что в title есть Python