# Quick Start Guide - Real Estate Chatbot Backend

## Starting the Server

```bash
cd "c:\Users\hp\Downloads\Real Estate\backend"
venv\Scripts\python manage.py runserver 127.0.0.1:8000
```

Server will be available at: `http://127.0.0.1:8000/`

## API Endpoints

### 1. Query Analysis Endpoint
**POST** `/api/query/`

**Request**:
```json
{
  "message": "Analyze Akurdi"
}
```

**Response**:
```json
{
  "type": "single",
  "area": "Akurdi",
  "summary": "Akurdi real estate market analysis (2020-2024): Average rate: Rs 7,803/sqft with upward trend of 26.7%. Price range: Rs 6,488 to Rs 8,774/sqft. Transaction activity: 2675 units sold (increased by 25.5%). Moderate market with 12.2% price volatility.",
  "chart": {
    "years": [2020, 2021, 2022, 2023, 2024],
    "values": [6488, 7046, 7404, 8081, 8774]
  },
  "table": [
    {
      "year": 2020,
      "location": "Akurdi",
      "price": 6488,
      "sales": 456,
      "units": 533
    },
    ...
  ]
}
```

### 2. Comparison Endpoint
**POST** `/api/query/`

**Request**:
```json
{
  "message": "Compare Akurdi and Wakad"
}
```

**Response**:
```json
{
  "type": "comparison",
  "areas": ["Akurdi", "Wakad"],
  "summary": "Market Comparison...",
  "chart": {...},
  "tables": {
    "Akurdi": [...],
    "Wakad": [...]
  }
}
```

### 3. Debug Endpoint (Testing)
**GET** `/api/debug/`

Verifies HuggingFace API key configuration and availability.

**Response**:
```json
{
  "status": "OK",
  "api_key_configured": true,
  "api_key_preview": "hf_XXXXXXXXXXXXX...XXXXX",
  "sample_data_rows": 5,
  "test_llm": "Available"
}
```

## Example Queries

### Single Area Analysis
- "Analyze Akurdi"
- "Tell me about Wakad"
- "What's happening in Aundh?"
- "Ambegaon Budruk analysis"

### Comparison Queries
- "Compare Akurdi and Aundh"
- "Wakad vs Ambegaon Budruk"
- "Compare all areas"

### Available Areas
- Akurdi
- Ambegaon Budruk
- Aundh
- Wakad

## Summary Features

Each summary includes:
- **Market Analysis Period**: Year range (2020-2024)
- **Price Performance**: Average rate, trend percentage, min/max range
- **Transaction Activity**: Total units sold, trend direction
- **Market Stability**: Volatility assessment and percentage
- **Growth Patterns**: Historical price and sales trends

## Testing with cURL

```bash
# Single area analysis
curl -X POST http://127.0.0.1:8000/api/query/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Analyze Akurdi"}'

# Comparison
curl -X POST http://127.0.0.1:8000/api/query/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Compare Akurdi and Wakad"}'

# Debug check
curl -X GET http://127.0.0.1:8000/api/debug/
```

## Python Client Example

```python
import urllib.request
import json

# Query analysis
data = json.dumps({"message": "Analyze Akurdi"}).encode('utf-8')
req = urllib.request.Request(
    'http://127.0.0.1:8000/api/query/',
    data=data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

with urllib.request.urlopen(req, timeout=60) as response:
    result = json.loads(response.read())
    print(result['summary'])
```

## JavaScript/React Client Example

```javascript
// Fetch data
const response = await fetch('http://127.0.0.1:8000/api/query/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: 'Analyze Akurdi'
  })
});

const data = await response.json();
console.log(data.summary);
console.log(data.chart);
console.log(data.table);
```

## Response Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success - Analysis complete |
| 400 | Bad Request - Invalid message format |
| 500 | Server Error - Internal error |

## Troubleshooting

### Server won't start
- Make sure venv is activated
- Check that port 8000 is not in use
- Verify Python 3.11 is installed

### API returns 400
- Verify JSON format of request
- Ensure "message" field is present and non-empty

### Slow responses
- First request may be slower (data loading)
- Subsequent requests are cached for same area

### Summary looks generic
- This is normal when HuggingFace API is unavailable
- Backend uses analytical engine for fallback
- Still provides sophisticated market insights

## Production Deployment

Before deploying to production:

1. **Environment Variables**: Ensure `.env` file is in production server
2. **Database**: Run `python manage.py migrate`
3. **Static Files**: Run `python manage.py collectstatic`
4. **Security**: Set `DEBUG = False` in settings.py
5. **CORS**: Update `CORS_ALLOWED_ORIGINS` with production domain
6. **API Key**: Update `HUGGINGFACE_API_KEY` in `.env`

---

**Backend Status**: ✅ Running & Tested  
**Last Updated**: December 5, 2025
