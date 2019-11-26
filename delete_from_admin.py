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
        driver.get("http://sharmilashrestha.pythonanywhere.com/admin/")
        assert "Logged In"
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/th/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
        assert "Delete post"
        driver.get("http://sharmilashrestha.pythonanywhere.com/admin/blog/post/")
        time.sleep(1)
        driver.get("http://sharmilashrestha.pythonanywhere.com/admin/blog/post/")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()