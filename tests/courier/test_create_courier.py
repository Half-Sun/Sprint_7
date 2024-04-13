import helpers
import allure
from conftest import courier

class TestCreateCourier:

    @allure.title("Create courier - success")
    def test_create_courier_success(self):
        login = helpers.generate_random_string(10)
        password = helpers.generate_random_string(10)
        first_name = helpers.generate_random_string(10)
        response = helpers.register_new_courier(login, password, first_name)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Create duplicate courier")
    def test_create_duplicate_courier(self, courier):
        login, password, first_name = courier

        assert helpers.register_new_courier(login, password, first_name).status_code == 409
        assert (
                "Этот логин уже используется. Попробуйте другой."
                in helpers.register_new_courier(login, password, first_name).json()["message"]
        )

    @allure.title("Create courier without login")
    def test_create_courier_without_login(self):
        password = helpers.generate_random_string(10)
        first_name = helpers.generate_random_string(10)

        assert helpers.register_new_courier("", password, first_name).status_code == 400
        assert (
                "Недостаточно данных для создания учетной записи"
                in helpers.register_new_courier("", password, first_name).json()["message"]
        )

    @allure.title("Create courier without password")
    def test_create_courier_without_password(self):
        login = helpers.generate_random_string(10)
        first_name = helpers.generate_random_string(10)

        assert helpers.register_new_courier(login, "", first_name).status_code == 400
        assert (
                "Недостаточно данных для создания учетной записи"
                in helpers.register_new_courier(login, "", first_name).json()["message"]
        )

    @allure.title("Create courier without first name")
    def test_create_courier_without_first_name(self):
        login = helpers.generate_random_string(10)
        password = helpers.generate_random_string(10)
        response = helpers.register_new_courier(login, password, "")

        assert response.status_code == 201
        assert response.json() == {"ok": True}