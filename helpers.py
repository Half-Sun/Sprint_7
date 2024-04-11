import requests
import random
import string
import allure


@allure.step("Generate new courier and return credentials")
def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

@allure.step("Generate courier credential")
def generate_courier_credentials(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        return login, password
@allure.step("Register new courier")
def register_new_courier(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name,
    }
    response = requests.post(
        "https://qa-scooter.praktikum-services.ru/api/v1/courier", json=payload
    )
    return response

@allure.step("Generate random string")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


@allure.step("Generate unique login")
def generate_unique_login():
    login = generate_random_string(10)
    while requests.get(
            f"https://qa-scooter.praktikum-services.ru/api/v1/couriers/login/{login}"
    ).status_code == 200:
        login = generate_random_string(10)
    return login

@allure.step("Delete courier")
def delete_courier(courier_id):
    response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
    return response

def get_random_order():
    """Возвращает случайный доступный заказ.

    Returns:
        tuple: (order_id, order_data)
    """

    while True:
        # Генерируем случайный номер заказа
        order_id = random.randint(100000, 999999)

        # Проверяем существование заказа
        response = requests.get(
            f"https://qa-scooter.praktikum-services.ru/api/v1/orders/{order_id}"
        )

        if response.status_code != 200:
            # Заказ не существует, переходим кгенерации нового ID
            continue

        # Проверяем доступность заказа
        order_data = response.json()
        if order_data["status"] != "new":
            # Заказ занят, переходим кгенерации нового ID
            continue

        # Заказ найден, возвращаем данные
        return order_id, order_data
