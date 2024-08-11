import pytest
from datetime import datetime

# Rapor dosyası yolu
REPORT_FILE_PATH = "report.txt"

@pytest.fixture(scope="session", autouse=True)
def reset_report():
    # Rapor dosyasını sıfırla
    with open(REPORT_FILE_PATH, "w") as report_file:
        report_file.write(f"Rapor Başlangıcı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

@pytest.fixture
def log_report():
    def _log_report(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(REPORT_FILE_PATH, "a") as report_file:
            report_file.write(f"[{timestamp}] {message}\n")
    return _log_report
