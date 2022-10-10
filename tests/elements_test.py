from pages.elements_page import LanguageSelection, DropdownMenu
from data.data import Url as url


class TestBasePage:

    class TestLanguageSelection:
        def test_language_selection(self, driver):
            page = LanguageSelection(driver, url='https://eusp.org/')
            page.open()
            actual_lang = page.check_lang()
            page.change_lang()
            new_lang = page.check_lang()
            assert new_lang != actual_lang, 'The language has not changed.'

    class TestDropdownMenu:
        def test_university(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_university()
            assert page.check_button_university() == 'expanded dropdown open', 'The "University" drop-down menu is not displayed'
            assert page.check_open_university() != 'True', 'The "University"-button does not function'

        def test_faculties(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_faculties()
            assert page.check_button_faculties() == 'expanded dropdown open', 'The "faculties" drop-down menu is not displayed'
            assert page.check_open_faculties() != 'True', 'The "faculties"-button does not function'

        def test_centers(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_centers()
            assert page.check_button_centers() == 'expanded dropdown open', 'The "Centers" drop-down menu is not displayed'
            assert page.check_open_centers() != 'True', 'The "Centers"-button does not function'

        def test_events(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_events()
            assert page.check_button_events() == 'expanded dropdown open', 'The "Events" drop-down menu is not displayed'
            assert page.check_open_events() != 'True', 'The "Events"-button does not function'


class TestCustomCases:
    pass
