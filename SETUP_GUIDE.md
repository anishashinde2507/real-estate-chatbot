# Real Estate Analysis Chatbot - Complete Setup Guide

## 📋 Project Overview

A full-stack chatbot application for real estate analysis with:
- **Backend**: Django REST API with pandas-based Excel parsing
- **Frontend**: React with Recharts visualization
- **Data**: Real estate trends by area, year, price, and demand

---

## 🗂️ Project Structure

```
Real Estate/
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── services.py          # Excel parsing & analysis logic
│   │   ├── views.py             # API endpoints
│   │   ├── serializers.py       # Request/response validation
│   │   └── urls.py              # Route definitions
│   ├── realestate_api/
│   │   ├── __init__.py
│   │   ├── settings.py          # Django configuration
│   │   ├── urls.py              # URL routing
│   │   └── wsgi.py              # WSGI application
│   ├── data/
│   │   └── realestate.xlsx      # Sample Excel file
│   ├── manage.py                # Django management script
│   ├── generate_data.py         # Data generation script
│   └── requirements.txt         # Python dependencies
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx       # Chat interface
│   │   │   ├── ChatWindow.css
│   │   │   ├── MessageBubble.jsx    # Message display
│   │   │   ├── MessageBubble.css
│   │   │   ├── SummaryCard.jsx      # Analysis summary
│   │   │   ├── SummaryCard.css
│   │   │   ├── TrendChart.jsx       # Price trend chart
│   │   │   ├── TrendChart.css
│   │   │   ├── DataTable.jsx        # Property table
│   │   │   └── DataTable.css
│   │   ├── api/
│   │   │   └── queryApi.js          # API communication
│   │   ├── App.jsx                  # Main app component
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── .env                     # Environment variables
│   ├── .gitignore
│   └── package.json             # Dependencies
```

---

## ⚙️ Setup Instructions

### Part 1: Backend Setup (Django)

#### 1.1 Create Virtual Environment

```bash
cd backend
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

#### 1.2 Install Dependencies

```bash
pip install -r requirements.txt
```

#### 1.3 Generate Sample Data

```bash
python generate_data.py
```

Output:
```
✓ Excel file created: data/realestate.xlsx
✓ Total records: 20
✓ Areas: ['Wakad', 'Akurdi', 'Aundh', 'Baner']
```

#### 1.4 Run Django Development Server

```bash
python manage.py runserver
```

Expected output:
```
Starting development server at http://127.0.0.1:8000/
```

---

### Part 2: Frontend Setup (React)

#### 2.1 Install Node Dependencies

```bash
cd frontend
npm install
```

This installs:
- `react` - UI library
- `react-dom` - DOM rendering
- `recharts` - Charting library
- `react-scripts` - Build tools

#### 2.2 Start React Development Server

```bash
npm start
```

Expected output:
```
Compiled successfully!
Open http://localhost:3000 to view it in your browser.
```

---

## 🚀 Using the Application

### Example Queries

Try these queries in the chatbot:

1. **"Analyze Wakad"**
   - Shows all Wakad properties
   - Price trend from 2020-2024
   - Summary statistics

2. **"Show price trend for Akurdi"**
   - Displays Akurdi price progression
   - Line chart visualization
   - Demand and size data

3. **"Compare Aundh and Baner demand"**
   - (Note: Currently analyzes one area at a time)
   - Can query "Analyze Aundh" then "Analyze Baner"

### Available Areas in Sample Data

- **Wakad** - ₹45L to ₹65L (2020-2024)
- **Akurdi** - ₹35L to ₹48L (2020-2024)
- **Aundh** - ₹50L to ₹65L (2020-2024)
- **Baner** - ₹42L to ₹56L (2020-2024)

---

## 📊 API Documentation

### Endpoint: `POST /api/query/`

**Request:**
```json
{
  "message": "Analyze Wakad"
}
```

**Response:**
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
    ...
  ]
}
```

---

