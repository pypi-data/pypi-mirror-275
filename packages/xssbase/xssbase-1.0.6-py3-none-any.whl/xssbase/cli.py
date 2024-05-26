import argparse
import os
import sys
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from .main import test_xss_payloads
from .utils import download_chromedriver

def main():
    # Check if the operating system is Windows
    if platform.system() != 'Windows':
        print("This tool only supports Windows.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="XSS testing tool")
    parser.add_argument('--url', required=True, help='URL to test for XSS vulnerability')
    args = parser.parse_args()

    # Download the chromedriver if it doesn't exist
    download_chromedriver()

    # Set up Chrome WebDriver
    service = Service('chromedriver-win64/chromedriver.exe')  # Specify the path to chromedriver executable
    driver = webdriver.Chrome(service=service)

    try:
        # Test XSS payloads
        test_xss_payloads(driver, args.url)
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
