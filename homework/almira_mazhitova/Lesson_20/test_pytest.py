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


@pytest.mark.critical
@pytest.mark.parametrize(
    'name, color, size',
    [
        ('Valya', 'yellow', 'big'),
        ('Malya', 'blue', 'small'),
        ('Balya', 'green', 'medium')
    ],
    ids=["name", "color", "size"],
)
def test_create_object(setup_teardown_session, setup_teardown_function, name, color, size):
    body = {
        "name": name,
        "data": {
            "color": color,
            "size": size
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    ).json()

    assert response.get("data") == body.get("data")
    assert response.get("name") == body.get("name")


@pytest.mark.medium
def test_update_object_put(setup_teardown_session, setup_teardown_function, create_and_delete_new_object):
    new_object = create_and_delete_new_object
    new_object_id = new_object.get("id")
    body = {
        "name": create_and_delete_new_object.get("name")[:-2] + "ek",
        "data": {
            "color": "dark " + create_and_delete_new_object.get("data").get("color"),
            "size": create_and_delete_new_object.get("data").get("size") + "er"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    ).json()

    assert response.get("data") == body.get("data")
    assert response.get("name") == body.get("name")


def test_update_object_patch_name(setup_teardown_session, setup_teardown_function, create_and_delete_new_object):
    new_object = create_and_delete_new_object
    new_object_id = new_object.get("id")
    body = {
        "name": new_object.get("name")[:-2] + "issa",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    ).json()

    assert response.get("name") == body.get("name")


def test_update_object_patch_data(setup_teardown_session, setup_teardown_function, create_and_delete_new_object):
    new_object = create_and_delete_new_object
    new_object_id = new_object.get("id")
    body = {
        "data": {
            "color": "light " + new_object.get("data").get("color"),
            "size": new_object.get("data").get("size")
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    ).json()

    assert response.get("data") == body.get("data")


def test_delete_object(setup_teardown_session, setup_teardown_function, create_and_delete_new_object):
    new_object = create_and_delete_new_object
    new_object_id = new_object.get("id")
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}'
    )

    assert response.status_code == 200, 'State code is not 200, object dont deleted!'
