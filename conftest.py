import pytest
import helpers
@pytest.fixture(scope='function')
def courier():
    login, password, first_name = helpers.register_new_courier_and_return_login_password()
    yield login, password, first_name
    helpers.delete_courier(login)