## 🔧 Backend Architecture

### services.py - Core Logic

```
RealEstateService
├── __init__() - Load Excel data
├── _load_data() - Read Excel file with pandas
├── detect_area() - Extract area name from query
├── filter_by_area() - Filter DataFrame by area
├── get_price_trend() - Generate chart data
├── get_summary() - Create natural language summary
├── get_table_data() - Format data for JSON response
└── analyze_query() - Main pipeline
```

### views.py - REST API

- `QueryView` - POST endpoint at `/api/query/`
- Validates input with serializers
- Calls service for analysis
- Returns formatted JSON response

### CORS Configuration

The backend accepts requests from:
- `http://localhost:3000` (React dev server)
- `http://localhost:5173` (Vite dev server)

---

## 🎨 Frontend Architecture

### Component Hierarchy

```
App (Main container)
├── ChatWindow
│   ├── MessageBubble (repeated for each message)
│   └── Input area
├── SummaryCard (Summary statistics)
├── TrendChart (Recharts line chart)
└── DataTable (Property data in table)
```

### State Management

- `analysis` - Current query result
- `isLoading` - API call status
- `error` - Error messages

### Data Flow

1. User types message → ChatWindow
2. "Send" button triggers `onSendMessage()`
3. Message sent to backend via `queryApi.js`
4. Backend returns analysis result
5. Components update with chart, table, summary
6. Bot response shown in chat

---

## 🛠️ Customization

### Adding More Areas

1. Add rows to Excel file with new area names
2. Restart backend
3. Query will auto-detect new areas

### Changing Gradient Colors

**Backend card headers** - Edit `settings.py`:
```python
# CORS and styling config
```

**Frontend colors** - Edit component `.css` files:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Modifying Columns

To analyze different properties, add columns to Excel:
- `Location` - Latitude/longitude
- `Beds` - Number of bedrooms
- `Age` - Property age

Then update `services.py` to process new columns.

---

## 🐛 Troubleshooting

### Issue: "Module not found: pandas"

**Solution:**
```bash
pip install pandas openpyxl
```

### Issue: "CORS error" in browser console

**Solution:** Ensure Django server is running on `http://localhost:8000`

### Issue: "No data found for X"

**Solution:** Check if area name in Excel matches query (case-insensitive but exact)

### Issue: Chart not displaying

**Solution:** 
1. Check browser console for errors
2. Ensure `recharts` is installed: `npm install recharts`
3. Verify chart data has entries

---

## 📦 Dependencies

### Backend Requirements
- Django 4.2 - Web framework
- djangorestframework 3.14 - REST API
- django-cors-headers 4.0 - CORS support
- pandas 2.0 - Data analysis
- openpyxl 3.10 - Excel handling

### Frontend Requirements
- react 18.2 - UI framework
- react-dom 18.2 - DOM rendering
- recharts 2.10 - Charting library

---

## 📝 Example Workflow

```
1. Start Backend:
   $ python manage.py runserver
   Backend running on http://localhost:8000

2. Start Frontend:
   $ npm start
   Frontend running on http://localhost:3000

3. Open browser:
   Navigate to http://localhost:3000

4. Send query:
   "Analyze Wakad"

5. See results:
   ✓ Chat shows analysis complete
   ✓ Summary card shows statistics
   ✓ Chart shows price trend
   ✓ Table shows all properties
```

---

## 🚀 Deployment

### Backend (Production)

```bash
# Use gunicorn for production
pip install gunicorn
gunicorn realestate_api.wsgi --bind 0.0.0.0:8000

# Update DEBUG = False in settings.py
# Set SECRET_KEY from environment variable
```

### Frontend (Production)

```bash
# Build optimized bundle
npm run build

# Serves a production-ready build in build/ folder
```

---

## 📞 Support

For issues or questions:
1. Check console for error messages
2. Verify both servers are running
3. Check network tab in browser DevTools
4. Review API response format

---

**Happy Analyzing! 📊**
