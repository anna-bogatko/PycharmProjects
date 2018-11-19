from selenium import webdriver

class FindByLinkText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementLinkText = driver.find_element_by_link_text("Login")

        if elementLinkText is not None:
            print("We found an element by LinkText")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialLinkText is not None:
            print("We found an element by PartialLinkText")



ff = FindByLinkText()
ff.test()