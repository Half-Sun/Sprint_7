from random import randint

from helpers import generate_random_string, register_new_courier
import requests
import allure
from data import LOGIN_URL, GET_COURIER_BY_ID_URL, DELETE_COURIER_URL


class TestDeleteCourier:

    @allure.title("Delete courier - success")
    def test_delete_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        register_new_courier(login, password, first_name)

        response = requests.post(
            LOGIN_URL,
            json={"login": login, "password": password},
        )
        courier_id = response.json()["id"]

        response = requests.delete(
            DELETE_COURIER_URL.format(courier_id)
        )

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Verify courier deletion")
    def test_verify_courier_deleted(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        register_new_courier(login, password, first_name)

        response = requests.post(
            LOGIN_URL,
            json={"login": login, "password": password},
        )
        courier_id = response.json()["id"]

        requests.delete(
            DELETE_COURIER_URL.format(courier_id)
        )

        response = requests.get(
            GET_COURIER_BY_ID_URL.format(courier_id)
        )
        assert response.status_code == 404

    @allure.title("Delete courier - unsuccessful")
    def test_delete_courier_unsuccessful(self):
        random_courier_id = randint(999999, 1000000)

        response = requests.delete(
            DELETE_COURIER_URL.format(random_courier_id)
        )

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}
