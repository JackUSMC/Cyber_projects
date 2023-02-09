"""This code uses the requests library to make a GET request to each website and retrieve its content. 
The is_suspicious function checks the content for keywords that might indicate a suspicious website, and 
the send_alert function sends a notification if a suspicious website is detected. In this example, the 
send_alert function simply prints a message, but you could modify it to send an email, SMS, or any other type of alert. 
The crawl function ties everything together by making the request, checking the content, and sending an alert if necessary."""

import requests
import re

# Function to determine if a website is suspicious
def is_suspicious(content):
    # Check for keywords that might indicate a suspicious website
    keywords = ["hack", "malware", "phishing"]
    for keyword in keywords:
        if keyword in content.lower():
            return True
    return False

# Function to send alert
def send_alert(url):
    # Implement code to send an alert notification here (e.g. email, SMS, etc.)
    print(f"ALERT: Suspicious website detected - {url}")

# Function to crawl a website and check for suspicious content
def crawl(url):
    try:
        response = requests.get(url)
        content = response.text
        if is_suspicious(content):
            send_alert(url)
    except:
        print(f"Error accessing {url}")

# Example usage
websites = ["https://www.google.com", "https://www.badwebsite.com", "https://www.facebook.com"]
for website in websites:
    crawl(website)
