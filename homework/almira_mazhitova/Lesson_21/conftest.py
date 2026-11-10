import pytest
import random
import requests


@pytest.fixture(scope='session')
def setup_teardown_session():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def setup_teardown_function():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def create_and_delete_new_object():
    names_list = ['Valya', 'Malya', 'Balya', 'Galya', 'Zalya', 'Nalya', 'Balya', 'Salya', 'Talya', 'Kalya']
    colors_list = ['white', 'black', 'grey', 'yellow', 'blue', 'green', 'pink', 'red', 'purple']
    sizes_list = ['big', 'small', 'medium', 'huge']
    body = {
        "name": random.choice(names_list),
        "data": {
            "color": random.choice(colors_list),
            "size": random.choice(sizes_list)
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    ).json()

    yield response
    created_object_id = response.get("id")
    object_exist = requests.get(f'http://objapi.course.qa-practice.com/object/{created_object_id}')
    if object_exist.status_code == 200:
        requests.delete(
            f'http://objapi.course.qa-practice.com/object/{created_object_id}'
        )
