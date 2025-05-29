from pages.base_page import BasePage
import locators.main_page
import allure
from selenium.common.exceptions import NoSuchElementException

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Вводим адрес начала маршрута')
    def input_address_from(self, address):
        self.set_input_data(locators.main_page.POINT_FROM, address)

    @allure.step('Вводим адрес конца маршрута ')
    def input_address_where(self, address):
        self.set_input_data(locators.main_page.POINT_WHERE, address)

    @allure.step('Проверям отображение точки начала маршрута')
    def check_visibility_point_a(self):
        self.wait_for_load_element(locators.main_page.MAP_POINT_A)
        data = self.get_find_element_on_page(locators.main_page.MAP_POINT_A)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверям отображение точки конца маршрута')
    def check_visibility_point_b(self):
        self.wait_for_load_element(locators.main_page.MAP_POINT_B)
        data = self.get_find_element_on_page(locators.main_page.MAP_POINT_B)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверям что типы активны')
    def check_active_type(self):
        try:
            element = self.find_element_on_page(locators.main_page.ACTIVE_TYPE)
        except NoSuchElementException:
             return "Element active"

    @allure.step('Проверяем текст с информацией о стоимсоти авто')
    def get_text_element_free_avto(self):
        self.wait_for_load_element(locators.main_page.ROUTE_BLOCK)
        return self.get_text_element(locators.main_page.TEXT_AVTO_COST)

    @allure.step('Проверяем текст с информацией о стоимости авто')
    def get_text_element_travel_time(self):
        self.wait_for_load_element(locators.main_page.ROUTE_BLOCK)
        return self.get_text_element(locators.main_page.TEXT_TIME)

    @allure.step('Переход на таб Оптимальный')
    def click_tab_optimal(self):
        self.wait_for_load_element(locators.main_page.TAB_OPTIMAL)
        self.click_element(locators.main_page.TAB_OPTIMAL)

    @allure.step('Переход на таб Свой')
    def click_tab_mine(self):
        self.wait_for_load_element(locators.main_page.TAB_MINE)
        self.click_element(locators.main_page.TAB_MINE)

    @allure.step('Получаем элемент таба Оптимальный')
    def get_text_active_tab(self):
         return self.get_text_element(locators.main_page.ACTIVE_TAB)

    @allure.step('Проверка отображения блока маршрута')
    def check_visibility_route_block(self):
        self.wait_for_load_element(locators.main_page.ROUTE_BLOCK)
        data = self.get_find_element_on_page(locators.main_page.ROUTE_BLOCK)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Клик по кнопке вызвать такси')
    def click_button_call_taxi(self):
        self.wait_for_load_element(locators.main_page.BUTTON_CALL_TAXI)
        self.click_element(locators.main_page.BUTTON_CALL_TAXI)

    @allure.step('Проверка отображения кнопки заказать такси')
    def check_visibility_button_order_taxi(self):
        self.wait_for_load_element(locators.main_page.BUTTON_ORDER_TAXI)
        data = self.get_find_element_on_page(locators.main_page.BUTTON_ORDER_TAXI)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Клик по тарифу Драйв')
    def click_type_drive(self):
        self.wait_for_load_element(locators.main_page.TYPE_DRIVE)
        self.click_element(locators.main_page.TYPE_DRIVE)

    @allure.step('Клик по кнопке заказть')
    def click_button_to_book(self):
        self.wait_for_load_element(locators.main_page.BUTTON_TO_BOOK)
        self.click_element(locators.main_page.BUTTON_TO_BOOK)

    @allure.step('Клик по кнопке вызвать такси')
    def click_button_button_order_taxi(self):
        self.wait_for_load_element(locators.main_page.BUTTON_ORDER_TAXI)
        self.click_element(locators.main_page.BUTTON_ORDER_TAXI)

    @allure.step('Проверка отображения кнопки заказать такси и ввести номер')
    def check_visibility_button_book_and_input_license(self):
        self.wait_for_load_element(locators.main_page.BUTTON_BOOK_AND_INPUT_LICENSE)
        data = self.get_find_element_on_page(locators.main_page.BUTTON_BOOK_AND_INPUT_LICENSE)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    # @allure.step('Проверка отображения окна поиск машины')
    # def check_visibility_modal_search_car(self):
    #     self.wait_for_load_element(locators.main_page.MODAL_SEARCH_CAR)
    #     data = self.get_find_element_on_page(locators.main_page.MODAL_SEARCH_CAR)
    #     if data.is_displayed():
    #         return "Element found"
    #     else:
    #         return "Element not found"

    @allure.step('Получить наименование активного тарифа')
    def get_active_tariff(self):
        self.wait_for_load_element(locators.main_page.ACTIVE_TARIFF_TAXI)
        return self.get_text_element(locators.main_page.ACTIVE_TARIFF_TAXI)

    @allure.step('Наводим курсор на кнопко i')
    def hoverable_to_button_i(self):
        self.wait_for_load_element(locators.main_page.BUTTON_I_ACTIVE_TARIFF_TAXI)
        self.hoverable_element(locators.main_page.BUTTON_I_ACTIVE_TARIFF_TAXI)

    @allure.step('Проверяем отображение окна о тарифе')
    def check_visibility_modal_window_about_tariff(self):
        self.wait_for_load_element(locators.main_page.TOOLTIP_ACTIVE_TARIFF)
        data = self.get_find_element_on_page(locators.main_page.TOOLTIP_ACTIVE_TARIFF)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Получаем описание активного тарифе')
    def get_text_about_active_tariff(self):
        return self.get_text_element(locators.main_page.TEXT_ABOUT_ACTIVE_TARIFF)

    @allure.step('Клик по кнопке вызвать такси')
    def wait_visibility_order_form_taxi(self):
        self.wait_for_load_element(locators.main_page.FORM_ORDER_TAXI)

    @allure.step('Включаем тогл для тарифа Рабочий - Столик для Ноутбука')
    def active_toggle_taxi_work_with_table_notebook(self):
        self.wait_for_load_element(locators.main_page.TAXI_TARIFF_WORK)
        self.click_element(locators.main_page.TAXI_TARIFF_WORK)
        self.wait_for_load_element(locators.main_page.FIELD_REQUIREMENTS)
        self.click_element(locators.main_page.FIELD_REQUIREMENTS)
        self.click_element(locators.main_page.TOGGLE_TABLE_NOTEBOOK)
        self.wait_for_load_element(locators.main_page.TOGGLE_TABLE_NOTEBOOK)

    @allure.step('Проверяем отображение заголовка в окне Поиск машины')
    def check_visibility_element_title_search_car(self):
        self.wait_for_load_element(locators.main_page.TITLE_SEARCH_CAR)
        data = self.get_find_element_on_page(locators.main_page.TITLE_SEARCH_CAR)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверяем отображение таймера в окне Поиск машины')
    def check_visibility_element_time_search_car(self):
        self.wait_for_load_element(locators.main_page.TITLE_SEARCH_CAR)
        data = self.get_find_element_on_page(locators.main_page.TIME_SEARCH_CAR)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверяем отображение кнопки Отмена в окне Поиск машины')
    def check_visibility_element_cancel_order(self):
        self.wait_for_load_element(locators.main_page.BUTTON_CANCEL)
        data = self.get_find_element_on_page(locators.main_page.BUTTON_CANCEL)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверяем отображение кнопки Детали в окне Поиск машины')
    def check_visibility_element_detail_order(self):
        self.wait_for_load_element(locators.main_page.BUTTON_DETAIL)
        data = self.get_find_element_on_page(locators.main_page.BUTTON_DETAIL)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Дожидаемся когда пропадет окно поиск машины')
    def wait_invisibility_window_search_car(self):
        self.wait_for_invisibility_element(locators.main_page.TITLE_SEARCH_CAR)

    @allure.step('Проверяем отображение заголовка в окне Заказа такси')
    def check_visibility_title_complete_order(self):
        data = self.get_find_element_on_page(locators.main_page.TITLE_COMPLITE_ORDER)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверяем отображение номера в окне Заказа такси')
    def check_visibility_number_car_complete_order(self):
        data = self.get_find_element_on_page(locators.main_page.AVTO_NUMBER)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверяем отображение картинки тарифа в окне Заказа такси')
    def check_visibility_img_tariff_complete_order(self):
        data = self.get_find_element_on_page(locators.main_page.IMG_TARIFF)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверяем отображение рейтингав окне Заказа такси')
    def check_visibility_rait_driver_tariff_complete_order(self):
        data = self.get_find_element_on_page(locators.main_page.IMG_TARIFF)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверяем отображение картинки водителя в окне Заказа такси')
    def check_visibility_img_driver_tariff_complete_order(self):
        data = self.get_find_element_on_page(locators.main_page.IMG_DRIVER)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверяем отображение имени водителя в окне Заказа такси')
    def check_visibility_name_driver_tariff_complete_order(self):
        data = self.get_find_element_on_page(locators.main_page.NAME_DRIVER)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Получаем цену тарифа в окне Заказа такси по кнопке Детали')
    def get_text_detail_cost_in_order_complete(self):
        return self.get_text_element(locators.main_page.DETAIL_COST_TARIF)

    @allure.step('Получаем первоначальную цену тарифы')
    def get_text_cost_active_tariff(self):
        return self.get_text_element(locators.main_page.COST_TARIF)

    @allure.step('Кликаем по кнопке Детали в окне Заказа такси')
    def click_detail_in_complete_order(self):
        self.click_element(locators.main_page.BUTTON_DETAIL)

    @allure.step('Кликаем по кнопке отмена в окне Заказа такси')
    def click_button_cansel_order(self):
        self.click_element(locators.main_page.BUTTON_CANCEL)

    @allure.step('Проверяем что окно Заказа такси пропало')
    def check_invisibility_window_order_car(self):
        data = self.get_find_element_on_page(locators.main_page.MODAL_ORDER_CAR)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"