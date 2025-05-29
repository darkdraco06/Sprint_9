from pages.main_page import MainPage
import allure
import data
import  pytest


class TestBlockRoute:

    @allure.title('Проверка отображения блока маршрута при заполнии адресов начала и конца маршрута')
    @allure.description('Вводим адресса начала и конца маршрута и проряем что появился блок с выбором маршрута')
    @pytest.mark.parametrize(
        'point_a, point_b',
        [
            [data.ADDRESS_HAMOVSLIY_VAL, data.ADDRESS_ZUBOVSKIY_BULVAR],
            [data.ADDRESS_ZUBOVSKIY_BULVAR, data.ADDRESS_HAMOVSLIY_VAL]
        ]
    )
    def test_block_route_displayed_two_route_block_displayed(self, browser, point_a, point_b):
        page_main = MainPage(browser)
        page_main.input_address_from(point_a)
        page_main.input_address_where(point_b)

        assert page_main.check_visibility_point_a() == "Element found" and page_main.check_visibility_point_b() == "Element found"

    @allure.title('Проверка отображени времени в пути и стоимости авто при одинаковом адресе начала и конца маршрута')
    @allure.description('Вводим одинаковые адреса начала и конца маршрут и проряем что стоимость авто бесплатна а время пути равно нулю')
    @pytest.mark.parametrize(
        'point_a, point_b',
        [
            [data.ADDRESS_HAMOVSLIY_VAL, data.ADDRESS_HAMOVSLIY_VAL],
            [data.ADDRESS_ZUBOVSKIY_BULVAR, data.ADDRESS_ZUBOVSKIY_BULVAR]
        ]
    )
    def test_time_travel_and_time_one_address_avto_free_and_time_zero(self, browser, point_a, point_b):
        page_main = MainPage(browser)

        page_main.input_address_from(point_a)
        page_main.input_address_where(point_b)
        avto = page_main.get_text_element_free_avto()
        travel = page_main.get_text_element_travel_time()
        assert  avto == data.VERIFICATION_TEXT_AVTO_FREE
        assert  travel == data.VERIFICATION_TEXT_TIME_TRAVEL
