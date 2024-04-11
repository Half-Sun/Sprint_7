import allure
import requests


class TestOrderByTrack:

    @allure.title("Get order by track")
    def test_get_order_by_track_success(self):
        response = requests.get(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders/track",
            params={"t": "749612"},
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert "order" in response.json()
        assert isinstance(response.json()["order"], dict)

    @allure.title("Get order by track without track parameter")
    def test_get_order_by_track_no_track_param(self):
        response = requests.get(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders/track"
        )

        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title("Get order by track nonexistent order")
    def test_get_order_by_track_nonexistent_order(self):
        response = requests.get(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders/track",
            params={"t": "1234567890"},  # **Несуществующий номер заказа**
        )

        # Проверка ответа
        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Заказ не найден'}
