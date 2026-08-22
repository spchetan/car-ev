from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

model = None
feature_metadata = None

def load_model():
    global model, feature_metadata
    try:
        with open('ev_range_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('feature_metadata.pkl', 'rb') as f:
            feature_metadata = pickle.load(f)
        print("Model loaded successfully!")
        return True
    except FileNotFoundError:
        print("Model files not found. Please train the model first by running train_model.py")
        return False

@app.route('/')
def home():
    return render_template('index.html')

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
    if load_model():
        print("\n" + "="*60)
        print("EV Range Prediction API Server")
        print("="*60)
        print("Server starting on http://localhost:5000")
        print("Open your browser and navigate to http://localhost:5000")
        print("="*60 + "\n")
        app.run(debug=True, host='0.0.0.0', port=5001)
    else:
        print("\nPlease run the following commands first:")
        print("1. python generate_dataset.py")
        print("2. python train_model.py")
        print("3. python app.py")
