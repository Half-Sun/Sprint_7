from helpers import generate_unique_login, generate_random_string, register_new_courier
import requests
import allure


class TestDeleteCourier:

    @allure.title("Delete courier - success")
    def test_delete_courier_success(self):
        login = generate_unique_login()
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        register_new_courier(login, password, first_name)

        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
            json={"login": login, "password": password},
        )
        courier_id = response.json()["id"]

        response = requests.delete(
            f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}"
        )

        assert response.status_code == 200
        assert response.json() == {"ok": True}

        response = requests.get(
            f"https://qa-scooter.praktikum-services.ru/api/v1/couriers/{courier_id}"
        )
        assert response.status_code == 404

    @allure.title("Delete courier -unsuccessful")
    def test_delete_courier_unsuccessful(self):
        courier_id = 12345

        response = requests.delete(
            f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}"
        )

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}

