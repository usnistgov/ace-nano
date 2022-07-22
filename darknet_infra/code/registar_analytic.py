import requests
import json

url = "http://ACE_IP_ADDR:PORT/api/v1/add_analytic"

payload = json.dumps(
{"analytic_host": "NANO_IP_ADDR","analytic_name": "jetson_yolo"}
)
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

