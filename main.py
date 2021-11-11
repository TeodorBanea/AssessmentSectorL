import unittest
from selenium import webdriver
from locators import BayutLocators
import json
import time


class LocationSearch(unittest.TestCase):

    def setUp(self):
        PATH = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.bayut.com/")

    def test_search_location(self):
        driver = self.driver

        cursor = driver.find_element(*BayutLocators.search_dropdown).click()

        cursor = driver.find_element(*BayutLocators.buy_selection).click()

        inputlocation = driver.find_element(*BayutLocators.input_locationToTest).send_keys("Dubai Marina")
        time.sleep(0.2)

        cursor = driver.find_element(*BayutLocators.select_first_option).click()

        cursor = driver.find_element(*BayutLocators.find_button).click()
        time.sleep(0.5)

        json_location = driver.find_element(*BayutLocators.location_json).get_attribute('innerHTML')
        parsed_json = json.loads(json_location)
        for element in parsed_json['itemListElement']:
            self.assertEqual(element['mainEntity']['address']['addressLocality'], 'Dubai Marina')

    def test_valid_links_bayut(self):
        driver = self.driver
        driver.maximize_window()
        links = [link.get_attribute("href") for link in driver.find_elements(*BayutLocators.links_to_test)]

        for link in links:
            driver.get(link)
            time.sleep(0.2)

            purpose = driver.find_element(*BayutLocators.rent_selection)
            self.assertEqual(purpose.text, 'Rent', BayutLocators.messagePurpose)

            location_aux = " ".join(link.split("/")[-2].split("-")).lower()
            location = driver.find_element(*BayutLocators.selected_location)
            self.assertIn(location_aux, location.text.replace("(","").replace(")","").lower(), BayutLocators.messageLocation)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()