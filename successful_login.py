# successful_login.py
import requests
from config import LOGIN_URL, USERNAME, PASSWORD

def test_successful_login():
    response = requests.post(LOGIN_URL, json={"username": USERNAME, "password": PASSWORD})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    test_successful_login()
