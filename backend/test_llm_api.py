#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import json

# Test LLM-powered summary
url = 'http://127.0.0.1:8000/api/query/'
data = json.dumps({'message': 'Analyze Akurdi'}).encode('utf-8')
headers = {'Content-Type': 'application/json'}

try:
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    with urllib.request.urlopen(req, timeout=90) as response:
        result = json.loads(response.read().decode())
        print("=" * 70)
        print("API RESPONSE WITH LLM-POWERED SUMMARY")
        print("=" * 70)
        print(f"\nArea: {result.get('area')}")
        print(f"\nLLM-Generated Summary:")
        print("-" * 70)
        summary = result.get('summary', '')
        print(summary.encode('utf-8', errors='replace').decode('utf-8'))
        print("-" * 70)
        print(f"\nChart Data:")
        print(f"  Years: {result.get('chart', {}).get('years')}")
        chart_vals = result.get('chart', {}).get('values', [])
        print(f"  Values (first 3): {chart_vals[:3]}")
        print(f"\nTable Data: {len(result.get('table', []))} records")
        print(f"\nSUCCESS: LLM integration working!")
        print("=" * 70)
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
