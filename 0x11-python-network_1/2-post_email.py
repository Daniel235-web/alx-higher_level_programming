#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to be sent in the POST request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    # Send the POST request and retrieve the response
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        # Read and decode the body of the response
        body = response.read().decode('utf-8')

        # Print the decoded response body
        print(body)

except urllib.error.HTTPError as e:
    # Handle HTTPError exceptions
    print(f"HTTP Error {e.code}: {e.reason}")

