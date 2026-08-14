import requests

response = requests.get("https://api.restful-api.dev/objects")
data = response.json()
print(data)