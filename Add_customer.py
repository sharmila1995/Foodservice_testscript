import csv
import unittest
import time
from itertools import islice

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HeyStack_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_site(self):
        # Open the CSV file containing all the records.
        with open('customer.csv', 'r') as csv_file:
            # Read the contents of the CSV file using comma as the delimiter.
            csv_reader = csv.reader(csv_file, delimiter=',')

            user = "instructor"
            # change this value to the desired password for the above user name
            pwd = "instructor1a"
            driver = self.driver
            driver.maximize_window()
            driver.get("http://sharmila.pythonanywhere.com/admin/")
            elem = driver.find_element_by_id("id_username")
            elem.send_keys(user)
            time.sleep(2)
            elem = driver.find_element_by_id("id_password")
            elem.send_keys(pwd)
            time.sleep(2)
            elem.send_keys(Keys.RETURN)
            assert "Logged In"

            count = 0
            for row in islice(csv_reader, 1, None):
                if count < 3:
                    driver.get("http://sharmila.pythonanywhere.com/admin/")
                    time.sleep(2)
                    elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a").click()
                    time.sleep(2)
                    driver.find_element_by_id("id_cust_name").send_keys(row[0])
                    driver.find_element_by_id("id_organization").send_keys(row[1])
                    driver.find_element_by_id("id_role").send_keys(row[2])
                    driver.find_element_by_id("id_email").send_keys(row[3])
                    driver.find_element_by_id("id_bldgroom").send_keys(row[4])
                    driver.find_element_by_id("id_address").send_keys(row[5])
                    driver.find_element_by_id("id_account_number").send_keys(row[6])
                    driver.find_element_by_id("id_city").send_keys(row[7])
                    driver.find_element_by_id("id_state").send_keys(row[8])
                    driver.find_element_by_id("id_zipcode").send_keys(row[9])
                    driver.find_element_by_id("id_phone_number").send_keys(row[10])
                    time.sleep(2)
                    elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
                    time.sleep(2)

                    assert "New customer added"

                count += 1

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
