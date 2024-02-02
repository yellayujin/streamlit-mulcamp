import requests

req = requests.get("http://google.com")
req.raise_for_status()
req.status_code()