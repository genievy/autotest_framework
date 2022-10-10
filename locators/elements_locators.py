from selenium.webdriver.common.by import By


class HomePageElements:
    ENG_LANG = (By.CSS_SELECTOR, "[id='lang-links']>ul>li:first-of-type")
    RU_LANG = (By.CSS_SELECTOR, "[id='lang-links']>ul>li:last-of-type")
    NOT_ACTUAL_LANG = (By.CSS_SELECTOR, "[id='lang-links']>ul>li>a")
    ACTUAL_LANG = (By.CSS_SELECTOR, "[id='lang-links']>ul>li>span")
    HTML = (By.CSS_SELECTOR, "html[lang]")


class DropDownPageElements:
    UNIVERSITY = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(1)")
    UNIVERSITY_MENU = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(1)>ul")
    PROGRAMS = (By.XPATH, "//a[@href='/education']/..")
    DEPARTMENTS = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(3)")
    DEPARTMENTS_MENU = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(3)>ul")
    RESEARCH = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(4)")
    RESEARCH_MENU = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(4)>ul")
    EVENTS = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(5)")
    EVENTS_MENU = (By.CSS_SELECTOR, "li[class*='expanded']:nth-child(5)>ul")


class DropDownPageLocators:
    UNIVERSITY: str = "[class*='menu nav']>li:nth-child(1)"
    DEPARTMENTS: str = "[class*='menu nav']>li:nth-child(3)"
    RESEARCH: str = "[class*='menu nav']>li:nth-child(4)"
    EVENTS: str = "[class*='menu nav']>li:nth-child(5)"
    HTML: str = "html"


class DropDownPageAttribute:
    CLASS_NAME = "className"
    AREA_EXPANDED: str = "ariaExpanded"
    LANG: str = "lang"
