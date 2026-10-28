import random
import requests

def get_all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    assert len(response) >= 0, 'No objects!'


def get_object_by_id(object_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{id}').json()
    assert response.get("id") == object_id, "Id in response != expected_id"


def create_and_return_new_object_info():
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
        f'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    ).json()

    # print(f"created_response={response}")

    return response


def create_object():
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
        f'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    ).json()

    # print(f"created_response={response}")

    assert response.get("data") == body.get("data")
    assert response.get("name") == body.get("name")


def update_object_put():
    new_object = create_and_return_new_object_info()
    new_object_id = new_object.get("id")
    body = {
        "name": new_object.get("name")[:-2] + "ek",
        "data": {
            "color": "dark " + new_object.get("data").get("color"),
            "size": new_object.get("data").get("size") + "er"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    ).json()

    # print(f"put_update_response={response}")

    assert response.get("data") == body.get("data")
    assert response.get("name") == body.get("name")


def update_object_patch_name():
    new_object = create_and_return_new_object_info()
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

    # print(f"patch_update_name_response={response}")

    assert response.get("name") == body.get("name")



def update_object_patch_data():
    new_object = create_and_return_new_object_info()
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

    # print(f"patch_update_data_response={response}")

    assert response.get("data") == body.get("data")


def delete_object():
    new_object = create_and_return_new_object_info()
    new_object_id = new_object.get("id")
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}'
    )
    # print(f"delete_response={response}")

    assert response.status_code == 200, 'State code is not 200, object dont deleted!'


create_object()
update_object_patch_name()
update_object_patch_data()
delete_object()
