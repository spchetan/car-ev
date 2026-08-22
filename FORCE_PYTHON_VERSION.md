# 🔧 CRITICAL FIX: Force Python 3.10 on Render.com

## ⚠️ Problem Identified!

**Render is using Python 3.14 instead of reading runtime.txt!**

This is why pandas fails - Python 3.14 doesn't have pandas wheels yet.

---

## ✅ SOLUTION: Force Python Version in Render Settings

### **On Render.com Dashboard:**

1. Go to: **https://dashboard.render.com**
2. Click your service: **`ev-range-prediction`**
3. Go to **"Settings"** tab
4. Scroll to **"Environment"** section
5. Click **"Add Environment Variable"**
6. Add this:
   - **Key:** `PYTHON_VERSION`
   - **Value:** `3.10.13`
7. Click **"Save Changes"**

---

## 🎯 Alternative: Specify in Build Settings

### **Method 1: Set Python Version in Environment**

In Render Settings → Environment:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.10.13` |

---

### **Method 2: Update Build Command**

Change your **Build Command** to:

```bash
python3.10 -m pip install --upgrade pip && python3.10 -m pip install -r requirements.txt && python3.10 train_model.py
```

This explicitly uses Python 3.10!

---

### **Method 3: Use .python-version file**

Create a file named `.python-version` (no .txt extension) with:

```
3.10.13
```

---

## 📋 COMPLETE FIX - Do ALL These Steps:

### **Step 1: Verify runtime.txt exists on GitHub**

1. Go to: https://github.com/spchetan/car-ev
2. Check if `runtime.txt` exists
3. Make sure it contains: `python-3.10.13`
4. If not, create it!

---

### **Step 2: Add Environment Variable on Render**

1. Render Dashboard → Your Service → Settings
2. Environment section
3. Add: `PYTHON_VERSION` = `3.10.13`
4. Save

---

### **Step 3: Update Build Command**

Use this **Build Command** on Render:

```bash
python3.10 -m pip install --no-cache-dir --upgrade pip && python3.10 -m pip install --no-cache-dir -r requirements.txt && python3.10 train_model.py
```

---

### **Step 4: Clear Cache & Redeploy**

1. Go to "Manual Deploy"
2. Click **"Clear build cache & deploy"**
3. Watch logs - should now use Python 3.10!

---

## 📊 Expected Log (After Fix):

```
==> Detected Python version from PYTHON_VERSION: 3.10.13 ✅
==> Using Python 3.10.13 ✅
==> Installing dependencies...
==> Installing pandas==2.0.3... ✅ SUCCESS!
==> Build successful! ✅
```

---

## 🐛 Why runtime.txt Might Be Ignored:

### **Common Reasons:**

1. **File not in root directory** - Must be at project root
2. **Wrong file name** - Must be exactly `runtime.txt`
3. **Not pushed to GitHub** - Render can't see it
4. **Render cache** - Old build cached
5. **Render defaults** - Sometimes ignores runtime.txt

---

## ✅ BEST SOLUTION: Create .python-version File

This is more reliable than runtime.txt!

### **Create this file:**

**File name:** `.python-version` (starts with a dot, no extension)

**Content:**
```
3.10.13
```

### **Push to GitHub:**

```bash
cd "C:\Users\Chetan_S_P\OneDrive - Dell Technologies\carev-hosted"

# Create .python-version file
echo 3.10.13 > .python-version

# Push to GitHub
git add .python-version
git commit -m "Add .python-version to force Python 3.10.13"
git push origin main
```

---

## 🎯 Complete Configuration

### **Files to have on GitHub:**

1. **runtime.txt:**
   ```
   python-3.10.13
   ```

2. **.python-version:**
   ```
   3.10.13
   ```

3. **requirements.txt:**
   ```
   flask==3.0.0
   numpy==1.24.3
   pandas==2.0.3
   scikit-learn==1.3.0
   matplotlib==3.7.2
   python-docx==0.8.11
   gunicorn==21.2.0
   ```

### **Render Settings:**

**Environment Variable:**
- Key: `PYTHON_VERSION`
- Value: `3.10.13`

**Build Command:**
```bash
python3.10 -m pip install --no-cache-dir --upgrade pip && python3.10 -m pip install --no-cache-dir -r requirements.txt && python3.10 train_model.py
```

**Start Command:**
```bash
gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app
```

---

## 🚀 Quick Fix Steps:

### **Right Now, Do This:**

1. **On Render Dashboard:**
   - Settings → Environment
   - Add: `PYTHON_VERSION` = `3.10.13`
   - Save

2. **Update Build Command:**
   ```
   python3.10 -m pip install --no-cache-dir --upgrade pip && python3.10 -m pip install --no-cache-dir -r requirements.txt && python3.10 train_model.py
   ```

3. **Clear Cache & Deploy:**
   - Manual Deploy → Clear build cache & deploy

4. **Watch Logs:**
   - Should now show "Using Python 3.10.13"

---

## 📸 What to Look for in Logs:

### **BEFORE (Wrong):**
```
==> Using Python 3.14.x ❌
==> Installing pandas... FAILED ❌
```

### **AFTER (Correct):**
```
==> Using Python 3.10.13 ✅
==> Installing pandas==2.0.3... SUCCESS ✅
```

---

## 🔍 Debug: Check Python Version

Add this to your Build Command temporarily to verify:

```bash
python3 --version && python3.10 -m pip install --no-cache-dir --upgrade pip && python3.10 -m pip install --no-cache-dir -r requirements.txt && python3.10 train_model.py
```

This will show which Python version Render is using!

---

## 💡 Alternative: Use Render Blueprint

Create `render.yaml` with explicit Python version:

```yaml
services:
  - type: web
    name: ev-range-prediction
    env: python
    runtime: python
    region: oregon
    plan: free
    branch: main
    buildCommand: "pip install --no-cache-dir -r requirements.txt && python train_model.py"
    startCommand: "gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app"
    envVars:
      - key: PYTHON_VERSION
        value: "3.10.13"
```

---

## ✅ Checklist:

- [ ] Add `PYTHON_VERSION=3.10.13` environment variable on Render
- [ ] Update Build Command to use `python3.10`
- [ ] Create `.python-version` file with `3.10.13`
- [ ] Verify `runtime.txt` exists on GitHub
- [ ] Clear build cache on Render
- [ ] Redeploy
- [ ] Check logs show Python 3.10.13

---

## 🎯 CRITICAL ACTIONS:

### **1. Add Environment Variable (NOW!):**

Render Dashboard → Settings → Environment:
```
PYTHON_VERSION = 3.10.13
```

### **2. Update Build Command:**

```bash
python3.10 -m pip install --no-cache-dir --upgrade pip && python3.10 -m pip install --no-cache-dir -r requirements.txt && python3.10 train_model.py
```

### **3. Deploy:**

Clear cache & deploy!

---

## 📞 If Still Using Python 3.14:

### **Contact Render Support:**

1. Go to Render Dashboard
2. Click "Help" or "Support"
3. Ask: "Why is my service using Python 3.14 instead of 3.10.13 specified in runtime.txt?"

### **Or Try Different Region:**

Sometimes different Render regions have different Python defaults.
Try changing region in Settings.

---

## 🚀 This WILL Fix It!

**Adding `PYTHON_VERSION` environment variable forces Render to use Python 3.10!**

**Do it NOW and redeploy!** ✅
