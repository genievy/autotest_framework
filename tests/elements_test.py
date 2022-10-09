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
            real_lang = page.get_attribute('html', 'lang')
            print(real_lang)
            assert new_lang != actual_lang, 'The language has not changed.'

    class TestDropdownMenu:
        def test_university(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_university()
            assert page.check_open_university() == 'true', 'The "University" drop-down menu is not displayed'

        def test_faculties(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_faculties()
            assert page.check_open_faculties() == 'true', 'The "Faculties" drop-down menu is not displayed'

        def test_centers(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_centers()
            assert page.check_open_centers() == 'true', 'The "Centers" drop-down menu is not displayed'

        def test_events(self, driver):
            page = DropdownMenu(driver, url.home_page)
            page.open()
            page.open_events()
            assert page.check_open_events() == 'true', 'The "Events" drop-down menu is not displayed'


class TestCustomCases:
    pass
