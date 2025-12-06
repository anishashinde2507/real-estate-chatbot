# 🛠️ Installation & Dependencies Checklist

## ✅ Pre-Installation Requirements

### System Requirements
- [ ] Python 3.8 or higher installed
- [ ] Node.js 14+ installed
- [ ] npm 6+ installed
- [ ] Git installed (optional)
- [ ] 500MB free disk space
- [ ] Terminal/CMD access
- [ ] Text editor or IDE (VS Code recommended)

### Verify Installation
```bash
# Check Python
python --version  # Should show 3.8+

# Check Node.js
node --version    # Should show 14+

# Check npm
npm --version     # Should show 6+
```

---

## 📦 Backend Dependencies

### Python Packages (via pip)

```txt
Django==4.2.0
djangorestframework==3.14.0
django-cors-headers==4.0.0
pandas==2.0.0
openpyxl==3.10.0
```

### Installation Steps

```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install from requirements.txt
pip install -r requirements.txt

# 5. Verify installation
pip list
```

### Dependency Details

| Package | Version | Purpose | Size |
|---------|---------|---------|------|
| Django | 4.2.0 | Web framework | ~3MB |
| DRF | 3.14.0 | REST API | ~2MB |
| django-cors-headers | 4.0.0 | CORS support | ~100KB |
| pandas | 2.0.0 | Data analysis | ~15MB |
| openpyxl | 3.10.0 | Excel handling | ~5MB |

**Total Backend Size:** ~25MB

---

## 🎨 Frontend Dependencies

### Node Packages (via npm)

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "recharts": "^2.10.0",
    "react-scripts": "5.0.1"
  }
}
```

### Installation Steps

```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies from package.json
npm install

# 3. Verify installation
npm list

# 4. Should show:
# react@18.2.0
# react-dom@18.2.0
# recharts@2.10.0
```

### Dependency Details

| Package | Version | Purpose | Size |
|---------|---------|---------|------|
| react | 18.2.0 | UI library | ~40MB |
| react-dom | 18.2.0 | DOM rendering | ~35MB |
| recharts | 2.10.0 | Charts | ~20MB |
| react-scripts | 5.0.1 | Build tools | ~400MB |

**Total Frontend Size:** ~500MB (node_modules)

---

## 🔄 Quick Install Script

### Windows Batch Script

Save as `install.bat`:
```batch
@echo off
echo ===============================
echo Real Estate Chatbot - Full Setup
echo ===============================

echo.
echo [1/4] Setting up Backend...
cd backend
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python generate_data.py
echo [✓] Backend ready!

echo.
echo [2/4] Setting up Frontend...
cd ..\frontend
call npm install
echo [✓] Frontend ready!

echo.
echo [3/4] Summary...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo [4/4] To start development:
echo Terminal 1: cd backend && venv\Scripts\activate && python manage.py runserver
echo Terminal 2: cd frontend && npm start
echo.
echo ✓ Installation complete!
pause
```

### Mac/Linux Bash Script

Save as `install.sh`:
```bash
#!/bin/bash

echo "==============================="
echo "Real Estate Chatbot - Full Setup"
echo "==============================="

echo ""
echo "[1/4] Setting up Backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python generate_data.py
echo "[✓] Backend ready!"

echo ""
echo "[2/4] Setting up Frontend..."
cd ../frontend
npm install
echo "[✓] Frontend ready!"

