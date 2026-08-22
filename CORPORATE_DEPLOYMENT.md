# 🏢 Corporate Environment Deployment Guide

Your app is blocked by Application Control policies. Here are approved alternatives:

## ✅ Option 1: VS Code Port Forwarding (RECOMMENDED)

**Best for:** Quick demos, testing, Dell corporate environment

### Steps:
1. **Install VS Code** (if not already installed)
   - Download from: https://code.visualstudio.com/

2. **Open your project in VS Code**
   ```powershell
   code .
   ```

3. **Start your Flask app**
   ```powershell
   python app.py
   ```

4. **Forward the port:**
   - Press `Ctrl+Shift+P`
   - Type "Forward a Port"
   - Enter `5000`
   - Click the globe icon to make it **Public**
   - Copy the URL (e.g., `https://abc123-5000.preview.app.github.dev`)

5. **Share the URL!** Anyone can access it now.

**Pros:**
- ✅ Works in corporate environments
- ✅ No installation needed
- ✅ Automatic HTTPS
- ✅ Easy to use

**Cons:**
- ⚠️ Requires VS Code to be running
- ⚠️ Session-based (not permanent)

---

## ✅ Option 2: Deploy to Render.com (FREE)

**Best for:** Permanent deployment, 24/7 availability

### Steps:

1. **Create a GitHub repository** (if you haven't already)
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Sign up at Render.com**
   - Go to: https://render.com
   - Sign up with GitHub

3. **Create a New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repo

4. **Configure the service:**
   - **Name**: `ev-range-prediction`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python train_model.py`
   - **Start Command**: `python app.py`
   - **Instance Type**: `Free`

5. **Deploy!**
   - Click "Create Web Service"
   - Wait 2-3 minutes for deployment
   - You'll get a URL like: `https://ev-range-prediction.onrender.com`

**Pros:**
- ✅ Free tier available
- ✅ Permanent URL
- ✅ Automatic HTTPS
- ✅ Auto-deploys on git push
- ✅ 24/7 availability

**Cons:**
- ⚠️ Free tier spins down after inactivity (takes 30s to wake up)

---

## ✅ Option 3: Deploy to Railway.app (FREE)

**Best for:** Quick deployment, modern interface

### Steps:

1. **Push code to GitHub** (same as Option 2, step 1)

2. **Sign up at Railway.app**
   - Go to: https://railway.app
   - Sign up with GitHub

3. **Deploy:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway auto-detects Python and deploys!

4. **Get your URL:**
   - Go to Settings → Generate Domain
   - You'll get: `https://your-app.up.railway.app`

**Pros:**
- ✅ Easiest deployment
- ✅ Auto-detects everything
- ✅ Free $5/month credit
- ✅ Fast deployment

---

## ✅ Option 4: Use Your Network IP (LAN Access)

**Best for:** Sharing within your office/network

Your app is already accessible on your local network at:
```
http://10.17.10.124:5000
```

Anyone on the same network (office WiFi, VPN) can access this URL!

**To find your IP:**
```powershell
ipconfig
```
Look for "IPv4 Address"

**Pros:**
- ✅ Already working!
- ✅ No setup needed
- ✅ Fast (local network)

**Cons:**
- ⚠️ Only works on same network
- ⚠️ Not accessible from internet
- ⚠️ Your computer must stay on

---

## ✅ Option 5: Azure App Service (Dell Approved)

**Best for:** Enterprise deployment, Dell-approved platform

Since you're at Dell, you likely have access to Azure:

### Steps:

1. **Create requirements.txt** (already exists)

2. **Create startup.sh:**
   ```bash
   python train_model.py
   gunicorn --bind=0.0.0.0 --timeout 600 app:app
   ```

3. **Add gunicorn to requirements.txt:**
   ```
   gunicorn==21.2.0
   ```

4. **Deploy to Azure:**
   ```powershell
   az login
   az webapp up --name ev-range-prediction --runtime PYTHON:3.11
   ```

5. **Access your app:**
   - URL: `https://ev-range-prediction.azurewebsites.net`

---

## 📊 Comparison Table

| Method | Setup Time | Cost | Permanent | Corporate-Friendly |
|--------|------------|------|-----------|-------------------|
| VS Code Port Forward | 2 min | Free | No | ✅ Yes |
| Render.com | 10 min | Free | Yes | ✅ Yes |
| Railway.app | 5 min | Free* | Yes | ✅ Yes |
| Network IP | 0 min | Free | No | ✅ Yes |
| Azure App Service | 15 min | Paid | Yes | ✅ Yes |

*Railway: $5/month free credit

---

## 🚀 Quick Start (VS Code Method)

The fastest way right now:

1. Open VS Code
2. Open terminal in VS Code
3. Run: `python app.py`
4. Press `Ctrl+Shift+P` → "Forward a Port" → Enter `5000`
5. Make it public (click globe icon)
6. Share the URL!

---

## 🔒 Security Notes

- Your app is currently in DEBUG mode - disable for production
- Consider adding authentication for sensitive data
- Use environment variables for secrets
- Enable CORS if needed for API access

---

## 📞 Need Help?

- VS Code Port Forwarding: https://code.visualstudio.com/docs/editor/port-forwarding
- Render.com Docs: https://render.com/docs
- Railway Docs: https://docs.railway.app
- Azure App Service: https://docs.microsoft.com/azure/app-service/

---

**Your app is ready to share! Choose the method that works best for you.** 🎉
