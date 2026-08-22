# 🚀 Complete Guide: Upload to GitHub & Deploy to Internet

## 📋 Overview

This guide will help you:
1. Upload your entire project folder to GitHub
2. Deploy it to the internet (FREE)
3. Get a public URL to share

**Total Time:** 10-15 minutes

---

## Part 1: Upload to GitHub (5 minutes)

### Option A: Using GitHub Website (Easiest)

1. **Go to GitHub**
   - Visit: https://github.com/spchetan/car-ev
   - Make sure you're logged in

2. **Upload Files**
   - Click the **"Add file"** dropdown button
   - Select **"Upload files"**
   - Drag and drop your entire project folder OR click "choose your files"
   - Select all files from: `C:\Users\Chetan_S_P\OneDrive - Dell Technologies\carev-hosted`

3. **Important Files to Upload:**
   ```
   ✅ index.html
   ✅ app.py
   ✅ train_model.py
   ✅ requirements.txt
   ✅ render.yaml
   ✅ railway.json
   ✅ Procfile
   ✅ runtime.txt
   ✅ start.sh
   ✅ wsgi.py
   ✅ .gitignore
   
   ❌ DON'T upload:
   - *.pkl files (model files - too large)
   - *.csv files (data files)
   - *.pptx, *.docx files
   - templates/ folder
   ```

4. **Commit Changes**
   - Scroll down
   - Add commit message: "Upload complete project with deployment configs"
   - Click **"Commit changes"**

5. **Verify Upload**
   - Check your repo: https://github.com/spchetan/car-ev
   - You should see all the files listed

---

### Option B: Using Git Command Line

```bash
# Navigate to your project folder
cd "C:\Users\Chetan_S_P\OneDrive - Dell Technologies\carev-hosted"

# Initialize git (if not already done)
git init

# Add remote repository
git remote add origin https://github.com/spchetan/car-ev.git

# Add all files
git add .

# Commit
git commit -m "Upload complete project with deployment configurations"

# Push to GitHub
git push -u origin main
```

If `main` doesn't work, try:
```bash
git push -u origin master
```

---

## Part 2: Deploy to Internet (5-10 minutes)

### 🎯 Recommended: Render.com (FREE & Easy)

#### Step 1: Sign Up

1. Go to: **https://render.com**
2. Click **"Get Started for Free"**
3. Sign up with your GitHub account
4. Authorize Render to access your repositories

---

#### Step 2: Create Web Service

1. Click **"New +"** (top right)
2. Select **"Web Service"**
3. Find and select: **`spchetan/car-ev`**
4. Click **"Connect"**

---

#### Step 3: Configure Service

Fill in these exact values:

| Field | Value |
|-------|-------|
| **Name** | `ev-range-prediction` |
| **Region** | Oregon (US West) |
| **Branch** | `main` (or `master`) |
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt && python train_model.py` |
| **Start Command** | `gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app` |
| **Instance Type** | Free |

---

#### Step 4: Deploy

1. Click **"Create Web Service"**
2. Wait 3-5 minutes (watch the logs)
3. You'll see:
   ```
   ==> Installing dependencies...
   ==> Training model...
   ==> Build successful!
   ==> Your service is live!
   ```

---

#### Step 5: Get Your URL

Once deployed:
- You'll see a green **"Live"** badge
- Your URL will be: `https://ev-range-prediction.onrender.com`
- Click it to open your app!

---

## 🎉 Your App is Now Live!

### Your Public URL:
```
https://ev-range-prediction.onrender.com
```
(or whatever name you chose)

### Share it with:
- ✅ Colleagues
- ✅ Clients
- ✅ Friends
- ✅ Anyone in the world!

---

## 📱 Features You Get:

- ✅ **Permanent URL** - Doesn't change
- ✅ **HTTPS Security** - Automatic SSL
- ✅ **24/7 Availability** - Always online
- ✅ **Auto-Deploy** - Push to GitHub → Auto-updates
- ✅ **Free Hosting** - No cost
- ✅ **Global Access** - Works worldwide

---

## 🔄 Update Your App Later

