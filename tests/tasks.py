default_path = "/tasks"


def test_get_all_task(client, authentication_header):
    response = client.get(default_path, headers=authentication_header)
    assert response.status == "200 OK"
    assert response.json == []


def test_create_task(client, authentication_header):
    response = client.post(default_path, headers=authentication_header,
                           json={"title": "test"})

    assert response.status == "201 CREATED"

    response_get = client.get(default_path, headers=authentication_header)
    assert response_get.status == "200 OK"
    assert response_get.json[0]['title'] == "test"


def test_update_task(client, authentication_header):
    _ = client.post(default_path, headers=authentication_header,
                    json={"title": "test"})
    response_get = client.get(default_path, headers=authentication_header)
    assert response_get.status == "200 OK"
    assert response_get.json[0]['title'] == "test"

    response = client.put(f'{default_path}/{response_get.json[0]["id"]}',
                          headers=authentication_header,
                          json={"title": "test 1"})
    assert response.status == "200 OK"

    response_get = client.get(default_path, headers=authentication_header)
    assert response_get.status == "200 OK"
    assert response_get.json[0]['title'] == "test 1"


def test_delete_task(client, authentication_header):
    created = client.post(default_path, headers=authentication_header,
                          json={"title": "test"})
    assert created.status == "201 CREATED"

    response_get = client.get(default_path, headers=authentication_header)
    assert response_get.status == "200 OK"
    assert response_get.json[0]['title'] == "test"

    response = client.delete(f'{default_path}/{response_get.json[0]["id"]}',
                             headers=authentication_header)
    assert response.status == "200 OK"

    response_get = client.get(default_path, headers=authentication_header)
    assert response_get.status == "200 OK"
    assert response_get.json == []
