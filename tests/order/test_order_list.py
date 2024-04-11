from requests import Response
from helpers import generate_unique_login, generate_random_string, register_new_courier
import requests
import allure


class TestOrderList:

    @allure.title("Get orders success")
    def test_get_orders_success(self):
        response: Response = requests.get(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders"
        )

        assert response.status_code == 200
        assert "orders" in response.json()
        assert "pageInfo" in response.json()
        assert "availableStations" in response.json()

    @allure.title("Get orders with nonexistent courier id")
    def test_get_orders_with_nonexistent_courier_id(self):
        response: Response = requests.get(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId=12345"
        )
        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Курьер с идентификатором 12345 не найден'}

    @allure.title("Get orders with courier id")
    def test_get_orders_with_courier_id(self):
        login = generate_unique_login()
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        register_new_courier(login, password, first_name)

        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
            json={"login": login, "password": password},
        )
        courier_id = response.json()["id"]

        response: Response = requests.get(
            f"https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId={courier_id}"
        )

        assert response.status_code == 200
        assert "orders" in response.json()
        assert "pageInfo" in response.json()
        assert "availableStations" in response.json()



