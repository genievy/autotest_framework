import allure
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BaseObjects:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Opens the browser')
    def open(self):
        return self.driver.get(self.url)

    @allure.step('Finds the element')
    def find_element(self, element):
        return self.driver.find_element(element)

    @allure.step('Returns the element if visible')
    def element_visible(self, element, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(element))

    def lang_is(self):
        return self.driver.execute_script("return document.querySelector('html').lang")

    @allure.step('Returns the attribute value by locator')
    def get_attribute(self, locator, attribute):
        script = f'return document.querySelector("{locator}").{attribute}'
        return self.driver.execute_script(script)
