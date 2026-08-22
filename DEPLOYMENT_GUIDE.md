# 🌐 Make Your EV Range Prediction App Accessible from Internet

This guide will help you expose your Flask app to the internet in under 5 minutes.

## 🚀 Quick Start with ngrok (Recommended)

### Step 1: Install ngrok

1. **Download ngrok:**
   - Visit: https://ngrok.com/download
   - Click "Download for Windows"
   - Extract the ZIP file to a convenient location (e.g., `C:\ngrok\`)

2. **Add ngrok to your PATH (optional but convenient):**
   - Right-click "This PC" → Properties → Advanced System Settings
   - Click "Environment Variables"
   - Under "System Variables", find "Path" and click "Edit"
   - Click "New" and add the folder where you extracted ngrok.exe
   - Click "OK" on all dialogs

### Step 2: Sign Up for ngrok (Free - Optional but Recommended)

Without signup: 2-hour session limit, random URLs
With free account: Longer sessions, custom subdomains available

1. Create account: https://dashboard.ngrok.com/signup
2. Get your auth token: https://dashboard.ngrok.com/get-started/your-authtoken
3. Run this command once (replace YOUR_TOKEN):
   ```powershell
   ngrok config add-authtoken YOUR_TOKEN
   ```

### Step 3: Start Your Flask App

Open PowerShell in your project directory and run:

```powershell
python app.py
```

You should see:
```
EV Range Prediction API Server
Server starting on http://localhost:5000
```

**Keep this terminal window open!**

### Step 4: Expose Your App with ngrok

Open a **NEW** PowerShell window and run:

```powershell
# If you added ngrok to PATH:
ngrok http 5000

# OR if you didn't add to PATH, navigate to ngrok folder and run:
cd C:\ngrok
.\ngrok.exe http 5000
```

### Step 5: Get Your Public URL

ngrok will display something like:

```
Session Status                online
Account                       your-email@example.com
Version                       3.x.x
Region                        United States (us)
Forwarding                    https://abc123xyz.ngrok-free.app -> http://localhost:5000
```

**Your public URL is:** `https://abc123xyz.ngrok-free.app`

Share this URL with anyone! They can access your app from anywhere in the world.

---

## 🔧 Alternative Methods

### Option 2: Using Cloudflare Tunnel (Free, No Signup Required)

1. Download Cloudflare Tunnel:
   ```powershell
   Invoke-WebRequest -Uri "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe" -OutFile "cloudflared.exe"
   ```

2. Start your Flask app:
   ```powershell
   python app.py
   ```

3. In a new terminal, run:
   ```powershell
   .\cloudflared.exe tunnel --url http://localhost:5000
   ```

4. You'll get a URL like: `https://random-words.trycloudflare.com`

### Option 3: Deploy to Cloud (Permanent Solution)

For a more permanent deployment, consider:

#### **Render.com (Free Tier)**
1. Create account at https://render.com
2. Connect your GitHub repo
3. Create a new "Web Service"
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python app.py`

#### **Railway.app (Free Tier)**
1. Create account at https://railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Select your repository
4. Railway auto-detects Python and deploys

#### **Heroku (Free Tier Available)**
Create a `Procfile`:
```
web: python app.py
```

Deploy:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

---

## 📋 Troubleshooting

### Issue: "Model files not found"
**Solution:** Run these commands first:
```powershell
python train_model.py
```

### Issue: "Port 5000 already in use"
**Solution:** Change the port in app.py (line 80):
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```
Then use `ngrok http 8080`

### Issue: ngrok shows "ERR_NGROK_108"
**Solution:** You need to sign up and add your auth token (see Step 2)

### Issue: "Connection refused" when accessing public URL
**Solution:** Make sure your Flask app is running (check terminal)

### Issue: Firewall blocking ngrok
**Solution:** Allow ngrok through Windows Firewall:
- Windows Security → Firewall & network protection → Allow an app through firewall
- Add ngrok.exe

---

## 🔒 Security Considerations

1. **Don't share sensitive data:** Your app is now public!
2. **Add authentication:** Consider adding login functionality for production
3. **Use HTTPS:** ngrok provides HTTPS automatically
4. **Monitor usage:** Check ngrok dashboard for traffic stats
5. **Rate limiting:** Consider adding rate limiting for production use

---

## 📱 Sharing Your App

Once your app is live, you can:

1. **Share the URL** directly: `https://your-url.ngrok-free.app`
2. **Test on mobile devices:** Just open the URL on your phone
3. **Demo to clients:** Perfect for presentations and demos
4. **Integrate with other services:** Use the API endpoint from anywhere

---

## 🎯 Next Steps

- [ ] Add user authentication
- [ ] Set up a custom domain
- [ ] Deploy to cloud for 24/7 availability
- [ ] Add API rate limiting
- [ ] Set up monitoring and analytics
- [ ] Add CORS for API access from other domains

---

## 📞 Need Help?

- ngrok documentation: https://ngrok.com/docs
- Flask deployment guide: https://flask.palletsprojects.com/en/latest/deploying/
- Cloudflare Tunnel docs: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/

---

**Happy Deploying! 🚀**
