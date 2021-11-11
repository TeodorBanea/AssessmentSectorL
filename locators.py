from selenium.webdriver.common.by import By


class BayutLocators(object):

    search_dropdown = (By.XPATH, "//div[@name='purpose']//span[@class='ef5cccac']")

    buy_selection = (By.XPATH, "//button[normalize-space()='Buy']")

    input_locationToTest = (By.XPATH, "//input[@type='text']")

    select_first_option = (By.XPATH, "(//button[@class='_0e756b14'])")

    find_button = (By.XPATH, "//a[normalize-space()='Find']")

    select_to_rent = (By.XPATH, "//div[@class='d8530318']")

    view_all_options = (By.XPATH, "(//div[@role='button'][normalize-space()='View all'])[3]")

    links_to_test = (By.XPATH, "//body//div//div[@aria-label='Popular properties']//div//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//ul[1]//li//a")

    location_json = (By.XPATH, "//script[contains(text(),'{\"@context\":\"https://schema.org\",\"@type\":[\"Place\",')]")

    rent_selection = (By.XPATH,"(//span[contains(text(),'Rent')])[2]")

    selected_location = (By.XPATH,"//span[@aria-label='Filter label']")

    messagePurpose = "The purpose section was not loaded correctly."
    messageLocation = "The search page did not load the correct location."