echo ""
echo "[3/4] Summary..."
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:3000"
echo ""
echo "[4/4] To start development:"
echo "Terminal 1: cd backend && source venv/bin/activate && python manage.py runserver"
echo "Terminal 2: cd frontend && npm start"
echo ""
echo "✓ Installation complete!"
```

---

## 🚀 Complete Setup Checklist

### Step 1: Environment Setup
- [ ] Python 3.8+ installed
- [ ] Node.js 14+ installed
- [ ] Virtual environment created for backend
- [ ] npm cache cleared (if needed)

### Step 2: Backend Setup
- [ ] Backend folder structure created
- [ ] Virtual environment activated
- [ ] pip dependencies installed
- [ ] `pip list` shows all required packages
- [ ] `generate_data.py` executed successfully
- [ ] `realestate.xlsx` file created in `data/` folder

### Step 3: Frontend Setup
- [ ] Frontend folder structure created
- [ ] `npm install` completed
- [ ] `node_modules/` folder created
- [ ] `npm list` shows React, Recharts, react-scripts

### Step 4: File Verification
- [ ] Backend files created (7 files)
- [ ] Frontend components created (7 components)
- [ ] Style files present (7 CSS files)
- [ ] API client created (`queryApi.js`)
- [ ] Main App component created
- [ ] Configuration files present (.env, settings.py)

### Step 5: Test Run
- [ ] Backend server starts: `python manage.py runserver`
- [ ] Backend listens on http://localhost:8000
- [ ] Frontend dev server starts: `npm start`
- [ ] Frontend opens at http://localhost:3000
- [ ] Chat interface visible
- [ ] Can type messages

### Step 6: API Test
- [ ] Send "Analyze Wakad" query
- [ ] Receive 5 properties in response
- [ ] Summary card displays statistics
- [ ] Chart shows price trend line
- [ ] Data table populated
- [ ] No console errors

---

## 🔧 Troubleshooting Checklist

### Backend Issues

#### Issue: "ModuleNotFoundError: No module named 'django'"
- [ ] Virtual environment activated?
- [ ] `pip install -r requirements.txt` completed?
- [ ] Check `pip list` output

**Fix:**
```bash
pip install -r requirements.txt --upgrade
```

#### Issue: "No module named 'pandas'"
- [ ] pip installation completed?
- [ ] openpyxl installed?

**Fix:**
```bash
pip install pandas openpyxl --upgrade
```

#### Issue: "FileNotFoundError: realestate.xlsx"
- [ ] Generated data file?
- [ ] File path correct?

**Fix:**
```bash
python generate_data.py
```

### Frontend Issues

#### Issue: "npm: command not found"
- [ ] Node.js installed?
- [ ] npm in PATH?

**Fix:**
```bash
# Reinstall Node.js from nodejs.org
node --version
npm --version
```

#### Issue: "Cannot find module 'react'"
- [ ] npm install completed?
- [ ] node_modules exists?

**Fix:**
```bash
npm install --no-save
npm cache clean --force
npm install
```

#### Issue: "recharts not found"
- [ ] Reinstall recharts specifically

**Fix:**
```bash
npm install recharts --save
npm start
```

### CORS/Connection Issues

#### Issue: "CORS error" or "Failed to fetch"
- [ ] Backend running on :8000?
- [ ] Frontend running on :3000?

**Fix:**
```bash
# Terminal 1:
python manage.py runserver

# Terminal 2:
npm start
```

#### Issue: "Connection refused"
- [ ] Backend server running?
- [ ] Port 8000 available?

**Check:**
```bash
# Windows
netstat -ano | findstr :8000

# Mac/Linux
lsof -i :8000
```

---

## 📋 Verification Checklist

### Backend Verification

```bash
# Navigate to backend
cd backend

# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Verify installations
pip list | grep Django
pip list | grep pandas
pip list | grep djangorestframework

# Check data file
ls data/realestate.xlsx  # Mac/Linux
dir data\realestate.xlsx  # Windows

# Test Django
python manage.py check
```

**Expected Output:**
```
System check identified no issues (0 silenced).
```

### Frontend Verification

```bash
# Navigate to frontend
cd frontend

# Verify npm installations
npm list react
npm list recharts
npm list react-scripts

# Check node_modules
ls node_modules | wc -l  # Should show 600+
```

### API Verification

```bash
# While backend is running:
curl -X POST http://localhost:8000/api/query/ \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Analyze Wakad\"}"

# Should return JSON with area, summary, chart, table
```

---

## 📊 Installation Sizes

| Component | Size | Time |
|-----------|------|------|
| Python venv | ~50MB | ~2 min |
| Backend deps | ~25MB | ~3 min |
| Node modules | ~500MB | ~5 min |
| Frontend build | ~200KB | ~30 sec |
| **Total** | **~600MB** | **~10 min** |

---

## 🎯 Post-Installation

### After Successful Installation

1. **Read Documentation**
   - [ ] Read README.md
   - [ ] Read QUICKSTART.md
   - [ ] Review SETUP_GUIDE.md

2. **Test Application**
   - [ ] Start backend
   - [ ] Start frontend
   - [ ] Send test queries
   - [ ] Verify all components

3. **Customize**
   - [ ] Add more data areas
   - [ ] Change color theme
   - [ ] Modify summary format
   - [ ] Test edge cases

4. **Deploy (Optional)**
   - [ ] Heroku backend setup
   - [ ] Vercel frontend setup
   - [ ] Environment configuration
   - [ ] Production testing

---

## 🔑 Key Commands Reference

```bash
# Backend
cd backend
python -m venv venv          # Create venv
venv\Scripts\activate         # Activate (Windows)
source venv/bin/activate      # Activate (Mac/Linux)
pip install -r requirements.txt
python generate_data.py       # Generate sample data
python manage.py runserver    # Start Django

# Frontend
cd frontend
npm install                   # Install deps
npm start                     # Start dev server
npm run build                 # Build for production
npm test                      # Run tests

# Stop servers
Ctrl+C                        # Stop current server
```

---

## ✅ Final Checklist

- [ ] Python 3.8+ installed
- [ ] Node.js 14+ installed
- [ ] Backend dependencies installed
- [ ] Frontend dependencies installed
- [ ] Sample data generated
- [ ] Backend can start
- [ ] Frontend can start
- [ ] API responds to queries
- [ ] UI displays correctly
- [ ] Documentation reviewed

---

**When all checkboxes are marked, you're ready to use the application! 🚀**
