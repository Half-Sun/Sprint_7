import pytest
from helpers import register_new_courier_and_return_login_password, delete_courier
import requests
import allure


class TestLoginCourier:

    @pytest.fixture
    def courier(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        yield login, password
        delete_courier(login)  # Убедитесь, что вы удаляете курьера

    @allure.title("Successful log in")
    def test_courier_login_success(self, courier):
        login, password = courier

        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
            json={"login": login, "password": password},
        )

        assert response.status_code == 200
        assert response.json()["id"] is not None


    @allure.title("Log in not all required fields are filled")
    def test_courier_login_required_fields(self):
        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
            json={"password": "12345"},
        )
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
            json={"login": "test_login"},
        )
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title("Log in fails with invalid credentials")
    def test_login_fails_with_invalid_credentials(self, courier):
        login, password = courier

        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
            json={"login": "nonexistent_login", "password": password},
        )
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
            json={"login": login, "password": "wrong_password"},
        )
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
