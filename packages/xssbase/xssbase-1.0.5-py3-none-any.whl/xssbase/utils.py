# xssbase - A professional tool for scanning XSS vulnerabilities
# Author: Fidal
# Date: 2024
# License: MIT

import os
import requests
import zipfile
import tarfile

def download_and_extract(url, extract_to):
    response = requests.get(url)
    zip_path = os.path.join(extract_to, 'chromedriver.zip')

    with open(zip_path, 'wb') as file:
        file.write(response.content)

    if zip_path.endswith('.zip'):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    elif zip_path.endswith('.tar.gz'):
        with tarfile.open(zip_path, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_to)

    os.remove(zip_path)

def download_chromedriver_windows():
    chromedriver_url = "https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/win64/chromedriver-win64.zip"
    chromedriver_exe_path = "chromedriver-win64/chromedriver.exe"
    if not os.path.exists(chromedriver_exe_path):
        print("Downloading chromedriver for Windows...")
        download_and_extract(chromedriver_url, '.')

def download_chromedriver_linux():
    chromedriver_url = "https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chromedriver-linux64.zip"
    chromedriver_exe_path = "chromedriver-linux64/chromedriver"
    if not os.path.exists(chromedriver_exe_path):
        print("Downloading chromedriver for Linux...")
        download_and_extract(chromedriver_url, '.')

def download_chromedriver_mac():
    chromedriver_url = "https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/mac-x64/chromedriver-mac64.zip"
    chromedriver_exe_path = "chromedriver-mac64/chromedriver"
    if not os.path.exists(chromedriver_exe_path):
        print("Downloading chromedriver for macOS...")
        download_and_extract(chromedriver_url, '.')
