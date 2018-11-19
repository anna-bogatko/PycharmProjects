from selenium import webdriver
from selenium.webdriver.common.by import By
from wait_types.explicit_wait_type import ExplicitWaitType
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()

        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/24/2018")
        returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
        returnDate.click()
        returnDate.clear()
        returnDate.send_keys("12/26/2018")
        driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").click()

        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()