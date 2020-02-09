import requests

payload = {'test': 'test'}
url = "localhost:8000"
requests.post(url, data=payload)
print("Send")
