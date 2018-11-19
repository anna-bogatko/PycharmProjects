from selenium import webdriver

class ElementState():

    def isEnabled(self):
        baseUrl = "http://www.google.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_id("gs_htif0")
        e1State = e1.is_enabled() # True for enabled and False for disabled
        print("E1 is enabled? -> " + str(e1State))

        e2 = driver.find_element_by_id("gs_taif0")
        e2State = e2.is_enabled()  # True for enabled and False for disabled
        print("E2 is enabled? -> " + str(e2State))

        e3 = driver.find_element_by_id("lst-ib")
        e3State = e3.is_displayed()  # True for enabled and False for disabled
        print("E3 is enabled? -> " + str(e3State))

        e3.send_keys("letskodeit")

e = ElementState()
e.isEnabled()

