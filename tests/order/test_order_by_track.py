from random import random
import random
import allure
import requests
from data import GET_ORDER_BY_TRACK_URL


class TestOrderByTrack:

    @allure.title("Get order by track")
    def test_get_order_by_track_success(self):
        response = requests.get(
            GET_ORDER_BY_TRACK_URL,
            params={"t": "749612"},
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert "order" in response.json()
        assert isinstance(response.json()["order"], dict)

    @allure.title("Get order by track without track parameter")
    def test_get_order_by_track_no_track_param(self):
        response = requests.get(
            GET_ORDER_BY_TRACK_URL
        )

        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title("Get order by track nonexistent order")
    def test_get_order_by_track_nonexistent_order(self):
        random_track_id = random.randint(8888, 99999)
        response = requests.get(
            GET_ORDER_BY_TRACK_URL,
            params={"t": random_track_id},
        )

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Заказ не найден'}
