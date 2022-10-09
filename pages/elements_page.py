from pages.base_objects import BaseObjects
from locators.elements_locators import HomePageLocators, DropDownPageLocators
import time

class LanguageSelection(BaseObjects):
    locators = HomePageLocators()

    def change_lang(self):
        self.element_visible(self.locators.NOT_ACTUAL_LANG).click()

    def check_lang(self):
        return self.lang_is()



class DropdownMenu(BaseObjects):
    locators = DropDownPageLocators()

    def open_university(self):
        self.element_visible(self.locators.UNIVERSITY).click()

    def check_open_university(self):
        return self.get_attribute("[class*='menu nav']>li:nth-child(1)>a", "ariaExpanded")

    def open_faculties(self):
        self.element_visible(self.locators.FACULTIES).click()

    def check_open_faculties(self):
        return self.get_attribute("[class*='menu nav']>li:nth-child(3)>a", "ariaExpanded")

    def open_centers(self):
        self.element_visible(self.locators.CENTERS).click()

    def check_open_centers(self):
        return self.get_attribute("[class*='menu nav']>li:nth-child(4)>a", "ariaExpanded")

    def open_events(self):
        self.element_visible(self.locators.EVENTS).click()

    def check_open_events(self):
        return self.get_attribute("[class*='menu nav']>li:nth-child(5)>a", "ariaExpanded")
