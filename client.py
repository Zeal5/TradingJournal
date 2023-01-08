# import requests

# url = "http://localhost:3001/user/login/"
# data = {
#     "email": "a2sa@q.com",
#     "password": "q",
# }
# r = requests.post(url,json=data)
# print(r.text)
# print(r)

import requests
import json

url = "http://localhost:3001/user/login/"

payload = json.dumps({
  "email": "a2sa@q.com",
  "password": "q"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)