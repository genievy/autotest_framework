from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


"""
Инициируем класс BaseObjects, объект которого при создании будет принимать в качестве параметров driver и url
Здесь функции, которые открывают веб-страницы, совершают всевозможные действия на страницах,
осущ-т поиск элементов в DOM, возвращают элементы как объекты
"""
class BaseObjects:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        return self.driver.get(self.url)

    def find_element(self, element):
        return self.driver.find_element(element)

    def element_visible(self, element, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(element))

    def lang_is(self):
        return self.driver.execute_script("return document.querySelector('html').lang")

    def get_attribute(self, locator, attribute):
        script = f'return document.querySelector("{locator}").{attribute}'
        return self.driver.execute_script(script)
