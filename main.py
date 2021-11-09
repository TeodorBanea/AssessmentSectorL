import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LocationSearch(unittest.TestCase):

    def setUp(self):
        PATH = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.bayut.com/")

    def test_search_location(self):
        driver = self.driver

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

        json_location = driver.find_element(By.XPATH, "//script[contains(text(),'{\"@context\":\"https://schema.org\",\"@type\":[\"Place\",')]").get_attribute('innerHTML')
        parsed_json = json.loads(json_location)
        for element in parsed_json['itemListElement']:
            self.assertEqual(element['mainEntity']['address']['addressLocality'], 'Dubai Marina')

    def test_valid_links_bayut(self):
        driver = self.driver
        driver.maximize_window()
        links = [link.get_attribute("href") for link in driver.find_elements(By.XPATH, "//body//div//div[@aria-label='Popular properties']//div//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//ul[1]//li//a")]
        for link in links:
            driver.get(link)
            time.sleep(2)
            print("primu print din for " + link)
            print(link)
            time.sleep(1)

            purpose = driver.find_element(By.XPATH,"(//span[contains(text(),'Rent')])[2]")
            self.assertEqual(purpose.text, 'Rent')
            print("a trecut primu assert")

            location_aux = " ".join(link.split("/")[-2].split("-")).lower()

            location = driver.find_element(By.XPATH,"//span[@aria-label='Filter label']")

            self.assertIn(location_aux, location.text.replace("(","").replace(")","").lower())
            print("a trecut al doilea assert")

            time.sleep(2)

            print("a ajuns si la sfarsitul for-ului")
            time.sleep(1)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()