# 🎯 Render.com Deployment - Step by Step

## Complete visual guide to deploy your app in 5 minutes

---

## 📋 Prerequisites

- ✅ Code on GitHub: https://github.com/spchetan/car-ev
- ✅ Deployment files pushed (see PUSH_TO_GITHUB.md)
- ✅ GitHub account

---

## 🚀 Step-by-Step Deployment

### Step 1: Go to Render.com

1. Open your browser
2. Go to: **https://render.com**
3. Click **"Get Started for Free"** button

---

### Step 2: Sign Up with GitHub

1. Click **"GitHub"** button
2. Authorize Render to access your GitHub
3. You'll be redirected to Render dashboard

---

### Step 3: Create New Web Service

1. Click the **"New +"** button (top right corner)
2. Select **"Web Service"** from the dropdown
3. You'll see "Create a new Web Service" page

---

### Step 4: Connect Your Repository

**First time:**
1. Click **"Connect account"** next to GitHub
2. Authorize Render to access your repositories
3. You can choose "All repositories" or "Only select repositories"
4. Select `spchetan/car-ev` if choosing specific repos

**After authorization:**
1. Find your repository: `spchetan/car-ev`
2. Click **"Connect"** button next to it

---

### Step 5: Configure Your Service

Fill in the form with these exact values:

#### Basic Settings:

**Name:**
```
ev-range-prediction
```
(or any name you prefer - this will be in your URL)

**Region:**
```
Oregon (US West)
```
(or choose closest to your location)

**Branch:**
```
main
```
(or `master` if that's your default branch)

**Root Directory:**
```
(leave blank)
```

**Runtime:**
```
Python 3
```
(should be auto-detected)

---

#### Build & Deploy Settings:

**Build Command:**
```
pip install -r requirements.txt && python train_model.py
```

**Start Command:**
```
gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app
```

---

#### Instance Type:

Select: **Free**
- 512 MB RAM
- Shared CPU
- Perfect for this app!

---

### Step 6: Advanced Settings (Optional)

Click **"Advanced"** to expand:

**Auto-Deploy:**
- ✅ Keep "Yes" checked
- Your app will auto-update when you push to GitHub

**Environment Variables:**
- Not needed for now
- Can add later if needed

---

### Step 7: Create Web Service

1. Review all settings
2. Click **"Create Web Service"** button (bottom of page)
3. You'll be redirected to your service dashboard

---

### Step 8: Watch Deployment

You'll see the deployment logs in real-time:

```
==> Cloning from https://github.com/spchetan/car-ev...
==> Checking out commit abc123...
==> Running build command: pip install -r requirements.txt && python train_model.py
==> Installing dependencies...
==> Training model...
==> Build successful!
==> Starting service...
==> Your service is live!
```

**This takes 3-5 minutes**

---

### Step 9: Get Your URL

Once deployment is complete:

1. You'll see a green **"Live"** badge
2. Your URL will be displayed at the top:
   ```
   https://ev-range-prediction.onrender.com
   ```
3. Click the URL to open your app!

---

### Step 10: Test Your App

1. Click your URL
2. You should see your EV Range Prediction interface
3. Try making a prediction!
4. Share the URL with anyone!

---

## 🎉 Congratulations!

Your app is now live on the internet! 🌍

### Your App URL:
```
https://ev-range-prediction.onrender.com
```
(replace with your actual URL)

---

## 📱 What You Can Do Now

### Share Your App:
- ✅ Send URL via email, Slack, Teams
- ✅ Open on mobile devices
- ✅ Share with colleagues/clients
- ✅ Use in presentations

### Monitor Your App:
- View logs in Render dashboard
- Check deployment history
- Monitor resource usage
- See request metrics

### Update Your App:
```bash
# Make changes to your code
git add .
git commit -m "Update feature"
git push origin main
```
Render will automatically redeploy! 🚀

---

## ⚙️ Render Dashboard Features

### Logs Tab:
- View real-time application logs
- Debug issues
- Monitor requests

### Metrics Tab:
- CPU usage
- Memory usage
- Request count
- Response times

### Settings Tab:
- Environment variables
- Custom domains
- Auto-deploy settings
- Scaling options

### Events Tab:
- Deployment history
- Build logs
- Service events

---

## 🔧 Common Configurations

### Add Environment Variables:

1. Go to your service dashboard
2. Click **"Environment"** in left sidebar
3. Click **"Add Environment Variable"**
4. Add key-value pairs:
   ```
   FLASK_ENV=production
   DEBUG=False
   ```
5. Click **"Save Changes"**
6. Service will redeploy automatically

### Add Custom Domain:

1. Go to **"Settings"** tab
2. Scroll to **"Custom Domains"**
3. Click **"Add Custom Domain"**
4. Enter your domain: `yourdomain.com`
5. Update DNS records as shown
6. Wait for verification (few minutes)
7. Your app at: `https://yourdomain.com`

### Scale Your App:

1. Go to **"Settings"** tab
2. Scroll to **"Instance Type"**
3. Upgrade to paid plan for:
   - More RAM
   - Dedicated CPU
   - No sleep time
   - Better performance

---

## ⚠️ Free Tier Notes

### Limitations:
- ✅ 750 hours/month (enough for 24/7)
- ⚠️ Spins down after 15 min inactivity
- ⚠️ Takes ~30 sec to wake up
- ✅ 512 MB RAM
- ✅ Shared CPU

### Keep App Awake:

Use **UptimeRobot** to ping your app:

1. Go to: https://uptimerobot.com
2. Sign up (free)
3. Add New Monitor:
   - Type: HTTP(s)
   - URL: Your Render URL
   - Interval: 5 minutes
4. Save
5. Your app stays awake! 🎉

---

## 🐛 Troubleshooting

### Build Failed:

**Check logs:**
1. Go to your service dashboard
2. Click **"Logs"** tab
3. Look for error messages

**Common issues:**
- Missing dependencies → Update requirements.txt
- Python version mismatch → Check runtime.txt
- Build timeout → Increase timeout in settings

### App Not Loading:

**Check:**
1. Service status (should be "Live")
2. Logs for errors
3. Build command completed successfully
4. Start command is correct

**Solution:**
- Click **"Manual Deploy"** → "Clear build cache & deploy"

### Model Training Failed:

**Issue:** Training takes too long

**Solution:**
- Already handled! Timeout set to 600 seconds
- If still fails, train model locally and commit the .pkl files

---

## 📞 Get Help

- **Render Docs**: https://render.com/docs
- **Render Community**: https://community.render.com
- **Render Status**: https://status.render.com

---

## ✅ Checklist

Before deploying, make sure:

- [ ] Code pushed to GitHub
- [ ] `requirements.txt` includes gunicorn
- [ ] `app.py` uses PORT environment variable
- [ ] `render.yaml` exists (optional but helpful)
- [ ] Model training works locally

After deploying:

- [ ] Service shows "Live" status
- [ ] URL opens successfully
- [ ] App loads correctly
- [ ] Predictions work
- [ ] Shared URL with others

---

## 🎯 Quick Reference

**Your GitHub Repo:**
```
https://github.com/spchetan/car-ev
```

**Your Render Dashboard:**
```
https://dashboard.render.com
```

**Build Command:**
```
pip install -r requirements.txt && python train_model.py
```

**Start Command:**
```
gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app
```

---

## 🚀 You're All Set!

Your EV Range Prediction app is now:
- ✅ Live on the internet
- ✅ Accessible from anywhere
- ✅ Secured with HTTPS
- ✅ Auto-deploying on git push
- ✅ Free to use!

**Share your app and enjoy! 🎉**
