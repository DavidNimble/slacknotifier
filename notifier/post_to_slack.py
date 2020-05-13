import requests
url = ''# replace with slack webhook URL
data = {"text": "Hello, world."}
requests.post(url, json=data)
