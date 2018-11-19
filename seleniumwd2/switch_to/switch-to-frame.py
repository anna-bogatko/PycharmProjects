from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using Id
        #driver.switch_to.frame("courses-iframe")

        # Switch to frame using name
        #driver.switch_to.frame("iframe-name")

        # Switch to frame using numbers
        driver.switch_to.frame(0) # 0 number because only one iframe is present on the page
        time.sleep(3)

        # Search course
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("python")
        time.sleep(3)

        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)
        driver.find_element(By.ID, "name").send_keys("Test successful")

ff = SwitchToFrame()
ff.test()
