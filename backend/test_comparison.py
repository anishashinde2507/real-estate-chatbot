import urllib.request
import json

# Test comparison query
url = 'http://localhost:8000/api/query/'
data = json.dumps({'message': 'Compare Ambegaon Budruk and Aundh'}).encode('utf-8')
headers = {'Content-Type': 'application/json'}

try:
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())
        print("=== COMPARISON RESPONSE ===")
        print(json.dumps(result, indent=2))
except Exception as e:
    print(f'Error: {e}')

print("\n\n")

# Test single area query
data2 = json.dumps({'message': 'Analyze Akurdi'}).encode('utf-8')
try:
    req = urllib.request.Request(url, data=data2, headers=headers, method='POST')
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())
        print("=== SINGLE AREA RESPONSE ===")
        print(json.dumps(result, indent=2))
except Exception as e:
    print(f'Error: {e}')
