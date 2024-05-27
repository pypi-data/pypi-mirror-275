from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_xss_payloads(driver, url, payloads):
    vulnerability_found = False

    try:
        driver.get(url)
        original_url = driver.current_url

        for payload in payloads:
            input_boxes = driver.find_elements(By.XPATH, "//input[@type='text' or @type='password' or @type='search' or @type='tel' or @type='url' or @type='text' or @type='text' or @type='text' or @type='text']")
            for input_box in input_boxes:
                input_box_type = input_box.get_attribute('type')
                if input_box_type in ['number', 'email', 'date']:
                    continue

                input_box.clear()
                input_box.send_keys(payload)
                input_box.submit()

                time.sleep(2)
                current_url = driver.current_url
                if current_url != original_url:
                    vulnerability_found = True
                    print("Potential XSS vulnerability detected!")
                    print("Payload:", payload)
                    print("Current URL:", current_url)
                    print("Original URL:", original_url)
                    break

            if vulnerability_found:
                break

        if not vulnerability_found:
            print("No XSS vulnerability found. The site may be in good health. Try another site.")

    except Exception as e:
        print("Error occurred:", str(e))
