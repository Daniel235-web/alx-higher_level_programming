import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)

data = response.text

print("Body response:")
print("\t- type:", type(data))
print("\t- content:", data)