To update your live app:

1. **Make changes** to your code locally
2. **Upload to GitHub** (using website or git)
3. **Render auto-deploys** - Your app updates automatically!

---

## ⚠️ Important Notes

### Free Tier Limitations:

**Render.com Free Tier:**
- ✅ 750 hours/month (enough for 24/7)
- ⚠️ Spins down after 15 min of inactivity
- ⚠️ Takes ~30 seconds to wake up on first request
- ✅ 512 MB RAM
- ✅ Shared CPU

### Keep Your App Awake:

Use **UptimeRobot** to ping your app every 5 minutes:

1. Go to: https://uptimerobot.com
2. Sign up (free)
3. Add New Monitor:
   - Type: HTTP(s)
   - URL: Your Render URL
   - Interval: 5 minutes
4. Your app stays awake! 🎉

---

## 🐛 Troubleshooting

### Issue: Build Failed on Render

**Check:**
1. Go to Render dashboard
2. Click "Logs" tab
3. Look for error messages

**Common fixes:**
- Make sure `requirements.txt` is uploaded
- Verify `train_model.py` exists
- Check Python version in `runtime.txt`

### Issue: App Not Loading

**Solution:**
1. Wait 30 seconds (free tier wakes up)
2. Refresh the page
3. Check Render dashboard for "Live" status

### Issue: Model Training Timeout

**Solution:**
Already handled! Timeout is set to 600 seconds in the start command.

---

## 🎯 Quick Reference

### Your Resources:
- **GitHub Repo:** https://github.com/spchetan/car-ev
- **Deploy Platform:** https://render.com
- **Your Dashboard:** https://dashboard.render.com

### Build Command:
```bash
pip install -r requirements.txt && python train_model.py
```

### Start Command:
```bash
gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app
```

---

## 📊 Alternative Platforms (If Render Doesn't Work)

### Option 2: Railway.app

1. Go to: https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `spchetan/car-ev`
5. Add start command in Settings:
   ```
   python train_model.py && gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app
   ```
6. Generate Domain in Settings
7. Done!

**Your URL:** `https://car-ev-production.up.railway.app`

---

### Option 3: Vercel

1. Go to: https://vercel.com
2. Sign up with GitHub
3. Import `spchetan/car-ev`
4. Deploy
5. Done!

**Your URL:** `https://car-ev.vercel.app`

---

## ✅ Checklist

### Before Deploying:

- [ ] All files uploaded to GitHub
- [ ] Verified files at: https://github.com/spchetan/car-ev
- [ ] `requirements.txt` includes gunicorn
- [ ] `app.py` uses PORT environment variable
- [ ] `index.html` is in root directory

### After Deploying:

- [ ] Service shows "Live" status
- [ ] URL opens successfully
- [ ] App interface loads
- [ ] Can make predictions
- [ ] Shared URL with others

---

## 🎯 Step-by-Step Summary

### 1️⃣ Upload to GitHub
- Go to https://github.com/spchetan/car-ev
- Click "Add file" → "Upload files"
- Upload all project files
- Commit changes

### 2️⃣ Deploy on Render
- Go to https://render.com
- Sign up with GitHub
- New + → Web Service
- Connect `spchetan/car-ev`
- Use the commands above
- Create Web Service

### 3️⃣ Get Your URL
- Wait 3-5 minutes
- Copy your URL
- Share with the world! 🌍

---

## 🎉 That's It!

Your EV Range Prediction app will be:
- ✅ Live on the internet
- ✅ Accessible from anywhere
- ✅ Free to use
- ✅ Automatically secured with HTTPS
- ✅ Ready to share!

**Total Time:** 10-15 minutes from start to finish

---

## 📞 Need Help?

- **Render Docs:** https://render.com/docs
- **Railway Docs:** https://docs.railway.app
- **GitHub Help:** https://docs.github.com

---

## 🚀 Ready? Let's Go!

1. Upload to GitHub: https://github.com/spchetan/car-ev
2. Deploy on Render: https://render.com
3. Enjoy your live app! 🎉

**Good luck!** 🌟
