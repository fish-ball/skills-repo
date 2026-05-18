import os
import requests

def check_proxy():
    proxy = os.getenv("https_proxy")
    print(f"Current https_proxy: {proxy}")
    try:
        response = requests.get("https://www.google.com", proxies={"https": proxy}, timeout=5)
        print(f"Connection to google.com status: {response.status_code}")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    check_proxy()
