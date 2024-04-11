import pytest
import helpers
import requests
import allure


class TestCreateCourier:

    @pytest.fixture
    def courier(self):
        login, password, first_name = helpers.register_new_courier_and_return_login_password()
        yield login, password, first_name
        helpers.delete_courier(login)

    @allure.title("Create courier - success")
    def test_create_courier_success(self):
        login = helpers.generate_unique_login()
        password = helpers.generate_random_string(10)
        first_name = helpers.generate_random_string(10)
        response = helpers.register_new_courier(login, password, first_name)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Create unique courier - success")
    def test_create_unique_courier_success(self, courier):
        login, password, first_name = courier

        response = requests.get(
            f"https://qa-scooter.praktikum-services.ru/api/v1/couriers/login/{login}"
        )
        assert response.status_code == 404

    @allure.title("Create duplicate courier")
    def test_create_duplicate_courier(self, courier):
        login, password, first_name = courier

        response = helpers.register_new_courier(login, password, first_name)

        assert response.status_code == 409
        assert (
                "Этот логин уже используется. Попробуйте другой."
                in response.json()["message"]
        )

    @allure.title("Create courier without login")
    def test_create_courier_without_login(self, courier):
        _, password, first_name = courier

        response = helpers.register_new_courier("", password, first_name)

        assert response.status_code == 400
        assert (
                "Недостаточно данных для создания учетной записи"
                in response.json()["message"]
        )

    @allure.title("Create courier without password")
    def test_create_courier_without_password(self, courier):
        login, _, first_name = courier

        response = helpers.register_new_courier(login, "", first_name)

        assert response.status_code == 400
        assert (
                "Недостаточно данных для создания учетной записи"
                in response.json()["message"]
        )

    @allure.title("Create courier without first name")
    def test_create_courier_without_first_name(self, courier):
        login = helpers.generate_unique_login()
        password = helpers.generate_random_string(10)
        response = helpers.register_new_courier(login, password, "")

        assert response.status_code == 201
        assert response.json() == {"ok": True}