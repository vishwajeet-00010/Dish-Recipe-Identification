# 🚀 Complete Setup Guide - Food Ingredient Detection System

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [Testing](#testing)
6. [Troubleshooting](#troubleshooting)
7. [Optional: Gemini AI Integration](#optional-gemini-ai-integration)

---

## 1. Prerequisites

### Required Software
- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **Modern web browser** (Chrome, Firefox, Edge, Safari)

### System Requirements
- **RAM**: 2GB minimum (4GB recommended)
- **Disk Space**: 1GB free space
- **Internet**: Required for initial model download and Gemini API (optional)

---

## 2. Installation

### Step 1: Navigate to Project Directory

```bash
cd "C:\Users\ADESH\Desktop\scripts personal\meal analyze"
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**
- Flask 3.0.0 - Web framework
- flask-cors 4.0.0 - CORS support
- tensorflow 2.15.0 - ML framework
- Pillow 10.1.0 - Image processing
- numpy 1.24.3 - Numerical computing
- Werkzeug 3.0.1 - WSGI utilities
- google-generativeai 0.3.2 - Gemini AI (optional)

**Installation time:** 5-10 minutes (TensorFlow is large)

### Step 3: Verify Installation

```bash
python -c "import tensorflow; print('TensorFlow version:', tensorflow.__version__)"
```

Expected output: `TensorFlow version: 2.15.0`

---

## 3. Configuration

### Basic Configuration (No Changes Needed)

The system works out-of-the-box with default settings:
- Backend port: 5000
- Frontend port: 8000
- Model: EfficientNetB0 (auto-downloaded on first run)
- Food database: 250+ foods included

### Optional: Gemini AI Configuration

See [Section 7](#optional-gemini-ai-integration) for Gemini setup.

---

## 4. Running the Application

### Method 1: Using Two Terminals (Recommended)

**Terminal 1 - Backend Server:**
```bash
cd "C:\Users\ADESH\Desktop\scripts personal\meal analyze"
python app.py
```

Wait for: `* Running on http://127.0.0.1:5000`

**Terminal 2 - Frontend Server:**
```bash
cd "C:\Users\ADESH\Desktop\scripts personal\meal analyze"
python -m http.server 8000
```

Wait for: `Serving HTTP on :: port 8000`

### Method 2: Using Batch File (Windows)

Create `start.bat`:
```batch
@echo off
start cmd /k "python app.py"
timeout /t 3
start cmd /k "python -m http.server 8000"
start http://localhost:8000
```

Double-click `start.bat` to launch everything.

### Accessing the Application

Open your browser and navigate to:
```
http://localhost:8000
```

You should see the Food Ingredient Detector interface.

---

## 5. Testing

### Quick Health Check

**Test Backend:**
```bash
curl http://localhost:5000/health
```

Expected response:
```json
{"status": "healthy", "model_loaded": true}
```

**Test Frontend:**
Open `http://localhost:8000` in browser - you should see the UI.

### Testing with Sample Images

1. Navigate to the `test_images/` folder
2. Upload any image through the web interface
3. Click "Analyze Food"

**Expected Results:**
| Image | Expected Detection | Confidence |
|-------|-------------------|------------|
| pizza.png | Pizza | 85-90% |
| burger.png | Burger | 90-95% |
| sushi.png | Sushi | 75-85% |
| ramen.png | Ramen | 20-30% |
| pasta.png | Pasta | 75-85% |
| cake.png | Cake/Trifle | Variable |

---

## 6. Troubleshooting

### Issue: "Port already in use"

**Problem:** Port 5000 or 8000 is occupied

**Solution:**
```bash
# Windows - Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or use different ports
python app.py --port 5001
python -m http.server 8001
```

### Issue: "Module not found"

**Problem:** Dependencies not installed

**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "TensorFlow not loading"

**Problem:** TensorFlow installation issue

**Solution:**
```bash
pip uninstall tensorflow
pip install tensorflow==2.15.0
```

### Issue: "Model download fails"

**Problem:** Network issues during first run

**Solution:**
- Ensure stable internet connection
- Wait for model download (14-21MB)
- Retry if interrupted

### Issue: "CORS errors in browser"

**Problem:** Frontend can't connect to backend

**Solution:**
- Ensure both servers are running
- Check `http://localhost:5000/health`
- Clear browser cache
- Try different browser

### Issue: "Low accuracy / wrong predictions"

**Expected Behavior:**
- ImageNet has limited food classes
- Some cuisines (especially Indian) may have lower accuracy
- This is normal for transfer learning

**Solutions:**
- Use clear, well-lit images
- Single food item per image
- Consider enabling Gemini AI validation

---

## 7. Optional: Gemini AI Integration

Gemini AI provides intelligent validation for low-confidence predictions.

### Step 1: Get FREE API Key

1. Visit: https://aistudio.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key (starts with `AIza...`)

**No credit card required!**

### Step 2: Configure API Key

**Option A: Environment Variable (Recommended)**

Windows PowerShell:
```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
python app.py
```

**Option B: Hardcode in app.py**

Open `app.py` and find line ~22:
```python
GEMINI_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your key
```

### Step 3: Verify Gemini is Working

Restart the backend server and look for:
```
✅ Gemini initialized: gemini-1.5-flash
```

### Step 4: Test Gemini Validation

Upload an image with expected low confidence (like ramen or dosa).

You should see in terminal:
```
🔍 Primary Model: ramen (20.0%)
🤖 Low confidence - asking Gemini for validation...
✅ Gemini confirmed: ramen
```

### Gemini Features

- **Automatic Validation**: Triggers when confidence < 70%
- **Smart Corrections**: Knows common misclassifications
- **Free Tier**: 1,500 requests/day
- **Text-Based**: Works without vision models

### Disabling Gemini

To disable Gemini (system works fine without it):

In `app.py`:
```python
GEMINI_API_KEY = None  # Disabled
```

---

## 8. Project Structure

```
meal-analyze/
├── app.py                    # Flask backend server
├── backend_model.py          # ML model logic
├── gemini_validator.py       # Gemini AI integration
├── ingredient_map.py         # Food database (250+ foods)
├── requirements.txt          # Python dependencies
├── index.html                # Frontend UI
├── frontend_css.css          # Styling
├── frontend_js.js            # Frontend logic
├── test_images/              # Sample test images
│   ├── pizza.png
│   ├── burger.png
│   ├── sushi.png
│   ├── ramen.png
│   ├── pasta.png
│   └── cake.png
├── README.md                 # Project documentation
├── PRESENTATION.md           # Presentation guide
└── SETUP.md                  # This file
```

---

## 9. Common Workflows

### Daily Development

```bash
# Start servers
python app.py                    # Terminal 1
python -m http.server 8000       # Terminal 2

# Open browser
start http://localhost:8000

# Stop servers
Ctrl+C in each terminal
```

### Adding New Foods

1. Open `ingredient_map.py`
2. Add entry:
```python
'new_food': ['ingredient1', 'ingredient2', 'ingredient3']
```
3. Restart backend server

### Updating Model

To use a different model, edit `backend_model.py`:
```python
# Change this line
self.model = EfficientNetB0(weights='imagenet')

# To (example)
self.model = MobileNetV2(weights='imagenet')
```

---

## 10. Performance Optimization

### For Faster Inference

1. **Use GPU** (if available):
```bash
pip install tensorflow-gpu==2.15.0
```

2. **Reduce Image Size**:
In `backend_model.py`, change:
```python
self.img_size = (224, 224)  # Default
# To
self.img_size = (160, 160)  # Faster, slightly less accurate
```

3. **Enable Caching**:
Add caching for repeated predictions (advanced).

---

## 11. Deployment Options

### Local Network Access

Allow other devices on your network to access:

```bash
# Backend
python app.py --host 0.0.0.0

# Frontend
python -m http.server 8000 --bind 0.0.0.0
```

Access from other devices: `http://YOUR_IP:8000`

### Cloud Deployment

**Recommended Platforms:**
- Heroku (Free tier)
- Google Cloud Run
- AWS EC2
- DigitalOcean

See `README.md` for deployment guides.

---

## 12. Security Notes

### For Production

1. **Remove API Key from Code**:
   - Use environment variables
   - Never commit to Git

2. **Add Authentication**:
   - Implement user login
   - Rate limiting

3. **HTTPS**:
   - Use SSL certificates
   - Secure connections

4. **Input Validation**:
   - Already implemented
   - File size limits
   - Type checking

---

## 13. Getting Help

### Resources

- **README.md** - Full documentation
- **PRESENTATION.md** - Presentation guide
- **Code Comments** - Inline documentation

### Common Questions

**Q: Why is accuracy low for some foods?**
A: ImageNet dataset bias. Fine-tune on Food-101 for better results.

**Q: Can it detect multiple foods?**
A: No, currently single food only. Use object detection for multi-food.

**Q: Is Gemini required?**
A: No, it's optional. System works great without it.

**Q: How to add more foods?**
A: Edit `ingredient_map.py` and add entries.

---

## 14. Quick Reference

### Start Application
```bash
python app.py                    # Backend
python -m http.server 8000       # Frontend
```

### Access Points
- **Frontend**: http://localhost:8000
- **Backend API**: http://localhost:5000
- **Health Check**: http://localhost:5000/health

### Stop Application
- Press `Ctrl+C` in each terminal

### Test Images
- Located in `test_images/` folder
- 6 professional samples included

---

## ✅ Setup Complete!

You're now ready to use the Food Ingredient Detection System!

**Next Steps:**
1. ✅ Start both servers
2. ✅ Open http://localhost:8000
3. ✅ Upload a test image
4. ✅ See the magic happen!

**For Presentation:**
- Review `PRESENTATION.md`
- Practice with test images
- Understand the architecture

---

**Need Help?** Check the troubleshooting section or review the code comments.

**Good luck! 🚀**
