from pages.main_page import MainPage
import allure
import data


class TestPreOrderTaxi:

    @allure.title('Проверка переключения между табами  c Быстрый на Оптимальный')
    @allure.description('Проверяем что таб Оптимальный становиться активный при клике по нему и происходит перерасчет стоимости авто и времени')
    def test_switch_tab_optimal_one_route_tab_switched_and_time_cost_changed(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        fast_time = page_main.get_text_element_travel_time()
        fast_cost = page_main.get_text_element_free_avto()
        page_main.click_tab_optimal()
        optimal_time = page_main.get_text_element_travel_time()
        optimal_cost = page_main.get_text_element_free_avto()

        assert page_main.get_text_active_tab() == data.VERIFICATION_TEXT_TAB_OPTIMAL
        assert fast_time != optimal_time and fast_cost != optimal_cost

    @allure.title('Проверка переключения на таб Свой и активность типов передвижений')
    @allure.description('Переключаемся на таб Свой с таба Быстрый и проверяем что каждый из типов передвижения становвится активным')
    def test_switch_tab_mine_one_route_tab_switched_and_all_type_active(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_tab_mine()

        assert page_main.get_text_active_tab() == data.VERIFICATION_TEXT_TAB_MINE
        assert page_main.check_active_type() == "Element active"

    @allure.title('Проверка активности кнопки "Вызвать такси" для типа такси')
    @allure.description('Вводим адреса маршрута, выбираем тариф Свой и проверяем что после клика появляется кнопка "Ввести номер и заказать"')
    def test_button_call_taxi_click_button_visibility_button_order_taxi(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_tab_mine()
        page_main.click_button_call_taxi()

        assert page_main.check_visibility_button_order_taxi() == "Element found"

    @allure.title('Проверка активности кнопки "Забронировать" для типа Драйв')
    @allure.description('Вводим адреса маршрута, выбираем тариф Свой, переключаемся на тип Драйв и проверяем что после клика на кнопку Забронировать появляется кнопка "Ввести права и забронировать"')
    def test_button_book_click_button_visibility_button_book_and_input_license(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_tab_mine()
        page_main.click_type_drive()
        page_main.click_button_to_book()

        assert page_main.check_visibility_button_book_and_input_license() == "Element found"