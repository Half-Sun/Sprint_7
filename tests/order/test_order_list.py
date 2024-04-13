from requests import Response
from helpers import generate_random_string, register_new_courier
import requests
import allure
from random import randint
from data import GET_ORDERS_URL, LOGIN_URL


class TestOrderList:

    @allure.title("Get orders success")
    def test_get_orders_success(self):
        response = requests.get(
            GET_ORDERS_URL
        )
        assert response.status_code == 200
        assert "orders" in response.json()
        assert "pageInfo" in response.json()
        assert "availableStations" in response.json()

    @allure.title("Get orders with nonexistent courier id")
    def test_get_orders_with_nonexistent_courier_id(self):
        random_courier_id = randint(1, 1000000)

        response = requests.get(
            f"{GET_ORDERS_URL}?courierId={random_courier_id}"
        )

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': f'Курьер с идентификатором {random_courier_id} не найден'}

    @allure.title("Get orders with courier id")
    def test_get_orders_with_courier_id(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        register_new_courier(login, password, first_name)

        response = requests.post(
            LOGIN_URL,
            json={"login": login, "password": password},
        )
        courier_id = response.json()["id"]

        response: Response = requests.get(
             f"{GET_ORDERS_URL}?courierId={courier_id}"
        )

        assert response.status_code == 200
        assert "orders" in response.json()
        assert "pageInfo" in response.json()
        assert "availableStations" in response.json()
