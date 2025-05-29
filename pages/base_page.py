from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Ожидание загрузки выбранного элемента')
    def wait_for_load_element(self, element):
        WebDriverWait(self.browser, 3).until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Клик по выбранному элементу')
    def find_element_on_page(self, element):
        self.browser.find_element(*element)

    @allure.step('Клик по выбранному элементу')
    def click_element(self, find_element):
        self.browser.find_element(*find_element).click()

    @allure.step('Ожидание пропажи модульного окна"')
    def wait_for_invisibility_element(self, element):
        WebDriverWait(self.browser, 60).until(expected_conditions.invisibility_of_element_located(element))

    @allure.step('Ввод выбранных значений в поле')
    def set_input_data(self, element, data):
        self.browser.find_element(*element).send_keys(data)

    @allure.step('Получаем значение элемента')
    def get_find_element_on_page(self, element):
        return self.browser.find_element(*element)

    @allure.step('Получаем текст выбранного элемента')
    def get_text_element(self, element):
        return self.browser.find_element(*element).text

    @allure.step('Проверяем что элемент есть на странице')
    def check_visibility_element(self, element):
        data = self.get_find_element_on_page(*element)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Наведение курсора на нужный элемент')
    def hoverable_element(self, element):
        hoverable = self.browser.find_element(*element)
        actions = ActionChains(self.browser)
        actions.pause(2)
        actions.move_to_element(hoverable).perform()