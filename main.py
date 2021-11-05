import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time


class LocationSearch(unittest.TestCase):

    def setUp(self):
        PATH = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(PATH)

    def test_search_location(self):
        driver = self.driver
        driver.get("https://www.bayut.com/")

        cursor = driver.find_element(By.XPATH ,"//div[@name='purpose']//span[@class='ef5cccac']")
        cursor.click()

        cursor = driver.find_element(By.XPATH, "//button[normalize-space()='Buy']")
        cursor.click()

        inputlocation = driver.find_element(By.XPATH, "//input[@type='text']")
        inputlocation.send_keys("Dubai Marina")
        time.sleep(0.2)
        cursor = driver.find_element(By.XPATH,"(//button[@class='_0e756b14'])")
        cursor.click()

        cursor = driver.find_element(By.XPATH, "//a[normalize-space()='Find']")
        cursor.click()
        time.sleep(1)

        json_location = driver.find_element(By.XPATH,"//script[contains(text(),'{\"@context\":\"https://schema.org\",\"@type\":[\"Place\",')]").get_attribute('innerHTML')
        parsed_json = json.loads(json_location)
        for element in parsed_json['itemListElement']:
            #print(element['mainEntity']['address']['addressLocality'])
            self.assertEqual(element['mainEntity']['address']['addressLocality'], 'Dubai Marina')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()