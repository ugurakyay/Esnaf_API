# empty_username_password_login.py
import requests
from config import LOGIN_URL

def test_empty_username_password_login():
    response = requests.post(LOGIN_URL, json={"username": "", "password": ""})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    test_empty_username_password_login()
