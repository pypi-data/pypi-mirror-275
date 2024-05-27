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

    # Define the argument parser
    parser = argparse.ArgumentParser(
        description="XSSbase - A professional tool for scanning XSS vulnerabilities.",
        epilog="Author: Fidal\nGitHub: https://github.com/mr-fidal\n\n"
               "Copyright 2024 Fidal. All rights reserved. "
               "Unauthorized copying of this tool, via any medium is strictly prohibited."
    )
    parser.add_argument('--url', help='URL to test for XSS vulnerability')
    parser.add_argument('--payload', help='File containing XSS payloads to test')
    parser.add_argument('--payload-list', action='store_true', help='Print the payload list URL')

    args = parser.parse_args()

    # Print the payload list URL if the --payload-list command is used
    if args.payload_list:
        print("payload list : https://mrfidal.in/cyber-security/xssbase/payload-list.html")
        sys.exit(0)

    if not args.url:
        print("The --url argument is required.")
        sys.exit(1)

    # Download the chromedriver if it doesn't exist
    download_chromedriver()

    # Set up Chrome WebDriver
    service = Service('chromedriver-win64/chromedriver.exe')  # Specify the path to chromedriver executable
    driver = webdriver.Chrome(service=service)

    try:
        # Test XSS payloads
        test_xss_payloads(driver, args.url, args.payload)
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
