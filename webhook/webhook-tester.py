import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'  # Ganti dengan URL yang sesuai

data = {
    'event': 'example_event',
    'data': 'example_data'
}

headers = {'Content-Type': 'application/json'}
response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

print("Response from webhook server:", response.json())
