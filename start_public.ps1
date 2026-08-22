# Quick Start Script for Public Access
# This script helps you expose your EV Range Prediction app to the internet

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  EV Range Prediction - Public Access  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if model files exist
if (-not (Test-Path "ev_range_model.pkl")) {
    Write-Host "Model files not found!" -ForegroundColor Yellow
    Write-Host "Running model training first..." -ForegroundColor Yellow
    Write-Host ""
    python train_model.py
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Model training failed. Please check the error above." -ForegroundColor Red
        exit 1
    }
    Write-Host "Model trained successfully!" -ForegroundColor Green
    Write-Host ""
}

# Check if ngrok is available
$ngrokAvailable = $false
try {
    $null = Get-Command ngrok -ErrorAction Stop
    $ngrokAvailable = $true
} catch {
    Write-Host "ngrok not found in PATH" -ForegroundColor Yellow
}

# Check if cloudflared is available
$cloudflaredAvailable = $false
if (Test-Path "cloudflared.exe") {
    $cloudflaredAvailable = $true
}

Write-Host "Available tunneling options:" -ForegroundColor Cyan
Write-Host ""

if ($ngrokAvailable) {
    Write-Host "  ngrok (Recommended)" -ForegroundColor Green
} else {
    Write-Host "  ngrok (Not installed)" -ForegroundColor Red
    Write-Host "     Download from: https://ngrok.com/download" -ForegroundColor Gray
}

if ($cloudflaredAvailable) {
    Write-Host "  Cloudflare Tunnel" -ForegroundColor Green
} else {
    Write-Host "  Cloudflare Tunnel (Not installed)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Prompt user to choose
if ($ngrokAvailable -or $cloudflaredAvailable) {
    Write-Host "Choose your tunneling method:" -ForegroundColor Yellow
    
    if ($ngrokAvailable) {
        Write-Host "  [1] Use ngrok" -ForegroundColor Cyan
    }
    if ($cloudflaredAvailable) {
        Write-Host "  [2] Use Cloudflare Tunnel" -ForegroundColor Cyan
    }
    Write-Host "  [3] Just start Flask (I will setup tunnel manually)" -ForegroundColor Cyan
    Write-Host ""
    
    $choice = Read-Host "Enter your choice (1-3)"
    
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    
    if ($choice -eq "1" -and $ngrokAvailable) {
        Write-Host "Starting Flask app..." -ForegroundColor Green
        Write-Host ""
        
        # Start Flask in background
        $flaskJob = Start-Job -ScriptBlock {
            Set-Location $using:PWD
            python app.py
        }
        
        Start-Sleep -Seconds 3
        
        Write-Host "Starting ngrok tunnel..." -ForegroundColor Green
        Write-Host ""
        Write-Host "Your app will be accessible at the URL shown below:" -ForegroundColor Yellow
        Write-Host "Press Ctrl+C to stop both Flask and ngrok" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host ""
        
        try {
            ngrok http 5000
        } finally {
            Stop-Job -Job $flaskJob
            Remove-Job -Job $flaskJob
        }
        
    } elseif ($choice -eq "2" -and $cloudflaredAvailable) {
        Write-Host "Starting Flask app..." -ForegroundColor Green
        Write-Host ""
        
        # Start Flask in background
        $flaskJob = Start-Job -ScriptBlock {
            Set-Location $using:PWD
            python app.py
        }
        
        Start-Sleep -Seconds 3
        
        Write-Host "Starting Cloudflare tunnel..." -ForegroundColor Green
        Write-Host ""
        Write-Host "Your app will be accessible at the URL shown below:" -ForegroundColor Yellow
        Write-Host "Press Ctrl+C to stop both Flask and Cloudflare tunnel" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host ""
        
        try {
            .\cloudflared.exe tunnel --url http://localhost:5000
        } finally {
            Stop-Job -Job $flaskJob
            Remove-Job -Job $flaskJob
        }
        
    } else {
        Write-Host "Starting Flask app only..." -ForegroundColor Green
        Write-Host ""
        Write-Host "To expose your app, open a NEW terminal and run:" -ForegroundColor Yellow
        Write-Host "  ngrok http 5000" -ForegroundColor Cyan
        Write-Host "OR" -ForegroundColor Yellow
        Write-Host "  .\cloudflared.exe tunnel --url http://localhost:5000" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host ""
        
        python app.py
    }
    
} else {
    Write-Host "No tunneling tools found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install one of the following:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Option 1 - ngrok (Recommended):" -ForegroundColor Cyan
    Write-Host "  1. Download from: https://ngrok.com/download" -ForegroundColor Gray
    Write-Host "  2. Extract to a folder and add to PATH" -ForegroundColor Gray
    Write-Host "  3. Run this script again" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Option 2 - Cloudflare Tunnel:" -ForegroundColor Cyan
    Write-Host "  Download from GitHub releases page" -ForegroundColor Gray
    Write-Host ""
    Write-Host "For now, starting Flask locally..." -ForegroundColor Yellow
    Write-Host "Access at: http://localhost:5000" -ForegroundColor Green
    Write-Host ""
    
    python app.py
}
