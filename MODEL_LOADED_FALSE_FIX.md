# 🔧 Fix: model_loaded: false Error

## ⚠️ Problem: Health endpoint shows `"model_loaded": false`

This means the model training is either:
1. Not running during build
2. Failing silently
3. CSV file not on GitHub yet

---

## 🔍 Diagnosis Steps

### **Step 1: Check if CSV is on GitHub**

1. Go to: https://github.com/spchetan/car-ev
2. Look for `ev_telemetry_data.csv` in the file list
3. **If NOT there** → CSV wasn't pushed (see Solution A)
4. **If there** → Model training is failing (see Solution B)

---

## ✅ SOLUTION A: CSV Not on GitHub Yet

### **Push the CSV file NOW:**

```bash
cd "C:\Users\Chetan_S_P\OneDrive - Dell Technologies\carev-hosted"

# Force add the CSV file
git add -f ev_telemetry_data.csv

# Also add updated .gitignore
git add .gitignore

# Commit
git commit -m "Add training data CSV file"

# Push
git push origin main
```

**Wait 3-5 minutes for Render to redeploy.**

---

## ✅ SOLUTION B: Model Training Failing

### **Check Render Build Logs:**

1. Go to: https://dashboard.render.com
2. Click your service
3. Click **"Logs"** tab
4. Look for errors in model training

### **Common Issues:**

#### **Issue 1: CSV file not found**
```
FileNotFoundError: ev_telemetry_data.csv
```
**Fix:** Push CSV to GitHub (Solution A)

#### **Issue 2: Model training timeout**
```
Build exceeded timeout
```
**Fix:** Increase timeout (already set to 600s)

#### **Issue 3: Import errors**
```
ModuleNotFoundError: No module named 'pandas'
```
**Fix:** Already fixed with Python 3.10

---

## ✅ SOLUTION C: Train Model in Start Command

If build keeps failing, train the model when the app starts:

### **Update Render Settings:**

**Build Command:**
```bash
python3.10 -m pip install --no-cache-dir --upgrade pip && python3.10 -m pip install --no-cache-dir -r requirements.txt
```

**Start Command:**
```bash
python3.10 train_model.py && gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app
```

This trains the model during startup instead of build!

---

## ✅ SOLUTION D: Simplify train_model.py

The current script might be too complex. Let's create a simpler version:

### **Create: simple_train.py**

```python
import pandas as pd
import pickle
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

print("Loading dataset...")
try:
    df = pd.read_csv('ev_telemetry_data.csv')
    print(f"Loaded {len(df)} samples")
except Exception as e:
    print(f"ERROR loading CSV: {e}")
    exit(1)

# Features
num_cols = ['soc', 'battery_temp', 'ambient_temp', 'speed', 'hvac_power', 
            'tire_pressure', 'payload_kg', 'elevation_change']
cat_cols = ['drive_mode', 'weather', 'road_type']

X = df[num_cols + cat_cols]
y = df['remaining_range_km']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training model...")
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
])

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(n_estimators=100, random_state=42))
])

model.fit(X_train, y_train)

# Save model
with open('ev_range_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save metadata
feature_metadata = {
    'num_cols': num_cols,
    'cat_cols': cat_cols,
    'feature_order': num_cols + cat_cols
}
with open('feature_metadata.pkl', 'wb') as f:
    pickle.dump(feature_metadata, f)

print("Model saved successfully!")
print(f"Train score: {model.score(X_train, y_train):.4f}")
print(f"Test score: {model.score(X_test, y_test):.4f}")
```

### **Update Build Command:**
```bash
python3.10 -m pip install --no-cache-dir --upgrade pip && python3.10 -m pip install --no-cache-dir -r requirements.txt && python3.10 simple_train.py
```

---

## ✅ SOLUTION E: Check File Permissions

### **Update app.py to show more debug info:**

Add this to the top of `load_model()` function:

```python
def load_model():
    global model, feature_metadata
    import os
    
    # Debug: Check if files exist
    print("Current directory:", os.getcwd())
    print("Files in directory:", os.listdir('.'))
    print("Model file exists:", os.path.exists('ev_range_model.pkl'))
    print("Metadata file exists:", os.path.exists('feature_metadata.pkl'))
    
    try:
        with open('ev_range_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('feature_metadata.pkl', 'rb') as f:
            feature_metadata = pickle.load(f)
        print("Model loaded successfully!")
        return True
    except FileNotFoundError as e:
        print(f"Model files not found: {e}")
        return False
    except Exception as e:
        print(f"Error loading model: {e}")
        return False
```

