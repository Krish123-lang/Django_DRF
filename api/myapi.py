import requests
import json

url = 'http://localhost:8000/stucreate'

data = {
    'id': 20,
    'name': 'Mark',
    'roll': 20,
    'city': 'Kathmandu'
}

json_data = json.dumps(data)
r = requests.post(url=url, data=json_data)
data = r.json()
print(data)
