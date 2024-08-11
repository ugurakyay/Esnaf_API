# empty_username_login.py
import requests
from config import LOGIN_URL, PASSWORD

def test_empty_username_login():
    response = requests.post(LOGIN_URL, json={"username": "", "password": PASSWORD})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    test_empty_username_login()
