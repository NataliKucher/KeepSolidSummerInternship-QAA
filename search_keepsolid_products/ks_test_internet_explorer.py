from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class BasicTests(unittest.TestCase):
   
    baseurl = "https://www.keepsolid.com"
    
    def setUp(self):
        self.browser = webdriver.Ie()

        self.browser.maximize_window()
        self.browser.implicitly_wait(5)

        self.browser.get(BasicTests.baseurl)


    def test_search_keepsolid_products(self):
        self.browser.find_element_by_link_text("Products").click()
        self.browser.find_elements_by_xpath('//h1[text()="Products"]')
        

    def tearDown(self):
        self.browser.quit()
       

if __name__ == '__main__':
    unittest.main()
