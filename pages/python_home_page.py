from selenium.webdriver.common.by import By

class PythonHomePage:
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.python.org")

    def search(self, query):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(query)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
