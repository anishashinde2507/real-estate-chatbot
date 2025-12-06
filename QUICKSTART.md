# Quick Start Guide

## ⚡ 5-Minute Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- Git (optional)

---

## Step 1: Backend Setup (2 minutes)

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
python generate_data.py
python manage.py runserver
```

✅ **Expected:** `Starting development server at http://127.0.0.1:8000/`

---

## Step 2: Frontend Setup (2 minutes)

```bash
cd frontend
npm install
npm start
```

✅ **Expected:** `Compiled successfully! Open http://localhost:3000`

---

## Step 3: Test (1 minute)

1. Open browser to `http://localhost:3000`
2. Type: **"Analyze Wakad"**
3. Click **Send** (➤)

---

## 🎯 Expected Output

### Chat Window
```
👤 You: Analyze Wakad
🤖 Bot: ✅ Analysis complete for Wakad! Found 5 properties.
```

### Summary Card
```
📊 Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Real Estate Analysis for Wakad

• Average Price: ₹54 Lakhs
• Price Range: ₹45 - ₹65 Lakhs
• Average Demand: 90%
• Average Size: 1350 sq.ft.
• Total Properties: 5
```

### Price Trend Chart
```
65 ┤       ╭─────╮
60 ┤     ╭─╯
52 ┤   ╭─╯
48 ┤ ╭─╯
45 ┤─╯
   └─────────────────
    2020 2021 2022 2023 2024
```

### Data Table
```
┌──────┬────────┬───────┬────────┬──────┐
│ Year │  Area  │ Price │ Demand │ Size │
├──────┼────────┼───────┼────────┼──────┤
│ 2020 │ Wakad  │   45  │   85   │ 1200 │
│ 2021 │ Wakad  │   48  │   88   │ 1250 │
│ 2022 │ Wakad  │   52  │   90   │ 1300 │
│ 2023 │ Wakad  │   58  │   92   │ 1400 │
│ 2024 │ Wakad  │   65  │   95   │ 1500 │
└──────┴────────┴───────┴────────┴──────┘
```

---

## 🧪 Test Queries

Try these queries:

| Query | Result |
|-------|--------|
| "Analyze Wakad" | Shows Wakad properties (5 rows) |
| "Show price trend for Akurdi" | Shows Akurdi properties (5 rows) |
| "Analyze Aundh" | Shows Aundh properties (5 rows) |
| "Tell me about Baner" | Shows Baner properties (5 rows) |
| "Random area XYZ" | No data found message |

---

## 🛑 Stop Servers

- **Backend**: Press `Ctrl+C` in Django terminal
- **Frontend**: Press `Ctrl+C` in npm terminal

---

## 📱 Mobile Testing

Open `http://localhost:3000` on mobile or use Chrome DevTools
(Ctrl+Shift+I → Toggle device toolbar)

The app is fully responsive!

---

## ❓ Got Issues?

### Error: "Cannot find module 'pandas'"
```bash
pip install pandas openpyxl
```

### Error: "CORS error" or "Failed to fetch"
- Ensure Django is running: `python manage.py runserver`
- Check `http://localhost:8000/api/query/` works in Postman

### Error: "Cannot find module 'react'"
```bash
cd frontend && npm install
```

---

## 🎓 Next Steps

1. ✅ Application is working!
2. 📚 Read `SETUP_GUIDE.md` for detailed documentation
3. 🔧 Customize colors, add more areas
4. 📊 Add your own Excel data
5. 🚀 Deploy to production

---

**You're all set! Enjoy your chatbot! 🚀**
