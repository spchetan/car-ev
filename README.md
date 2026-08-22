# Electric Vehicle Range Prediction System

A data-driven machine learning application for predicting electric vehicle range based on real-time vehicle parameters and environmental conditions.

## Features

- **ML-Powered Predictions**: Gradient Boosting Regressor trained on 5000+ synthetic data points
- **Modern Web UI**: Beautiful, responsive interface built with TailwindCSS
- **Real-time Predictions**: Instant range estimation based on 11 input parameters
- **Comprehensive Parameters**: Battery state, temperature, speed, HVAC, payload, terrain, and more

## Project Structure

```
windsurf-carev/
├── generate_dataset.py      # Generates synthetic EV telemetry data
├── train_model.py           # Trains ML model and saves artifacts
├── app.py                   # Flask API server
├── templates/
│   └── index.html          # Web UI
├── requirements.txt         # Python dependencies
├── ev_telemetry_data.csv   # Generated dataset (after running step 1)
├── ev_range_model.pkl      # Trained model (after running step 2)
└── feature_metadata.pkl    # Feature configuration (after running step 2)
```

## Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate Training Dataset

```bash
python generate_dataset.py
```

This creates `ev_telemetry_data.csv` with 5000 samples including:
- State of Charge (SoC)
- Battery & ambient temperature
- Speed, HVAC power, tire pressure
- Payload, elevation changes
- Drive mode, weather, road type

### 3. Train the Model

```bash
python train_model.py
```

This will:
- Train a Gradient Boosting model
- Display performance metrics (MAE, RMSE, R²)
- Save model to `ev_range_model.pkl`
- Generate prediction visualization

Expected performance:
- Test MAE: ~3-5 km
- Test R²: >0.95

### 4. Run the Web Application

```bash
python app.py
```

Open your browser and navigate to: **http://localhost:5000**

## Usage

### Web Interface

1. **Adjust Parameters** in the left panel:
   - **Battery**: State of Charge (0-100%)
   - **Temperatures**: Battery and ambient (-20°C to 60°C)
   - **Driving**: Speed, drive mode, road type
   - **Environment**: Weather, elevation change
   - **Vehicle**: HVAC power, tire pressure, payload

2. **Click "Calculate Range"** to get instant predictions

3. **View Results** in the right panel:
   - Estimated range in km and miles
   - Summary of key parameters

### API Endpoint

**POST** `/predict`

```json
{
  "soc": 80,
  "battery_temp": 25,
  "ambient_temp": 20,
  "speed": 60,
  "hvac_power": 2,
  "tire_pressure": 32,
  "payload_kg": 100,
  "elevation_change": 0,
  "drive_mode": "normal",
  "weather": "clear",
  "road_type": "mixed"
}
```

**Response:**

```json
{
  "predicted_range_km": 342.5,
  "predicted_range_miles": 212.8,
  "input_parameters": {...}
}
```

## Model Details

- **Algorithm**: Gradient Boosting Regressor (scikit-learn)
- **Features**: 8 numerical + 3 categorical (one-hot encoded)
- **Preprocessing**: StandardScaler for numerical features
- **Hyperparameters**:
  - n_estimators: 200
  - learning_rate: 0.1
  - max_depth: 5
  - subsample: 0.8

## Key Factors Affecting Range

1. **State of Charge**: Primary determinant (linear relationship)
2. **Temperature**: Extreme cold/heat reduces efficiency
3. **Speed**: Higher speeds increase energy consumption
4. **Drive Mode**: Eco (+15%), Normal (baseline), Sport (-15%)
5. **HVAC Usage**: Significant impact on range
6. **Terrain**: Uphill reduces range, downhill improves it
7. **Weather**: Snow/rain reduce efficiency
8. **Road Type**: Highway vs city driving patterns

## Future Enhancements

- [ ] Real vehicle data integration
- [ ] Time-series LSTM for sequential predictions
- [ ] Feature importance visualization
- [ ] Historical trip analysis
- [ ] Mobile-responsive design improvements
- [ ] Export prediction reports
- [ ] Multi-vehicle support

## Technologies Used

- **Backend**: Flask, Python 3.x
- **ML**: scikit-learn, pandas, numpy
- **Frontend**: HTML5, TailwindCSS, JavaScript
- **Visualization**: matplotlib

## License

MIT License - Feel free to use and modify for your projects.

## Author

Built with ❤️ for sustainable transportation
