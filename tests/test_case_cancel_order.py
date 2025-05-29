from pages.main_page import MainPage
import allure
import  pytest

class TestOrderTaxi:
    @allure.title('Проверка отображения кнопки отмена в окне поиска такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. В окне поиска такси отображается кнопка отмены')

    def test_displayed_button_cancel_order_one_tariff_displayed_cancel (self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()

        assert page_main.check_visibility_element_cancel_order() == "Element found"

    @allure.title('Проверка отображения кнопки Детали в окне поиска такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. В окне поиска такси отображается кнопка Детали')

    def test_displayed_button_detail_order_one_tariff_displayed_deteil (self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()

        assert page_main.check_visibility_element_detail_order() == "Element found"

    @allure.title('Проверка отображения таймер в окне поиска такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. В окне поиска такси отображается таймер')

    def test_displayed_time_search_car_one_tariff_displayed_time (self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()

        assert page_main.check_visibility_element_time_search_car() == "Element found"

    @allure.title('Проверка отображения заголовок окна поиска машины')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. В окне отображается заголвок поиска машины')

    def test_displayed_title_search_car_one_tariff_displayed_title (self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()

        assert page_main.check_visibility_element_title_search_car() == "Element found"

    @allure.title('Проверка отображения заголовка окна Заказа такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. Дожидаемся когда пропадет окно поиска и проверяем в окне заказа такси отображается заголовок окна')

    def test_displayed_title_complete_car_one_tariff_displayed_title (self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()
        page_main.wait_invisibility_window_search_car()

        assert page_main.check_visibility_title_complete_order() == "Element found"


    @allure.title('Проверка отображения картинки тарифа в окне Заказа такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. Дожидаемся когда пропадет окно поиска и проверяем в окне заказа такси отображение картинки тарифа')
    def test_displayed_img_tariff_car_one_tariff_displayed_img (self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()
        page_main.wait_invisibility_window_search_car()

        assert page_main.check_visibility_img_tariff_complete_order() == "Element found"

    @allure.title('Проверка отображения картинки тарифа в окне Заказа такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. Дожидаемся когда пропадет окно поиска и проверяем в окне заказа такси отображение номера машины')
    def test_displayed_number_car_tariff_car_one_tariff_displayed_number_car(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()
        page_main.wait_invisibility_window_search_car()

        assert page_main.check_visibility_number_car_complete_order() == "Element found"

    @allure.title('Проверка отображения рейтинга в окне Заказа такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. Дожидаемся когда пропадет окно поиска и проверяем в окне заказа такси рейтинг')
    def test_displayed_rait_one_tariff_displayed_rait_driver(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()
        page_main.wait_invisibility_window_search_car()

        assert page_main.check_visibility_rait_driver_tariff_complete_order() == "Element found"

    @allure.title('Проверка отображения картинки водиетля в окне Заказа такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. Дожидаемся когда пропадет окно поиска и проверяем в окне заказа такси отображение картинки водителя')
    def test_displayed_img_driver_one_tariff_displayed_img_driver(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()
        page_main.wait_invisibility_window_search_car()

        assert page_main.check_visibility_img_driver_tariff_complete_order() == "Element found"

    @allure.title('Проверка отображения имени водителя в окне Заказа такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. Дожидаемся когда пропадет окно поиска и проверяем в окне заказа такси отображение имя водителя')
    def test_displayed_name_driver_one_tariff_displayed_name_driver(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()
        page_main.wait_invisibility_window_search_car()

        assert page_main.check_visibility_name_driver_tariff_complete_order() == "Element found"

    @allure.title('Проверка отображения кнопки Детали в окне Заказа такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. Дожидаемся когда пропадет окно поиска и проверяем в окне заказа такси отображение кнопки Детали')
    def test_displayed_detail_complete_order_one_tariff_displayed_detail(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()
        page_main.wait_invisibility_window_search_car()

        assert page_main.check_visibility_element_detail_order() == "Element found"

    @allure.title('Проверка отображения стоимости тарифа в окне Заказа такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. Дожидаемся когда пропадет окно поиска и октрыаем детали заказа. Проверяем цену тарифа с ценой в заказе')
    def test_displayed_total_cost_complete_order_one_tariff_total_cost_equal_tariff_cost(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()
        cost_tariff = page_main.get_text_cost_active_tariff()
        cost_tariff = cost_tariff.replace(" ", "")
        page_main.wait_invisibility_window_search_car()
        page_main.click_detail_in_complete_order()
        total_cost = page_main.get_text_detail_cost_in_order_complete()

        assert cost_tariff in total_cost

    @allure.title('Проверка отображения кнопки отмена в окне Заказа такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. Дожидаемся когда пропадет окно поиска и проверяем в окне заказа такси отображение кнопки отмена')
    def test_displayed_cancel_complete_order_one_tariff_displayed_cancel(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()
        page_main.wait_invisibility_window_search_car()

        assert page_main.check_visibility_element_cancel_order() == "Element found"

    @allure.title('Проверка отмены заказа в окне Заказа такси')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать. Дожидаемся когда пропадет окно поиска и проверяем в окне заказа проверяем отменуц заказа кликнув по кнопке отмена')
    @pytest.mark.xfail(reason="Баг AAA-002: Не работает кнопка отмены заказа такси")
    def test_cancel_order_one_tariff_cancel_order(self, browser, address):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.active_toggle_taxi_work_with_table_notebook()
        page_main.click_button_button_order_taxi()
        page_main.wait_invisibility_window_search_car()
        page_main.click_button_cansel_order()

        assert page_main.check_invisibility_window_order_car() == "Element not found"