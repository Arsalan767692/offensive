# Install necessary libraries
!pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Function to check for SQL Injection vulnerability
def check_sql_injection(url):
    print(f"Checking for SQL Injection vulnerability on {url}...")
    # Common SQL injection payloads
    payloads = ["'", "' OR '1'='1", "' AND 1=1--", "' UNION SELECT NULL--"]

    for payload in payloads:
        target_url = f"{url}?id={payload}"
        response = requests.get(target_url)
        if "SQL syntax" in response.text or "mysql" in response.text.lower():
            print(f"Potential SQL Injection vulnerability detected with payload: {payload}")
        else:
            print(f"No SQL Injection vulnerability detected with payload: {payload}")

# Function to check for Cross-Site Scripting (XSS) vulnerability
def check_xss(url):
    print(f"\nChecking for XSS vulnerability on {url}...")
    xss_payload = "<script>alert('XSS')</script>"
    response = requests.get(f"{url}?q={xss_payload}")

    # If the payload is reflected back in the response, it may be vulnerable to XSS
    if xss_payload in response.text:
        print("Potential XSS vulnerability detected!")
    else:
        print("No XSS vulnerability detected.")

# Function to check for insecure headers
def check_insecure_headers(url):
    print(f"\nChecking for insecure headers on {url}...")
    response = requests.get(url)
    headers = response.headers

    # Check for common security headers
    if 'X-Content-Type-Options' not in headers:
        print("Missing 'X-Content-Type-Options' header (may allow MIME-type sniffing).")
    if 'X-Frame-Options' not in headers:
        print("Missing 'X-Frame-Options' header (may allow clickjacking).")
    if 'Content-Security-Policy' not in headers:
        print("Missing 'Content-Security-Policy' header (may allow XSS attacks).")
    else:
        print("Security headers are properly configured.")

# Example usage (replace with your target URL)
target_url = "http://example.com"  # Replace with the target URL

# Run the vulnerability tests
check_sql_injection(target_url)
check_xss(target_url)
check_insecure_headers(target_url)
