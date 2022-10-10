from pages.base_objects import BaseObjects
from locators.elements_locators import HomePageElements, DropDownPageElements
from locators.elements_locators import DropDownPageLocators, DropDownPageAttribute


class LanguageSelection(BaseObjects):
    elements = HomePageElements()
    locators = DropDownPageLocators()

    def change_lang(self):
        self.element_visible(self.elements.NOT_ACTUAL_LANG).click()

    def check_lang(self):
        return self.lang_is()


class DropdownMenu(BaseObjects):
    elements = DropDownPageElements()
    locators = DropDownPageLocators()
    attribute = DropDownPageAttribute()

    def open_university(self):
        self.element_visible(self.elements.UNIVERSITY).click()

    def check_button_university(self):
        return self.get_attribute(self.locators.UNIVERSITY, self.attribute.CLASS_NAME)

    def check_open_university(self):
        return True if self.element_visible(self.elements.UNIVERSITY_MENU) else False

    def open_departments(self):
        self.element_visible(self.elements.DEPARTMENTS).click()

    def check_button_departments(self):
        return self.get_attribute(self.locators.DEPARTMENTS, self.attribute.CLASS_NAME)

    def check_open_departments(self):
        return True if self.element_visible(self.elements.DEPARTMENTS_MENU) else False

    def open_research(self):
        self.element_visible(self.elements.RESEARCH).click()

    def check_button_research(self):
        return self.get_attribute(self.locators.RESEARCH, self.attribute.CLASS_NAME)

    def check_open_research(self):
        return True if self.element_visible(self.elements.RESEARCH_MENU) else False

    def open_events(self):
        self.element_visible(self.elements.EVENTS).click()

    def check_button_events(self):
        return self.get_attribute(self.locators.EVENTS, self.attribute.CLASS_NAME)

    def check_open_events(self):
        return True if self.element_visible(self.elements.EVENTS_MENU) else False
