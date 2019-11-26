import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# This will test the login functionality
class HeyStack_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # Remember to create the account for user and pwd before running, otherwise it won't work
    def test_site(self):
        # change this value to the desired username
        user = "instructor"
        # change this value to the desired password for the above user name
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://sharmila.pythonanywhere.com/")
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        driver.get("http://sharmila.pythonanywhere.com/")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[14]/a").click()
        time.sleep(3)
        driver.get("http://sharmila.pythonanywhere.com/customer_list")
        time.sleep(3)

        assert "Customer summary"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
