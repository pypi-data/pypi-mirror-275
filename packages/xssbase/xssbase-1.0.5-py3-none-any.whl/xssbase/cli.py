# xssbase - A professional tool for scanning XSS vulnerabilities
# Author: Fidal
# Date: 2024
# License: MIT

import argparse
import sys
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from .main import test_xss_payloads
from .utils import download_chromedriver_windows, download_chromedriver_linux, download_chromedriver_mac

def main():
    parser = argparse.ArgumentParser(description="XSS testing tool")
    parser.add_argument('--url', required=True, help='URL to test for XSS vulnerability')
    args = parser.parse_args()

    system = platform.system()

    if system == 'Windows':
        download_chromedriver_windows()
        service = Service('chromedriver-win64/chromedriver.exe')
    elif system == 'Linux':
        download_chromedriver_linux()
        service = Service('chromedriver-linux64/chromedriver')
    elif system == 'Darwin':
        download_chromedriver_mac()
        service = Service('chromedriver-mac64/chromedriver')
    else:
        print(f"This tool does not support {system}.")
        sys.exit(1)

    driver = webdriver.Chrome(service=service)

    try:
        test_xss_payloads(driver, args.url)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
