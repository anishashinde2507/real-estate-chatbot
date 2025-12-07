# 🏠 Real Estate Analysis Chatbot (React + Django + HuggingFace)

This project is a **full-stack Real Estate Analysis Chatbot** that allows users to analyze real estate localities using **natural language queries** like:

- “Analyze Wakad”
- “Show price trend for Akurdi”
- “Compare Aundh and Baner demand”

The application reads data from an **Excel file**, generates:
- ✅ AI-based summary  
- ✅ Year-wise price/demand chart  
- ✅ Filtered data table  

and displays them inside a **chatbot-style UI**.

---
## 🛠️ Tech Stack

### 🔹 Frontend
- React
- Bootstrap
- Recharts / Chart.js
- Axios / Fetch API

### 🔹 Backend
- Django
- Django REST Framework
- Pandas
- Python-dotenv
- Requests

### 🔹 AI Integration
- HuggingFace Inference API (Mistral / Gemma model)

### 🔹 Deployment
- Frontend → Vercel
- Backend → Render

---

## ✨ Features

✅ Chat-style user interface  
✅ Natural language query support  
✅ Excel-based data filtering  
✅ AI-powered real estate summary  
✅ Interactive price/demand trend chart  
✅ Filtered data table  
✅ Secure API key handling using environment variables  
✅ Fully deployed full-stack application  

---


---

## ⚙️ Backend Setup (Local)

### 1️⃣ Create & Activate Virtual Environment
```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Add .env File

Create a .env file inside backend/:
```bash
HUGGINGFACE_API_KEY=hf_your_api_key_here
DEBUG=True
```
### 4️⃣ Apply Migrations & Run Server
```bash
python manage.py migrate
python manage.py runserver
```

## 🌐 Frontend Setup (Local)
### 1️⃣ Install Dependencies
```bash
cd frontend
npm install
```
### 2️⃣ Add Environment Variable

Create .env inside frontend/
```bash
REACT_APP_API_URL=http://127.0.0.1:8000/api/query
```
### 3️⃣ Run Frontend
```bash
npm start
```




