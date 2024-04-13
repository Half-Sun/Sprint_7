import requests
import random
import string
import allure


@allure.step("Generate new courier and return credentials")
def register_new_courier_and_return_login_password():
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
        return login, password, first_name
    else:
        return None  # Or handle the error more specifically


@allure.step("Generate courier credential")
def generate_courier_credentials():  # Removed 'self' as it's not a class method
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

@allure.step("Delete courier")
def delete_courier(courier_id):
    response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
    return response


@allure.step("Generate random string")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))
