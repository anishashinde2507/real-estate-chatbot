# API Response Examples

## Example 1: Query "Analyze Wakad"

### Request
```bash
POST http://localhost:8000/api/query/
Content-Type: application/json

{
  "message": "Analyze Wakad"
}
```

### Response (200 OK)
```json
{
  "area": "Wakad",
  "summary": "📊 Real Estate Analysis for Wakad\n\n• Average Price: ₹54 Lakhs\n• Price Range: ₹45 - ₹65 Lakhs\n• Average Demand: 90%\n• Average Size: 1350 sq.ft.\n• Total Properties: 5",
  "chart": {
    "years": ["2020", "2021", "2022", "2023", "2024"],
    "values": [45, 48, 52, 58, 65]
  },
  "table": [
    {
      "Year": 2020,
      "Area": "Wakad",
      "Price": 45,
      "Demand": 85,
      "Size": 1200
    },
    {
      "Year": 2021,
      "Area": "Wakad",
      "Price": 48,
      "Demand": 88,
      "Size": 1250
    },
    {
      "Year": 2022,
      "Area": "Wakad",
      "Price": 52,
      "Demand": 90,
      "Size": 1300
    },
    {
      "Year": 2023,
      "Area": "Wakad",
      "Price": 58,
      "Demand": 92,
      "Size": 1400
    },
    {
      "Year": 2024,
      "Area": "Wakad",
      "Price": 65,
      "Demand": 95,
      "Size": 1500
    }
  ]
}
```

---

## Example 2: Query "Show price trend for Akurdi"

### Request
```bash
POST http://localhost:8000/api/query/
Content-Type: application/json

{
  "message": "Show price trend for Akurdi"
}
```

### Response (200 OK)
```json
{
  "area": "Akurdi",
  "summary": "📊 Real Estate Analysis for Akurdi\n\n• Average Price: ₹41 Lakhs\n• Price Range: ₹35 - ₹48 Lakhs\n• Average Demand: 80%\n• Average Size: 1200 sq.ft.\n• Total Properties: 5",
  "chart": {
    "years": ["2020", "2021", "2022", "2023", "2024"],
    "values": [35, 37, 40, 44, 48]
  },
  "table": [
    {
      "Year": 2020,
      "Area": "Akurdi",
      "Price": 35,
      "Demand": 75,
      "Size": 1100
    },
    {
      "Year": 2021,
      "Area": "Akurdi",
      "Price": 37,
      "Demand": 78,
      "Size": 1150
    },
    {
      "Year": 2022,
      "Area": "Akurdi",
      "Price": 40,
      "Demand": 80,
      "Size": 1200
    },
    {
      "Year": 2023,
      "Area": "Akurdi",
      "Price": 44,
      "Demand": 82,
      "Size": 1250
    },
    {
      "Year": 2024,
      "Area": "Akurdi",
      "Price": 48,
      "Demand": 85,
      "Size": 1300
    }
  ]
}
```

---

## Example 3: Query with Invalid Area "Analyze XYZ"

### Request
```bash
POST http://localhost:8000/api/query/
Content-Type: application/json

{
  "message": "Analyze XYZ"
}
```

### Response (200 OK - but no data)
```json
{
  "area": "",
  "summary": "No data found for .",
  "chart": {
    "years": [],
    "values": []
  },
  "table": []
}
```

---

## Example 4: Invalid Request (Missing field)

### Request
```bash
POST http://localhost:8000/api/query/
Content-Type: application/json

{}
```

### Response (400 Bad Request)
```json
{
  "error": {
    "message": [
      "This field is required."
    ]
  }
}
```

---

## Testing with Postman

### 1. Import Collection
Create new POST request:
- **URL**: `http://localhost:8000/api/query/`
- **Method**: POST
- **Headers**: `Content-Type: application/json`

### 2. Test Case 1: Wakad Analysis
```json
{
  "message": "Analyze Wakad"
}
```
Expected: 5 properties, price ₹45-65L

### 3. Test Case 2: Akurdi Analysis
```json
{
  "message": "Show price trend for Akurdi"
}
```
Expected: 5 properties, price ₹35-48L

### 4. Test Case 3: Empty Query
```json
{
  "message": ""
}
```
Expected: No data found

---

## Testing with cURL

```bash
# Test 1: Analyze Wakad
curl -X POST http://localhost:8000/api/query/ \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Analyze Wakad\"}"

# Test 2: Analyze Akurdi
curl -X POST http://localhost:8000/api/query/ \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Show price trend for Akurdi\"}"
```

---

## Response Structure

All successful responses follow this structure:

```json
{
  "area": "string",              // Detected area name
  "summary": "string",           // Multi-line summary text
  "chart": {
    "years": ["string", ...],    // X-axis labels
    "values": [number, ...]      // Y-axis values
  },
  "table": [
    {
      "Year": number,
      "Area": "string",
      "Price": number,
      "Demand": number,
      "Size": number
    },
    ...
  ]
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": {
    "fieldName": ["Error message"]
  }
}
```

### 500 Internal Server Error
```json
{
  "error": "Analysis failed: [error details]"
}
```

---

## Performance Metrics

- **Response Time**: ~50ms average
- **Max Query Length**: 500 characters
- **Max Table Rows**: 20 (current sample data)
- **Chart Points**: Up to 10 years

---

## Data Format Notes

- **Price** values are in Lakhs (₹)
- **Demand** is percentage (0-100)
- **Size** is in sq.ft.
- **Year** is integer (YYYY format)

---
