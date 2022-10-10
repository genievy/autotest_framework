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

    def open_faculties(self):
        self.element_visible(self.elements.FACULTIES).click()

    def check_button_faculties(self):
        return self.get_attribute(self.locators.FACULTIES, self.attribute.CLASS_NAME)

    def check_open_faculties(self):
        return True if self.element_visible(self.elements.FACULTIES_MENU) else False

    def open_centers(self):
        self.element_visible(self.elements.CENTERS).click()

    def check_button_centers(self):
        return self.get_attribute(self.locators.CENTERS, self.attribute.CLASS_NAME)

    def check_open_centers(self):
        return True if self.element_visible(self.elements.CENTERS_MENU) else False

    def open_events(self):
        self.element_visible(self.elements.EVENTS).click()

    def check_button_events(self):
        return self.get_attribute(self.locators.EVENTS, self.attribute.CLASS_NAME)

    def check_open_events(self):
        return True if self.element_visible(self.elements.EVENTS_MENU) else False
