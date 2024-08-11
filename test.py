import pytest
from complete_order import execute_order
from conftest import REPORT_FILE_PATH
from successful_login import test_successful_login
from wrong_password_login import test_wrong_password_login
from empty_username_login import test_empty_username_login
from empty_password_login import test_empty_password_login
from empty_username_password_login import test_empty_username_password_login
from datetime import datetime
import json

# Define a fixture to initialize the report file before each test session
@pytest.fixture(scope="session", autouse=True)
def initialize_report():
    with open(REPORT_FILE_PATH, 'w') as report_file:
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        report_file.write(f"Rapor Başlangıcı: {start_time}\n")

def log_report(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPORT_FILE_PATH, "a") as report_file:
        report_file.write(f"[{timestamp}] {message}\n")

def test_complete_order_scenario():
    try:
        execute_order()
    except Exception as e:
        pytest.fail(f"Complete Order test başarısız oldu: {str(e)}")

def test_successful_login_scenario():
    test_successful_login()

def test_wrong_password_login_scenario():
    test_wrong_password_login()

def test_empty_username_login_scenario():
    test_empty_username_login()

def test_empty_password_login_scenario():
    test_empty_password_login()

def test_empty_username_password_login_scenario():
    test_empty_username_password_login()
