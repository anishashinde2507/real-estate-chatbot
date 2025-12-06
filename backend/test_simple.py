#!/usr/bin/env python
import sys
import subprocess

# Test using curl-like request
result = subprocess.run([
    sys.executable, '-c',
    '''
import json
import urllib.request

url = "http://localhost:8000/api/query/"
data = json.dumps({"message": "Analyze Akurdi"}).encode()
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
try:
    with urllib.request.urlopen(req) as r:
        print(json.dumps(json.load(r), indent=2))
except Exception as e:
    print(f"Error: {e}")
'''
], capture_output=True, text=True)

print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
