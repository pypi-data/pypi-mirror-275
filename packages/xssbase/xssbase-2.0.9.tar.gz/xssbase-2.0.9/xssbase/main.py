from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException

def test_xss_payloads(driver, url, payload):
    vulnerability_found = False  # Flag to track if XSS vulnerability is found

    try:
        driver.get(url)
        original_url = driver.current_url

        # Find all input boxes and skip those with types 'number', 'email', and 'date'
        input_boxes = driver.find_elements(By.XPATH, "//input[@type='text' or @type='password' or @type='search' or @type='tel' or @type='url' or @type='text' or @type='text' or @type='text' or @type='text']")
        for input_box in input_boxes:
            input_box_type = input_box.get_attribute('type')
            if input_box_type in ['number', 'email', 'date']:
                continue

            # Fill the input box with XSS payload
            input_box.clear()
            input_box.send_keys(payload)
            input_box.submit()

            # Check if URL changes due to payload injection
            time.sleep(2)  # Allow time for potential alert boxes to appear
            current_url = driver.current_url
            if current_url != original_url:
                vulnerability_found = True  # Set flag to True if XSS vulnerability is found
                print("Potential XSS vulnerability detected!")
                print("Payload:", payload)
                print("Current URL:", current_url)
                print("Original URL:", original_url)
                break  # Exit the loop once XSS vulnerability is found

        # Check the flag and print message accordingly
        if not vulnerability_found:
            print("No XSS vulnerability found. The site may be in good health. Try another site.")

    except Exception as e:
        print("Error occurred:", str(e))
