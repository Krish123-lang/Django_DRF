# Fetching API
import requests

r = requests.get('http://localhost:8000/stuinfo/1')
# print(r.status_code)
js = r.json()
print(js)