#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: TODO: Add description 
# Date:        TODO: Add date
# Modified by: TODO: Add your name

### TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

# The purpose of this function is to retrieve all the HTML form elements present on a given web page specified by the 'url'. 
# It accomplishes this by making a request to the web page, parsing the HTML content using the BeautifulSoup library, and 
# then using the 'find_all' method of BeautifulSoup to locate and extract all occurrences of the "form" tag in the HTML.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# The purpose of this function is to extract relevant details from an HTML form element passed as input ('form') and 
# return those details in a structured format. The function parses the form's attributes, including the action, method,
# and input fields, and then stores this information in a dictionary.
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# The purpose of this function is to simulate the submission of an HTML form with specific data to a target URL, 
# based on the form details and the provided 'value'. The function takes in 'form_details', which is a dictionary 
# containing the necessary information about the form (action, method, and input fields), 'url' which is the base 
# URL of the webpage, and 'value' which represents the data to be submitted to the form.
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# The purpose of this function is to scan a given URL for potential Cross-Site Scripting (XSS) vulnerabilities.
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = '<script>alert(1)</script>' 
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

# Takes input from the user in an URL form. Then, the code scans the page in a URL format and scan to verify if it is vulnerable to XSS
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))
