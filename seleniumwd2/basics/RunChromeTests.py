from selenium import webdriver
import os

class RunChromeTests():
    #http: // chromedriver.storage.googleapis.com / index.html

    def test(self):
        driverLocation = "C:/Chromedriver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        #Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)

        #Open the provided URL
        driver.get("https://learn.letskodeit.com/")

ff = RunChromeTests()
ff.test()

