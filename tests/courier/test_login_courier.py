from conftest import courier
import requests
import allure
from data import BASE_URL, COURIER_REGISTER_URL, LOGIN_URL, GET_COURIER_BY_ID_URL, DELETE_COURIER_URL

class TestLoginCourier:



    @allure.title("Successful log in")
    def test_courier_login_success(self, courier):
        login, password, _ = courier
        response = requests.post(
            LOGIN_URL,
            json={"login": login, "password": password},
        )
        assert response.status_code == 200
        assert response.json()["id"] is not None


    @allure.title("Log in not all required fields are filled")
    def test_courier_login_required_fields(self):
        response = requests.post(
            LOGIN_URL,
            json={"password": "12345"},
        )
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

        response = requests.post(
            LOGIN_URL,
            json={"login": "test_login"},
        )
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title("Log in fails with invalid credentials")
    def test_login_fails_with_invalid_credentials(self, courier):
        login, password, _ = courier

        response = requests.post(
            LOGIN_URL,
            json={"login": "nonexistent_login", "password": password},
        )
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

        response = requests.post(
            LOGIN_URL,
            json={"login": login, "password": "wrong_password"},
        )
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
