import requests

def test_user_list():
    response = requests.get("https://dummyjson.com/test")
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "ok" 
