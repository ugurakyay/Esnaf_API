import requests
import pytest

BASE_URL = "https://stage.easypointapi.com/api"  # API'nin temel URL'si

def test_login():
    url = f"{BASE_URL}/login"
    payload = {"username": "test", "password": "test"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_get_posts():
    url = f"{BASE_URL}/get-posts"
    response = requests.get(url)
    assert response.status_code == 200

def test_complete_order():
    url = f"{BASE_URL}/complete-order"
    payload = {"order_id": "12345"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_get_post_by_barcode():
    url = f"{BASE_URL}/get-post-by-barcode"
    payload = {"barcode": "123456789"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_create_post():
    url = f"{BASE_URL}/create-post"
    payload = {"title": "New Post", "content": "This is a new post"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_return():
    url = f"{BASE_URL}/return"
    payload = {"item_id": "12345"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_post_change_status():
    url = f"{BASE_URL}/post-change-status"
    payload = {"post_id": "12345", "status": "active"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_resend_code():
    url = f"{BASE_URL}/resend-code"
    payload = {"phone": "+1234567890"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_get_profile():
    url = f"{BASE_URL}/get-profile"
    response = requests.get(url)
    assert response.status_code == 200

def test_create_campaign():
    url = f"{BASE_URL}/create-campaign"
    payload = {"name": "New Campaign", "description": "This is a new campaign"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_get_campaign():
    url = f"{BASE_URL}/get-campaign"
    response = requests.get(url)
    assert response.status_code == 200

def test_update_profile():
    url = f"{BASE_URL}/update-profile"
    payload = {"user_id": "12345", "email": "newemail@example.com"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_send_code():
    url = f"{BASE_URL}/send-code"
    payload = {"phone": "+1234567890"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_get_malls():
    url = f"{BASE_URL}/get-malls"
    response = requests.get(url)
    assert response.status_code == 200

def test_get_locations():
    url = f"{BASE_URL}/get-locations"
    response = requests.get(url)
    assert response.status_code == 200

def test_set_in_branch():
    url = f"{BASE_URL}/set-in-branch"
    payload = {"branch_id": "12345"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

def test_get_users():
    url = f"{BASE_URL}/get-users"
    response = requests.get(url)
    assert response.status_code == 200

def test_get_users_types():
    url = f"{BASE_URL}/get-users-types"
    response = requests.get(url)
    assert response.status_code == 200

def test_fetch_easy_points():
    url = f"{BASE_URL}/fetch-easy-points"
    response = requests.get(url)
    assert response.status_code == 200

def test_delete_post():
    url = f"{BASE_URL}/delete-post"
    payload = {"post_id": "12345"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

if __name__ == "__main__":
    # Pytest komutunu çalıştır ve raporu HTML formatında oluştur
    pytest.main(["--html=report.html", "--self-contained-html"])
