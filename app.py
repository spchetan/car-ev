from flask import Flask, request, jsonify, send_file
import pickle
import pandas as pd
import numpy as np
import os
import subprocess

app = Flask(__name__)

model = None
feature_metadata = None

def train_model_if_needed():
    """Train model if .pkl files don't exist"""
    if not os.path.exists('ev_range_model.pkl') or not os.path.exists('feature_metadata.pkl'):
        print("Model files not found. Training model now...")
        try:
            # Run train_model.py
            result = subprocess.run(['python', 'train_model.py'], 
                                  capture_output=True, 
                                  text=True, 
                                  timeout=300)
            print(result.stdout)
            if result.returncode != 0:
                print(f"Training failed: {result.stderr}")
                return False
            print("Model training completed!")
            return True
        except Exception as e:
            print(f"Error training model: {e}")
            return False
    return True

def load_model():
    global model, feature_metadata
    
    # Train model if needed
    if not train_model_if_needed():
        print("Failed to train model")
        return False
    
    try:
        with open('ev_range_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('feature_metadata.pkl', 'rb') as f:
            feature_metadata = pickle.load(f)
        print("Model loaded successfully!")
        return True
    except Exception as e:
        print(f"Error loading model: {e}")
        return False

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Please train the model first.'}), 500
    
    try:
        data = request.json
        
        input_data = {
            'soc': float(data.get('soc', 80)),
            'battery_temp': float(data.get('battery_temp', 25)),
            'ambient_temp': float(data.get('ambient_temp', 20)),
            'speed': float(data.get('speed', 60)),
            'hvac_power': float(data.get('hvac_power', 2)),
            'tire_pressure': float(data.get('tire_pressure', 32)),
            'payload_kg': float(data.get('payload_kg', 100)),
            'elevation_change': float(data.get('elevation_change', 0)),
            'drive_mode': data.get('drive_mode', 'normal'),
            'weather': data.get('weather', 'clear'),
            'road_type': data.get('road_type', 'mixed')
        }
        
        df_input = pd.DataFrame([input_data])
        
        prediction = model.predict(df_input)[0]
        prediction = max(0, prediction)
        
        return jsonify({
            'predicted_range_km': round(prediction, 2),
            'predicted_range_miles': round(prediction * 0.621371, 2),
            'input_parameters': input_data
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

if __name__ == '__main__':
    # Always try to load/train model
    load_model()
    
    # Start server even if model loading failed
    # (model will be None and predictions will return error)
    port = int(os.environ.get('PORT', 5000))
    print("\n" + "="*60)
    print("EV Range Prediction API Server")
    print("="*60)
    print(f"Model loaded: {model is not None}")
    print(f"Server starting on port {port}")
    print("="*60 + "\n")
    app.run(debug=False, host='0.0.0.0', port=port)
