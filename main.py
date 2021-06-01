from selenium import webdriver
import unittest
from pages.pageindex import *
from pages.pageitemlist import *
from pages.pageitem import *


class Items(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome('C:\\chromedriver.exe', options=chrome_options)
        self.driver.get('http://automationpractice.com/index.php')

    def test_view_item_page(self):
        page_index = Page_index(self.driver)
        page_item_list = Page_item_list(self.driver)
        page_item = Page_item(self.driver)

        page_index.search_items('dress')
        page_item_list.click_first_item()
        title, text_to_verify = page_item.verify_text('Printed Summer Dress')
        self.assertEqual(title, text_to_verify, 'Text should be different')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()