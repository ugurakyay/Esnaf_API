import requests
import random
from datetime import datetime
import json
import pytest
import os

# API ve servis URL'leri
BASE_URL = "https://stage.easypointapi.com/api"
LOGIN_URL = f"{BASE_URL}/login"
GET_POSTS_URL = f"{BASE_URL}/posts/get"
COMPLETE_ORDER_URL = f"{BASE_URL}/posts/complete"

# Kullanıcı bilgileri
USERNAME = "easypoint@easypoint.com.tr"
PASSWORD = "935105"

# Rapor dosyasının yolunu belirleyin
REPORT_FILE_PATH = "report.txt"

# Rapor dosyasını her çalışmada sıfırla
def initialize_report():
    with open(REPORT_FILE_PATH, "w") as report_file:
        report_file.write(f"Rapor Başlangıcı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Mesajları rapora ekle
def log_report(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPORT_FILE_PATH, "a") as report_file:
        report_file.write(f"[{timestamp}] {message}\n")

# Token al
def get_token():
    login_data = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(LOGIN_URL, json=login_data)

    # Hata kontrolü
    if response.status_code != 200:
        log_report(f"Login isteği başarısız oldu: {response.status_code} - {response.text}")
        raise Exception(f"Login isteği başarısız oldu: {response.status_code} - {response.text}")

    response_json = response.json()
    result = response_json.get("result", {})
    token = result.get("token")

    if not token:
        log_report(f"Token alınamadı: {response_json}")
        raise Exception(f"Token alınamadı: {response_json}")

    log_report(f"Login token alındı: {token}")
    return token

# Servise istek at
def call_service(token, url, data=None, method="GET"):
    headers = {"Authorization": f"Bearer {token}"}
    if method == "GET":
        response = requests.get(url, headers=headers)
    else:  # POST method
        response = requests.post(url, json=data, headers=headers)

    response.raise_for_status()  # Hata kontrolü

    # Cevabın JSON formatında olup olmadığını kontrol edin
    try:
        response_json = response.json()
    except ValueError:
        log_report(f"Geçersiz JSON cevabı alındı: {response.text}")
        raise

    log_report(f"{url} servisine istek atıldı. Cevap: {response.status_code} - {response_json}")
    return response_json

def main():
    # Raporu sıfırla
    initialize_report()

    try:
        # 1. Login token al
        token = get_token()

        # 2. Get Posts servisine istek at
        get_posts_body = {
            "status": [5],
            "limit": 3
        }
        posts_response = call_service(token, GET_POSTS_URL, data=get_posts_body, method="POST")

        # 3. result içinde "dataEntranceType" "Hepsiburada API" olanları filtrele ve rastgele bir tane seç
        result = posts_response.get("result", [])
        if not isinstance(result, list):
            log_report(f"Beklenen formatta olmayan yanıt: {posts_response}")
            return

        hepsiburada_posts = [post for post in result if post.get("dataEntranceType") == "Hepsiburada API"]
        if not hepsiburada_posts:
            log_report("Hepsiburada API'ye ait post bulunamadı.")
            return

        selected_post = random.choice(hepsiburada_posts)
        selected_post_id = selected_post.get("id")
        verification_code = selected_post.get("deliveryPassword")

        log_report(f"Seçilen ID: {selected_post_id}, Verification Code: {verification_code}")

        # 4. Complete Order servisine istek at
        complete_order_body = {
            "postID": selected_post_id,
            "otpType": "EasypointOTP",
            "otp": verification_code
        }

        # Log the request details
        log_report(f"Complete Order servisine istek atılıyor: {json.dumps(complete_order_body, indent=2)}")

        final_response = call_service(token, COMPLETE_ORDER_URL, data=complete_order_body, method="POST")

        # Log the response details
        log_report(f"Son istekten dönen cevap: {json.dumps(final_response, indent=2)}")

        # Log the ID and OTP used
        log_report(f"Complete servisinde kullanılan postID: {selected_post_id}, otp: {verification_code}")

    except Exception as e:
        log_report(f"Hata: {str(e)}")
        raise e

if __name__ == "__main__":
    main()

# Test fonksiyonu
def test_main():
    try:
        main()
    except Exception as e:
        pytest.fail(f"Test başarısız oldu: {str(e)}")
