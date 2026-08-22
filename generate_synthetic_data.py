"""
Generate synthetic EV telemetry data for training
This runs automatically if ev_telemetry_data.csv doesn't exist
"""
import pandas as pd
import numpy as np

def generate_data():
    print("Generating synthetic EV telemetry data...")
    np.random.seed(42)
    n_samples = 5000
    
    # Generate features
    data = {
        'soc': np.random.uniform(0, 100, n_samples),
        'battery_temp': np.random.uniform(-20, 60, n_samples),
        'ambient_temp': np.random.uniform(-20, 40, n_samples),
        'speed': np.random.uniform(0, 120, n_samples),
        'hvac_power': np.random.uniform(0, 5, n_samples),
        'tire_pressure': np.random.uniform(28, 36, n_samples),
        'payload_kg': np.random.uniform(0, 500, n_samples),
        'elevation_change': np.random.uniform(-100, 100, n_samples),
        'drive_mode': np.random.choice(['eco', 'normal', 'sport'], n_samples),
        'weather': np.random.choice(['clear', 'rain', 'snow', 'fog'], n_samples),
        'road_type': np.random.choice(['city', 'highway', 'mixed'], n_samples),
    }
    
    # Calculate realistic range based on factors
    base_range = data['soc'] * 4.5  # Base: 450km at 100% SoC
    
    # Temperature effect
    temp_factor = 1 - np.abs(data['ambient_temp'] - 20) * 0.005
    
    # Speed effect
    speed_factor = 1 - np.abs(data['speed'] - 60) * 0.003
    
    # HVAC effect
    hvac_factor = 1 - data['hvac_power'] * 0.02
    
    # Drive mode effect
    mode_factors = {'eco': 1.15, 'normal': 1.0, 'sport': 0.85}
    mode_effect = np.array([mode_factors[mode] for mode in data['drive_mode']])
    
    # Weather effect
    weather_factors = {'clear': 1.0, 'rain': 0.95, 'snow': 0.85, 'fog': 0.98}
    weather_effect = np.array([weather_factors[w] for w in data['weather']])
    
    # Road type effect
    road_factors = {'city': 0.9, 'highway': 1.1, 'mixed': 1.0}
    road_effect = np.array([road_factors[r] for r in data['road_type']])
    
    # Elevation effect
    elevation_factor = 1 - data['elevation_change'] * 0.002
    
    # Calculate final range
    data['remaining_range_km'] = (base_range * temp_factor * speed_factor * 
                                  hvac_factor * mode_effect * weather_effect * 
                                  road_effect * elevation_factor)
    
    # Add some noise
    data['remaining_range_km'] += np.random.normal(0, 5, n_samples)
    
    # Ensure positive values
    data['remaining_range_km'] = np.maximum(data['remaining_range_km'], 0)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('ev_telemetry_data.csv', index=False)
    print(f"✅ Generated {len(df)} samples → ev_telemetry_data.csv")
    return df

if __name__ == '__main__':
    generate_data()
