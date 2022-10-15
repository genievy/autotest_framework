import allure
from pages.elements_page import LanguageSelection, DropdownMenu
from data.data import Url as url


@allure.suite("Test elements")
class TestBasePage:
    @allure.feature('Testing the language selection')
    class TestLanguageSelection:
        def test_language_selection(self, driver):
            page = LanguageSelection(driver, url.home_page)
            page.open()
            actual_lang = page.check_lang()
            page.change_lang()
            new_lang = page.check_lang()
            assert new_lang != actual_lang, 'The language has not changed.'

    @allure.feature('Testing the main menu buttons')
    class TestDropdownMenu:
        @allure.title('Testing the "University"-menu button')
        def test_university(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_university()
            assert page.check_button_university() == 'expanded dropdown open', 'The "University"-menu is not displayed'
            assert page.check_open_university() != 'True', 'The "University"-button does not function'

        @allure.title('Testing the "Departments"-menu button')
        def test_faculties(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_departments()
            assert page.check_button_departments() == 'expanded dropdown open', 'The "Department"-menu is not displayed'
            assert page.check_open_departments() != 'True', 'The "faculties"-button does not function'

        @allure.title('Testing the "Research"-menu button')
        def test_centers(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_research()
            assert page.check_button_research() == 'expanded dropdown open', 'The "Research"-menu is not displayed'  # open
            assert page.check_open_research() != 'True', 'The "Centers"-button does not function'

        @allure.title('Testing the "Events"-menu button')
        def test_events(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_events()
            assert page.check_button_events() == 'expanded dropdown open', 'The "Events"-menu is not displayed'
            assert page.check_open_events() != 'True', 'The "Events"-button does not function'


class TestCustomCases:
    pass
