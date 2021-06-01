from selenium.webdriver.common.by import By


class Page_item:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.XPATH, '//h1[@itemprop="name"]')

    def verify_text(self, text_to_verify):
        title = self.driver.find_element(*self.title).text
        return title, text_to_verify