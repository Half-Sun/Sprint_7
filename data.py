# Данные для теста
TEST_DATA = [
    (
        "Иван",
        "Иванов",
        "Москва, ул. Ленина, 1",
        "Площадь Восстания",
        "+7 900 123 45 67",
        5,
        "2023-12-01",
        "Привезти в красной машине",
        ["RED"],
    ),
    (
        "Петр",
        "Петров",
        "Санкт-Петербург, Невский пр., 100",
        "Гостиный двор",
        "+7 911 234 56 78",
        3,
        "2023-12-05",
        "",
        [],
    ),
]

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

COURIER_REGISTER_URL = f"{BASE_URL}/courier"
LOGIN_URL = f"{BASE_URL}/courier/login"
GET_COURIERS_URL = f"{BASE_URL}/couriers"
GET_COURIER_BY_ID_URL = f"{BASE_URL}/courier/{{}}"
DELETE_COURIER_URL = f"{BASE_URL}/courier/{{}}"
CREATE_ORDER_URL = f"{BASE_URL}/orders"
GET_ORDER_BY_TRACK_URL = f"{BASE_URL}/orders/track"
GET_ORDERS_URL = f"{BASE_URL}/orders"