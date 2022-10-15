import allure
from pages.base_objects import BaseObjects
from locators.elements_locators import HomePageElements, DropDownPageElements
from locators.elements_locators import DropDownPageLocators, DropDownPageAttribute


class LanguageSelection(BaseObjects):
    elements = HomePageElements()
    locators = DropDownPageLocators()
    attribute = DropDownPageAttribute

    @allure.step("Change language")
    def change_lang(self):
        self.element_visible(self.elements.NOT_ACTUAL_LANG).click()

    @allure.step("Checking the language change")
    def check_lang(self):
        return self.get_attribute(self.locators.HTML, self.attribute.LANG)


class DropdownMenu(BaseObjects):
    elements = DropDownPageElements()
    locators = DropDownPageLocators()
    attribute = DropDownPageAttribute()

    @allure.step("Click on the 'University' button")
    def open_university(self):
        self.element_visible(self.elements.UNIVERSITY).click()

    @allure.step("Get the value of the 'University' button attribute")
    def check_button_university(self):
        return self.get_attribute(self.locators.UNIVERSITY, self.attribute.CLASS_NAME)

    @allure.step("Get the value of the drop-down menu 'University' attribute")
    def check_open_university(self):
        return True if self.element_visible(self.elements.UNIVERSITY_MENU) else False

    @allure.step("Click on the 'Departments' button")
    def open_departments(self):
        self.element_visible(self.elements.DEPARTMENTS).click()

    @allure.step("Get the value of the 'Departments' button attribute")
    def check_button_departments(self):
        return self.get_attribute(self.locators.DEPARTMENTS, self.attribute.CLASS_NAME)

    @allure.step("Get the value of the drop-down menu 'Departments' attribute")
    def check_open_departments(self):
        return True if self.element_visible(self.elements.DEPARTMENTS_MENU) else False

    @allure.step("Click on the 'Research' button")
    def open_research(self):
        self.element_visible(self.elements.RESEARCH).click()

    @allure.step("Get the value of the 'Research' button attribute")
    def check_button_research(self):
        return self.get_attribute(self.locators.RESEARCH, self.attribute.CLASS_NAME)

    @allure.step("Get the value of the drop-down menu 'Research' attribute")
    def check_open_research(self):
        return True if self.element_visible(self.elements.RESEARCH_MENU) else False

    @allure.step("Click on the 'Events' button")
    def open_events(self):
        self.element_visible(self.elements.EVENTS).click()

    @allure.step("Get the value of the 'Events' button attribute")
    def check_button_events(self):
        return self.get_attribute(self.locators.EVENTS, self.attribute.CLASS_NAME)

    @allure.step("Get the value of the drop-down menu 'Events' attribute")
    def check_open_events(self):
        return True if self.element_visible(self.elements.EVENTS_MENU) else False
