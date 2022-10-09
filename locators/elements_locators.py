from selenium.webdriver.common.by import By


class HomePageLocators:
    ENG_LANG = (By.CSS_SELECTOR, "[id='lang-links']>ul>li:first-of-type")
    RU_LANG = (By.CSS_SELECTOR, "[id='lang-links']>ul>li:last-of-type")
    NOT_ACTUAL_LANG = (By.CSS_SELECTOR, "[id='lang-links']>ul>li>a")
    ACTUAL_LANG = (By.CSS_SELECTOR, "[id='lang-links']>ul>li>span")
    HTML = (By.CSS_SELECTOR, "html[lang]")

class DropDownPageLocators:
    UNIVERSITY = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(1)")
    PROGRAMS = (By.XPATH, "//a[@href='/education']/..")
    FACULTIES = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(3)")
    CENTERS = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(4)")
    EVENTS = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(5)")
