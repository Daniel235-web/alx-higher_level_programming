#!/usr/bin/python3
import urllib.request
import sys

# Check if the URL argument is provided
if len(sys.argv) < 2:
    print("https://alx-intranet.hbtn.io/status")
    sys.exit(1)

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    data = response.read()
    print(data)
