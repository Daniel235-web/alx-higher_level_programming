import urllib.request
import sys

# Check if the URL argument is provided
if len(sys.argv) < 2:
    print("https://alx-intranet.hbtn.io/status")
    sys.exit(1)

url = sys.argv[1]

try:
    # Send the request and retrieve the response
    with urllib.request.urlopen(url) as response:
        # Read and decode the body of the response
        body = response.read().decode('utf-8')

        # Print the decoded response body
        print(body)

except urllib.error.HTTPError as e:
    # Handle HTTPError exceptions
    print(f"Error code: {e.code}")
