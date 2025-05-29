from selenium.webdriver.common.by import By

MAP_POINT_A = [By.XPATH, '//ymaps[contains(@class, "___ff3333_20x26")]']
MAP_POINT_B = [By.XPATH, '//ymaps[contains(@class, "___4296ea_20x26")]']

POINT_FROM = (By.ID, "from")
POINT_WHERE = (By.ID, 'to')

ROUTE_BLOCK = [By.XPATH, '//div[@class="type-picker shown"]']

TEXT_AVTO_COST = [By.XPATH, '//div[@class="text"]']
TEXT_TIME = [By.XPATH, '//div[@class="duration"]']

TAB_OPTIMAL = [By.XPATH, '//div[text()="Оптимальный"]']
TAB_FAST = [By.XPATH, '//div[text()="Быстрый"]']
TAB_MINE = [By.XPATH, '//div[text()="Свой"]']

ACTIVE_TAB = [By.XPATH, '//div[contains(@class, "mode active")]']

TYPE_CAR = [By.XPATH, '//img[contains(@src, "car.")]']
TYPE_WALK = [By.XPATH, '//img[contains(@src, "walk.")]']
TYPE_TAXI = [By.XPATH, '//img[contains(@src, "taxi.")]']
TYPE_BIKE = [By.XPATH, '//img[contains(@src, "bike.")]']
TYPE_SCOOTER = [By.XPATH, '//img[contains(@src, "scooter.")]']
TYPE_DRIVE= [By.XPATH, '//img[contains(@src, "drive.")]']

ACTIVE_TYPE= [By.XPATH, '//div[contains(@class, "type disabled")]']

BUTTON_CALL_TAXI = [By.XPATH, '//button[text()="Вызвать такси"]']
BUTTON_TO_BOOK = [By.XPATH, '//button[text()="Забронировать"]']
BUTTON_ORDER_TAXI = [By.XPATH, '//span[text()="Ввести номер и заказать"]']
BUTTON_BOOK_AND_INPUT_LICENSE = [By.XPATH, '//span[text()="Ввести права и забронировать"]']
MODAL_SEARCH_CAR = [By.XPATH, '//div[text()="Поиск машины"]']

BUTTON_I_ACTIVE_TARIFF_TAXI = [By.XPATH, '//div[@class="tcard active"]/child::button[@class="i-button tcard-i active"]']
BUTTON_I_ACTIVE_TARIFF_WEEKEND = [By.XPATH, '//div[@class="tcard active"]/child::button[@class="i-button tcard-i active"]']


ACTIVE_TARIFF_TAXI = [By.XPATH, '//div[@class="tcard active"]/child::div[@class="tcard-title"]']
TAXI_TARIFF_WORK = [By.XPATH, '//div[contains(text(), "Рабочий")]']
TAXI_TARIFF_SLEEP = [By.XPATH, '//div[contains(text(), "Сонный")]']
TAXI_TARIFF_WEEKEND = [By.XPATH, '//div[contains(text(), "Отпускной")]']
TAXI_TARIFF_TALK = [By.XPATH, '//div[contains(text(), "Разговорчивый")]']
TAXI_TARIFF_COMFORT = [By.XPATH, '//div[contains(text(), "Утешительный")]']
TAXI_TARIFF_GLOSSY = [By.XPATH, '//div[contains(text(), "Глянцевый")]']

TOOLTIP_ACTIVE_TARIFF = [By.XPATH, '//div[@class="tcard active"]/child::div[@data-id="tooltip"]']
TEXT_ABOUT_ACTIVE_TARIFF = [By.XPATH, '//div[@class="tcard active"]/descendant::div[@class="i-dPrefix"]']

FORM_ORDER_TAXI = [By.XPATH, '//div[@class="form"]']
FIELD_PHONE = [By.XPATH, '//div[@class="form"]/descendant::div[text()="Телефон"]']
FIELD_PAY = [By.XPATH, '//div[@class="form"]/descendant::div[text()="Способ оплаты"]']
FIELD_COMMENT = [By.XPATH, '//div[@class="form"]/descendant::label[text()="Комментарий водителю..."]']
FIELD_REQUIREMENTS = [By.XPATH, '//div[@class="form"]/descendant::div[text()="Требования к заказу"]']

TOGGLE_TABLE_NOTEBOOK = [By.XPATH, '//span[@class="slider round"]']
ORDER_TAXI_READY = [By.XPATH, '//div[@class="order-subbody"]']

BUTTON_CANCEL = [By.XPATH, '//div[text()="Отменить"]/preceding-sibling::button[@class="order-button"]']
BUTTON_DETAIL = [By.XPATH, '//img[contains(@src, "burger")]']
TITLE_SEARCH_CAR = [By.XPATH, '//div[text()="Поиск машины"]']
TIME_SEARCH_CAR  = [By.XPATH, '//div[@class="order-header-time"]']

TITLE_COMPLITE_ORDER = [By.XPATH, '//div[text()=" мин. и приедет"]']
AVTO_NUMBER = [By.XPATH, '//div[@class="number"]']
IMG_TARIFF = [By.XPATH, '//img[@alt="Car"]']

RAIT_DRIVER = [By.XPATH, '//div[@class="order-btn-rating"]']
IMG_DRIVER = [By.XPATH, '//img[contains(@src, "bender")]']

NAME_DRIVER = [By.XPATH, '//div[@class="order-button"]/following-sibling::div']
DETAIL_COST_TARIF = [By.XPATH, '//div[contains(text(), "Стоимость")]']
COST_TARIF = [By.XPATH, '//div[@class="tcard active"]/child::div[@class="tcard-price"]']

MODAL_ORDER_CAR = [By.XPATH, '//div[@class="order-body"]']