This will show in logs why the model isn't loading!

---

## 🎯 IMMEDIATE ACTION PLAN

### **Do These Steps in Order:**

### **1. Verify CSV is on GitHub**
```bash
# Check locally
ls -la ev_telemetry_data.csv

# Push to GitHub
git add -f ev_telemetry_data.csv
git add .gitignore
git commit -m "Add training data CSV"
git push origin main
```

### **2. Check Render Build Logs**
- Go to Render dashboard
- Click "Logs"
- Look for "Loading dataset..." and "Model saved"
- **Share the error if you see one**

### **3. If Build Succeeds but Model Still Not Loading**

Update **Start Command** on Render to:
```bash
python3.10 train_model.py && gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app
```

This ensures model is trained before app starts!

### **4. Manual Deploy**
- Go to Render dashboard
- Click "Manual Deploy"
- Select "Clear build cache & deploy"
- Watch the logs carefully

---

## 📊 What to Look For in Logs

### **SUCCESS - You should see:**
```
==> Running build command...
Loading dataset... ✅
Loaded 5000 samples ✅
Training model... ✅
Model saved successfully! ✅

==> Starting service...
Current directory: /opt/render/project/src
Files in directory: [..., 'ev_range_model.pkl', ...]
Model file exists: True ✅
Model loaded successfully! ✅
```

### **FAILURE - If you see:**
```
FileNotFoundError: ev_telemetry_data.csv ❌
```
→ CSV not on GitHub, push it!

```
Model file exists: False ❌
```
→ Training didn't run or failed

```
Error loading model: ... ❌
```
→ Model file corrupted or incompatible

---

## 🔧 Quick Fix: Generate Data on the Fly

If CSV upload keeps failing, generate data during build:

### **Create: generate_data.py**

```python
import pandas as pd
import numpy as np

print("Generating synthetic training data...")
np.random.seed(42)
n = 5000

data = {
    'soc': np.random.uniform(0, 100, n),
    'battery_temp': np.random.uniform(-20, 60, n),
    'ambient_temp': np.random.uniform(-20, 40, n),
    'speed': np.random.uniform(0, 120, n),
    'hvac_power': np.random.uniform(0, 5, n),
    'tire_pressure': np.random.uniform(28, 36, n),
    'payload_kg': np.random.uniform(0, 500, n),
    'elevation_change': np.random.uniform(-100, 100, n),
    'drive_mode': np.random.choice(['eco', 'normal', 'sport'], n),
    'weather': np.random.choice(['clear', 'rain', 'snow', 'fog'], n),
    'road_type': np.random.choice(['city', 'highway', 'mixed'], n),
}

# Calculate realistic range
base = data['soc'] * 4.5
temp_adj = 1 - abs(data['ambient_temp'] - 20) * 0.005
speed_adj = 1 - abs(data['speed'] - 60) * 0.003
data['remaining_range_km'] = base * temp_adj * speed_adj

df = pd.DataFrame(data)
df.to_csv('ev_telemetry_data.csv', index=False)
print(f"Generated {len(df)} samples → ev_telemetry_data.csv")
```

### **Update Build Command:**
```bash
python3.10 generate_data.py && python3.10 -m pip install --no-cache-dir --upgrade pip && python3.10 -m pip install --no-cache-dir -r requirements.txt && python3.10 train_model.py
```

This generates data during build - no CSV upload needed!

---

## ✅ Recommended Solution

### **Best Approach:**

1. **Push CSV to GitHub** (most reliable)
2. **Train during startup** (if build fails)
3. **Generate data on the fly** (if CSV too large)

### **Current Best Settings:**

**Build Command:**
```bash
python3.10 -m pip install --no-cache-dir --upgrade pip && python3.10 -m pip install --no-cache-dir -r requirements.txt
```

**Start Command:**
```bash
python3.10 train_model.py && gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app
```

This trains model during startup - guaranteed to work!

---

## 🚨 DO THIS NOW:

### **1. Push CSV to GitHub:**
```bash
git add -f ev_telemetry_data.csv
git add .gitignore
git commit -m "Add training data"
git push origin main
```

### **2. Update Render Start Command:**
```
python3.10 train_model.py && gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app
```

### **3. Redeploy:**
- Clear cache & deploy on Render

### **4. Check Health:**
```
https://your-app.onrender.com/health
```
Should show: `"model_loaded": true` ✅

---

## 📞 If Still Not Working

**Share these from Render logs:**
1. Build log output
2. Startup log output
3. Any error messages

I'll help you debug further!

---

**Training model during startup is the most reliable solution!** ✅
