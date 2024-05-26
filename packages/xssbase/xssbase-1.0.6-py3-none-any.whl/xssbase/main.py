from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import os

# Define XSS payloads to test
xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=\"javascript:alert('XSS');\">",
    "<svg/onload=alert('XSS')>"
    # Add more payloads here
]

# Function to inject XSS payloads and check for potential vulnerabilities
def test_xss_payloads(driver, url):
    try:
        driver.get(url)
        original_url = driver.current_url

        for payload in xss_payloads:
            # Locate the input field and inject payload
            try:
                input_element = driver.find_element(By.XPATH, "//input[@type='text']")
            except Exception:
                print("Could not find the input field with XPath //input[@type='text']")
                print("Trying with a different selector...")
                try:
                    input_element = driver.find_element(By.TAG_NAME, "input")
                except Exception:
                    print("Could not find any input field.")
                    print("Page source for debugging:")
                    print(driver.page_source)
                    return

            input_element.clear()
            input_element.send_keys(payload)
            input_element.send_keys(Keys.ENTER)

            # Check if URL changes due to payload injection
            time.sleep(2)  # Allow time for potential alert boxes to appear
            current_url = driver.current_url

            # Check for alert boxes
            try:
                alert = driver.switch_to.alert
                print(f"Alert detected with payload: {payload}")
                alert.accept()
            except:
                pass

            if current_url != original_url:
                print("Potential XSS vulnerability detected!")
                print("Original URL:", original_url)
                print("Current URL:", current_url)
                print(f"Payload: {payload}")
                break

    except Exception as e:
        print("Error occurred:", str(e))
