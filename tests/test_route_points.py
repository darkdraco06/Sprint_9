from pages.main_page import MainPage
import allure
import data
import  pytest


class TestrRoutePoints:

    @allure.title('Проверка отображения точек начала и конца маршрута')
    @allure.description('Вводим адресса начала и конца маршрута и проверяем что конечные точки отобразились на карте')
    @pytest.mark.parametrize(
        'point_a, point_b',
        [
            [data.ADDRESS_HAMOVSLIY_VAL, data.ADDRESS_ZUBOVSKIY_BULVAR],
            [data.ADDRESS_ZUBOVSKIY_BULVAR, data.ADDRESS_HAMOVSLIY_VAL]
        ]
    )
    def test_points_visibility_on_map_two_route_points_displayed(self, browser, point_a, point_b):
        page_main = MainPage(browser)
        page_main.input_address_from(point_a)
        page_main.input_address_where(point_b)

        assert page_main.check_visibility_route_block() == "Element found"