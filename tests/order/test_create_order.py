import pytest
from requests import Response
import requests
import allure
from data import CREATE_ORDER_URL, TEST_DATA


class TestCreateOrder:

    @allure.title("Order created with parametrize")
    @pytest.mark.parametrize(
        "first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color",
        TEST_DATA
    )
    def test_create_order(
            self,
            first_name,
            last_name,
            address,
            metro_station,
            phone,
            rent_time,
            delivery_date,
            comment,
            color,
    ):
        response: Response = requests.post(
            CREATE_ORDER_URL,  # Using the imported URL
            json={
                "firstName": first_name,
                "lastName": last_name,
                "address": address,
                "metroStation": metro_station,
                "phone": phone,
                "rentTime": rent_time,
                "deliveryDate": delivery_date,
                "comment": comment,
                "color": color,
            },
        )

        assert response.status_code == 201
        assert response.json()["track"] is not None

    @allure.title("Order created with one color")
    def test_create_order_with_one_color(self):
        response: Response = requests.post(
            CREATE_ORDER_URL,
            json={
                "firstName": "Иван",
                "lastName": "Иванов",
                "address": "Москва, ул. Ленина, 1",
                "metroStation": "Площадь Восстания",
                "phone": "+7 900 123 45 67",
                "rentTime": 5,
                "deliveryDate": "2023-12-01",
                "comment": "",
                "color": ["BLACK"],
            },
        )

        assert response.status_code == 201
        assert response.json()["track"] is not None

    @allure.title("Order created with two colors")
    def test_create_order_with_two_colors(self):
        response: Response = requests.post(
            CREATE_ORDER_URL,
            json={
                "firstName": "Иван",
                "lastName": "Иванов",
                "address": "Москва, ул. Ленина, 1",
                "metroStation": "Площадь Восстания",
                "phone": "+7 900 123 45 67",
                "rentTime": 5,
                "deliveryDate": "2023-12-01",
                "comment": "",
                "color": ["BLACK", "GREY"],
            },
        )

        assert response.status_code == 201
        assert response.json()["track"] is not None

    @allure.title("Order created without color")
    def test_create_order_without_color(self):
        response: Response = requests.post(
            CREATE_ORDER_URL,
            json={
                "firstName": "Иван",
                "lastName": "Иванов",
                "address": "Москва, ул. Ленина, 1",
                "metroStation": "Площадь Восстания",
                "phone": "+7 900 123 45 67",
                "rentTime": 5,
                "deliveryDate": "2023-12-01",
                "comment": "",
            },
        )

        assert response.status_code == 201
        assert response.json()["track"] is not None
