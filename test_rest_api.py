import requests   # module for working - sending HTTP requests to any site
import pytest

@pytest.fixture()
def obj_id():
    payload = {
        "name": "Intel Pentium ML9035",
        "data": {
            "year": 2026,
            "price": 2129.99,
            "CPU Model": "Intel Core I7",
            "Hard Disk size": "1 TB",
            "RAM": "32 GB"
        }
    }
    headers = {
        "Accept": "application/json",
        "x-api-key": "9593cd1f-875b-426a-9e85-2017f7b99d72"
    }
    response = requests.post("https://api.restful-api.dev/collections/test/objects/", json=payload,
                             headers=headers).json()
    return response['id']
def test_create_object():
    payload = {
        "name": "Intel Pentium ML9035",
        "data": {
            "year": 2026,
            "price": 2129.99,
            "CPU Model": "Intel Core I7",
            "Hard Disk size": "1 TB",
            "RAM": "32 GB"
        }
    }
    headers = {
        "Accept": "application/json",
        "x-api-key": "9593cd1f-875b-426a-9e85-2017f7b99d72"
    }
    response = requests.post("https://api.restful-api.dev/collections/test/objects/", json=payload, headers=headers).json()
    assert response['name'] == payload['name']

def test_read_object(obj_id):
    headers = {
        "Accept": "application/json",
        "x-api-key": "9593cd1f-875b-426a-9e85-2017f7b99d72"
    }
    response = requests.get(f"https://api.restful-api.dev/collections/test/objects/{obj_id}", headers=headers).json()
    print(response)


def test_update_object(obj_id):
    payload = {
        "name": "Apple MacBook Air 16",
        "data": {
            "year": 2024,
            "price": 1769.99,
            "CPU Model": "Intel Core I7",
            "Hard Disk size": "1 TB",
            "RAM": "16 GB"
        }
    }
    headers = {
        "Accept": "application/json",
        "x-api-key": "9593cd1f-875b-426a-9e85-2017f7b99d72"
    }
    response = requests.put(f"https://api.restful-api.dev/collections/test/objects/{obj_id}",
                            json=payload,headers=headers).json()
    print(response['name'], payload['name'])
    assert response['name'] == payload['name']

def test_delete_object(obj_id):
    headers = {
        "Accept": "application/json",
        "x-api-key": "9593cd1f-875b-426a-9e85-2017f7b99d72"
    }
    response = requests.delete(f"https://api.restful-api.dev/collections/test/objects/{obj_id}", headers=headers)
    assert response.status_code == 200
    response = requests.get(f"https://api.restful-api.dev/collections/test/objects/{obj_id}", headers=headers)
    assert response.status_code == 404
