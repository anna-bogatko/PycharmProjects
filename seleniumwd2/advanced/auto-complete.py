from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete():

    def test(self):
        baseUrl = "https://paulcamper.de"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Send Partial Data
        cityField = driver.find_element_by_xpath("//div[@class='container___2LTox']//input[1]")
        cityField.send_keys("New York")

        time.sleep(3)
        # Find the item and click
        itemToSelect = driver.find_element_by_xpath("//ul[@id='react-geo-list']//span[contains(text(), 'Mills, New York, Vereinigte Staaten')]")
        itemToSelect.click()

        # time.sleep(3)
        # driver.quit()

ff = AutoComplete()
ff.test()