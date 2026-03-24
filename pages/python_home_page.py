from selenium.webdriver.common.by import By

class PythonHomePage:
    URL = "https://www.python.org"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def search(self, query):
        search_box = self.driver.find_element(By.ID, "id-search-field")
        search_box.clear()
        search_box.send_keys(query)
        self.driver.find_element(By.ID, "submit").click()