import allure
import pytest
import requests


@allure.feature('Posts')
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
@allure.feature('Posts')
@allure.story('Create')
@allure.title('Создание поста')
def test_create_object(setup_teardown_session, setup_teardown_function, name, color, size):

    with allure.step('Генерируем body'):
        body = {
            "name": name,
            "data": {
                "color": color,
                "size": size
            }
        }
    with allure.step('Создаем headers'):
        headers = {'Content-Type': 'application/json'}

    with allure.step('Выполняем POST-запрос'):
        response = requests.post(
            'http://objapi.course.qa-practice.com/object',
            json=body,
            headers=headers
        ).json()
        
    with allure.step('Проверяем data полученного ответа'):
        assert response.get("data") == body.get("data")

    with allure.step('Проверяем name полученного ответа'):
        assert response.get("name") == body.get("name")


@allure.feature('Posts')
@allure.story('Update')
@allure.title('Изменение поста методом PUT')
@pytest.mark.medium
def test_update_object_put(setup_teardown_session, setup_teardown_function, create_and_delete_new_object):
    with allure.step('Получаем ответ на создание нового поста из предусловия'):
        new_object = create_and_delete_new_object
        
    with allure.step('Получаем id созданного поста'):
        new_object_id = new_object.get("id")

    with allure.step('Генерируем body для изменения созданного поста'):
        body = {
            "name": create_and_delete_new_object.get("name")[:-2] + "ek",
            "data": {
                "color": "dark " + create_and_delete_new_object.get("data").get("color"),
                "size": create_and_delete_new_object.get("data").get("size") + "er"
            }
        }

    with allure.step('Создаем headers'):
        headers = {'Content-Type': 'application/json'}

    with allure.step('Выполняем PUT-запрос'):
        response = requests.put(
            f'http://objapi.course.qa-practice.com/object/{new_object_id}',
            json=body,
            headers=headers
        ).json()

    with allure.step('Проверяем data полученного ответа'):
        assert response.get("data") == body.get("data")

    with allure.step('Проверяем name полученного ответа'):
        assert response.get("name") == body.get("name")


@allure.feature('Posts')
@allure.story('Update')
@allure.title('Изменение поста методом PATCH (поле name)')
def test_update_object_patch_name(setup_teardown_session, setup_teardown_function, create_and_delete_new_object):
    with allure.step('Получаем ответ на создание нового поста из предусловия'):
        new_object = create_and_delete_new_object

    with allure.step('Получаем id созданного поста'):
        new_object_id = new_object.get("id")

    with allure.step('Генерируем body для изменения созданного поста'):
        body = {
            "name": new_object.get("name")[:-2] + "issa",
        }

    with allure.step('Создаем headers'):
        headers = {'Content-Type': 'application/json'}

    with allure.step('Выполняем PATCH-запрос'):
        response = requests.patch(
            f'http://objapi.course.qa-practice.com/object/{new_object_id}',
            json=body,
            headers=headers
        ).json()

    with allure.step('Проверяем name полученного ответа'):
        assert response.get("name") == body.get("name")


@allure.feature('Posts')
@allure.story('Update')
@allure.title('Изменение поста методом PATCH (поле data)')
def test_update_object_patch_data(setup_teardown_session, setup_teardown_function, create_and_delete_new_object):
    with allure.step('Получаем ответ на создание нового поста из предусловия'):
        new_object = create_and_delete_new_object

    with allure.step('Получаем id созданного поста'):
        new_object_id = new_object.get("id")

    with allure.step('Генерируем body для изменения созданного поста'):
        body = {
            "data": {
                "color": "light " + new_object.get("data").get("color"),
                "size": new_object.get("data").get("size")
            }
        }

    with allure.step('Создаем headers'):
        headers = {'Content-Type': 'application/json'}

    with allure.step('Выполняем PATCH-запрос'):
        response = requests.patch(
            f'http://objapi.course.qa-practice.com/object/{new_object_id}',
            json=body,
            headers=headers
        ).json()

    with allure.step('Проверяем name полученного ответа'):
        assert response.get("data") == body.get("data")


@allure.feature('Posts')
@allure.story('Delete')
@allure.title('Удаление поста')
def test_delete_object(setup_teardown_session, setup_teardown_function, create_and_delete_new_object):
    with allure.step('Получаем ответ на создание нового поста из предусловия'):
        new_object = create_and_delete_new_object

    with allure.step('Получаем id созданного поста'):
        new_object_id = new_object.get("id")

    with allure.step('Выполняем DELETE-запрос'):
        response = requests.delete(
            f'http://objapi.course.qa-practice.com/object/{new_object_id}'
        )
    with allure.step('Проверяем status_code полученного ответа'):
        assert response.status_code == 300, 'State code is not 200, object dont deleted!'
