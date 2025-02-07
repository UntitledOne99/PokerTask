from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class BasePage:
    waiting_time = 5
###Базовые методы

    def __init__(self, browser):
        self.browser = browser

###Кастомный метод для поиска элементов с ожиданием
    def find_element(self, locator,highlight=True,time=waiting_time):
        elem = WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")
        if highlight:
            self.highlight(elem)
            return elem
        else:
            return elem

    def find_elements(self, locator,time=waiting_time):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

###Подкраска выбранных элементов для наглядности. Не несет функциональной пользы. Взял из пет-проекта

    def highlight(self, element):
        driver = element._parent
        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
        original_style = element.get_attribute('style')
        apply_style("border: 3px solid red;")
        sleep(.3)
        apply_style(original_style)