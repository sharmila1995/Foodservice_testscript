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
        time.sleep(3)
        # click post
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/a").click()
        time.sleep(3)
        # click add post
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[1]/div/div/select").click()
        time.sleep(3)
        # add author
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[1]/div/div/select/option[2]").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_title").send_keys("Test from admin")
        time.sleep(3)
        elem = driver.find_element_by_id("id_text").send_keys("text from admin")
        time.sleep(3)
        # add published date and time
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[1]/a[1]").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[2]/a[1]").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(3)
        assert "New post created"
        driver.get("http://sharmilashrestha.pythonanywhere.com/admin/blog/post/")
        time.sleep(1)
        driver.get("http://sharmilashrestha.pythonanywhere.com/admin/blog/post/")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()