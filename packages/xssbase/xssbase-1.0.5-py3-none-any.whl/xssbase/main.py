# xssbase - A professional tool for scanning XSS vulnerabilities
# Author: Fidal
# Date: 2024
# License: MIT

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=\"javascript:alert('XSS');\">",
    "<svg/onload=alert('XSS')>"
]

def test_xss_payloads(driver, url):
    try:
        driver.get(url)
        original_url = driver.current_url

        for payload in xss_payloads:
            input_element = driver.find_element(By.XPATH, "//input[@type='text']")
            input_element.clear()
            input_element.send_keys(payload)
            input_element.send_keys(Keys.ENTER)
            time.sleep(2)
            current_url = driver.current_url
            if current_url != original_url:
                print("Potential XSS vulnerability detected!")
                print("Original URL:", original_url)
                print("Current URL:", current_url)
                break
    except Exception as e:
        print("Error occurred:", str(e))
