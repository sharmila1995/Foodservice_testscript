
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://sharmilashrestha.pythonanywhere.com/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://sharmilashrestha.pythonanywhere.com/")
        assert "Logged In"
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("test post with selenium")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("test post of text with selenium")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        assert "New post created"
        driver.get("http://sharmilashrestha.pythonanywhere.com/")
        time.sleep(1)
        driver.get("http://sharmilashrestha.pythonanywhere.com/")
        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()



