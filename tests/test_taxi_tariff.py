import locators.main_page
from pages.main_page import MainPage
import allure
import data
import  pytest


class TestTaxiTariff:

    @allure.title('Проверка отображения тарифов такси')
    @allure.description('Вводим точки маршрутов и проверяем что отображается каждый из 6 тарифов такси, а так же на странице есть 1 активый тариф')
    @pytest.mark.parametrize(
        'tariff',
        [
            [locators.main_page.TAXI_TARIFF_WORK],
            [locators.main_page.TAXI_TARIFF_SLEEP],
            [locators.main_page.TAXI_TARIFF_WEEKEND],
            [locators.main_page.TAXI_TARIFF_TALK],
            [locators.main_page.TAXI_TARIFF_COMFORT],
            [locators.main_page.TAXI_TARIFF_GLOSSY]
        ]
    )
    def test_displayed_tariff_six_tariff_tariff_displayed_and_one_activ(self, browser, address, tariff):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()

        assert page_main.get_active_tariff() in data.ALL_TAXI_TARIFF
        assert page_main.check_visibility_element(tariff) == "Element found"

    @allure.title('Проверка отображения модального окна "О тарифе" при наведнии на иконку i и проверка текста описания')
    @allure.description('Выбираем нужный тариф, наводимся на иконку i. Проверяем что окно стало видимым и описание тарифа соотевтсвует ТЗ')
    @pytest.mark.parametrize(
        'tariff, text',
        [
            [locators.main_page.TAXI_TARIFF_WORK, data.VERIFICATION_DESCRIPTION_TEXT_WORK],
            [locators.main_page.TAXI_TARIFF_SLEEP, data.VERIFICATION_DESCRIPTION_TEXT_SLEEP],
            [locators.main_page.TAXI_TARIFF_WEEKEND, data.VERIFICATION_DESCRIPTION_TEXT_WEEKEND],
            [locators.main_page.TAXI_TARIFF_TALK, data.VERIFICATION_DESCRIPTION_TEXT_TALK],
            [locators.main_page.TAXI_TARIFF_COMFORT, data.VERIFICATION_DESCRIPTION_TEXT_COMFORT],
            [locators.main_page.TAXI_TARIFF_GLOSSY, data.VERIFICATION_DESCRIPTION_TEXT_GLOSSY]
        ]
    )
    @pytest.mark.xfail(
         reason="Баг AAA-001: В описании о тарифах в модальном окне. Перепутаны тексты тарифа Сонный и тарифа Разговрчивый")
    def test_displayed_modal_window_about_tariff_six_tariff_windows_displayed_and_text_verefication(self, browser, address, tariff, text):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.wait_for_load_element(tariff)
        page_main.click_element(tariff)
        page_main.wait_for_load_element(locators.main_page.BUTTON_I_ACTIVE_TARIFF_TAXI)
        page_main.hoverable_to_button_i()

        assert page_main.check_visibility_modal_window_about_tariff() == "Element found"
        assert page_main.get_text_about_active_tariff() == text


    @allure.title('Проверка отображения блока с полями для заполнения информации')
    @allure.description('Проверяем что блок с полями для заполнения отображается и в нем есть поля Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси')
    @pytest.mark.parametrize(
        'field',
        [
            [locators.main_page.FIELD_PHONE],
            [locators.main_page.FIELD_REQUIREMENTS],
            [locators.main_page.FIELD_COMMENT],
            [locators.main_page.FIELD_PAY]
        ]
    )
    def test_form_field_four_field_displayed_field(self, browser, address, field):
        page_main = MainPage(browser)
        page_main.input_address_from(address[0])
        page_main.input_address_where(address[1])
        page_main.click_button_call_taxi()
        page_main.wait_visibility_order_form_taxi()

        assert page_main.check_visibility_element(field) == "Element found"
