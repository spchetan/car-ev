"""
EV Range Prediction App with Embedded Model Training
All-in-one solution - no external dependencies
"""
from flask import Flask, request, jsonify, send_file
import pickle
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor

app = Flask(__name__)

model = None
feature_metadata = None

def generate_training_data():
    """Generate synthetic EV telemetry data"""
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
    temp_adj = 1 - np.abs(data['ambient_temp'] - 20) * 0.005
    speed_adj = 1 - np.abs(data['speed'] - 60) * 0.003
    hvac_adj = 1 - data['hvac_power'] * 0.02
    
    mode_map = {'eco': 1.15, 'normal': 1.0, 'sport': 0.85}
    mode_adj = np.array([mode_map[m] for m in data['drive_mode']])
    
    weather_map = {'clear': 1.0, 'rain': 0.95, 'snow': 0.85, 'fog': 0.98}
    weather_adj = np.array([weather_map[w] for w in data['weather']])
    
    road_map = {'city': 0.9, 'highway': 1.1, 'mixed': 1.0}
    road_adj = np.array([road_map[r] for r in data['road_type']])
    
    elev_adj = 1 - data['elevation_change'] * 0.002
    
    data['remaining_range_km'] = (base * temp_adj * speed_adj * hvac_adj * 
                                  mode_adj * weather_adj * road_adj * elev_adj)
    data['remaining_range_km'] += np.random.normal(0, 5, n)
    data['remaining_range_km'] = np.maximum(data['remaining_range_km'], 0)
    
    df = pd.DataFrame(data)
    print(f"✅ Generated {len(df)} training samples")
    return df

def train_and_load_model():
    """Train model and load it into memory"""
    global model, feature_metadata
    
    print("="*60)
    print("TRAINING MODEL")
    print("="*60)
    
    try:
        # Generate training data
        df = generate_training_data()
        
        # Define features
        num_cols = ['soc', 'battery_temp', 'ambient_temp', 'speed', 'hvac_power', 
                    'tire_pressure', 'payload_kg', 'elevation_change']
        cat_cols = ['drive_mode', 'weather', 'road_type']
        
        X = df[num_cols + cat_cols]
        y = df['remaining_range_km']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
        
        # Create preprocessing pipeline
        preprocessor = ColumnTransformer([
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
        ])
        
        # Create and train model
        print("Training Gradient Boosting model...")
        model = Pipeline([
            ('preprocessor', preprocessor),
            ('regressor', GradientBoostingRegressor(
                n_estimators=100,
                learning_rate=0.1,
                max_depth=5,
                random_state=42
            ))
        ])
        
        model.fit(X_train, y_train)
        
        # Evaluate
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)
        
        print(f"✅ Model trained successfully!")
        print(f"   Train R²: {train_score:.4f}")
        print(f"   Test R²:  {test_score:.4f}")
        
        # Save metadata
        feature_metadata = {
            'num_cols': num_cols,
            'cat_cols': cat_cols,
            'feature_order': num_cols + cat_cols
        }
        
        print("="*60)
        print("MODEL READY")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"❌ Error training model: {e}")
        import traceback
        traceback.print_exc()
        return False

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Please wait for model training to complete.'}), 500
    
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
    # Train model on startup
    print("\n" + "="*60)
    print("EV RANGE PREDICTION API SERVER")
    print("="*60)
    
    if train_and_load_model():
        print("✅ Model loaded and ready!")
    else:
        print("⚠️  Model training failed, but server will start anyway")
    
    port = int(os.environ.get('PORT', 5000))
    print(f"\n🚀 Starting server on port {port}")
    print(f"   Model status: {'LOADED ✅' if model is not None else 'NOT LOADED ❌'}")
    print("="*60 + "\n")
    
    app.run(debug=False, host='0.0.0.0', port=port)
