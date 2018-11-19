from selenium import webdriver

class FindByClassTag():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing the Element")

        if elementByClassName is not None:
            print("We found an element by ClassName")

        elementByTagName = driver.find_element_by_tag_name("h1")
        #elementByTagName.send_keys("Testing the Element")
        text = elementByTagName.text

        if elementByTagName is not None:
            print("We found an element by TagName and the text on element is: " + text)



ff = FindByClassTag()
ff.test()