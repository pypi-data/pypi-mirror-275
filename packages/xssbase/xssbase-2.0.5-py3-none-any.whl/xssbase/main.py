from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import StaleElementReferenceException
import os

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
        xss_found = False  # Flag to track if XSS vulnerability is found

        # Get the directory of the script
        script_dir = os.path.dirname(os.path.realpath(__file__))
        payloads_file = os.path.join(script_dir, "payloads.txt")

        with open(payloads_file) as f:
            payloads = f.read().splitlines()

        for payload in payloads:
            find_and_fill_inputs(driver, payload)
            
            # Check if URL changes due to payload injection
            current_url = driver.current_url
            if current_url != original_url:
                print("Potential XSS vulnerability detected!")
                print("Original URL:", original_url)
                print("Current URL:", current_url)
                print()

                xss_found = True
                break  # Add break here to stop after finding first XSS

        if not xss_found:
            print("No XSS vulnerability found. The site may be in good health. Try another site.")

    except Exception as e:
        print("Error occurred:", str(e))
