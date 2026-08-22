# 🚀 Quick Start - Make Your App Public in 3 Steps

## The Fastest Way (3 Minutes)

### Step 1: Download ngrok
1. Go to: **https://ngrok.com/download**
2. Click "Download for Windows"
3. Extract the ZIP file anywhere (e.g., Desktop or Downloads)

### Step 2: Start Your App
Open PowerShell in this folder and run:
```powershell
python app.py
```
Keep this window open!

### Step 3: Expose to Internet
Open a **NEW** PowerShell window, navigate to where you extracted ngrok, and run:
```powershell
.\ngrok.exe http 5000
```

**That's it!** Copy the URL that looks like: `https://abc123.ngrok-free.app`

---

## Even Easier - Use the Automated Script

Just run:
```powershell
.\start_public.ps1
```

This script will:
- ✅ Check if your model is trained
- ✅ Detect available tunneling tools
- ✅ Start Flask and expose it automatically

---

## What You'll See

When ngrok starts, you'll see:
```
Forwarding    https://abc123.ngrok-free.app -> http://localhost:5000
```

**Share that URL with anyone!** They can access your app from anywhere in the world.

---

## Troubleshooting

**"Model files not found"**
Run: `python train_model.py`

**"Port 5000 already in use"**
Close other apps using port 5000, or change the port in app.py

**Need more help?**
Check <ref_file file="C:\Users\Chetan_S_P\OneDrive - Dell Technologies\carev-hosted\DEPLOYMENT_GUIDE.md" /> for detailed instructions

---

## 📱 Test Your Public App

Once running:
1. ✅ Open the ngrok URL in your browser
2. ✅ Try it on your phone
3. ✅ Share with friends/colleagues
4. ✅ Use the API from other apps

**Your EV Range Prediction app is now live! 🎉**
