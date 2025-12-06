import urllib.request
import json

url = 'http://localhost:8000/api/query/'
data = json.dumps({'message': 'Analyze Akurdi'}).encode('utf-8')
headers = {'Content-Type': 'application/json'}

try:
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())
        print(json.dumps(result, indent=2))
except Exception as e:
    print(f'Error: {e}')
