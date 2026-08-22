import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

print("Loading dataset...")
df = pd.read_csv('ev_telemetry_data.csv')

target = 'remaining_range_km'
num_cols = ['soc', 'battery_temp', 'ambient_temp', 'speed', 'hvac_power', 
            'tire_pressure', 'payload_kg', 'elevation_change']
cat_cols = ['drive_mode', 'weather', 'road_type']

X = df[num_cols + cat_cols]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
    ]
)

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(
        n_estimators=200,
        learning_rate=0.1,
        max_depth=5,
        min_samples_split=5,
        min_samples_leaf=2,
        subsample=0.8,
        random_state=42
    ))
])

print("\nTraining model...")
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

train_mae = mean_absolute_error(y_train, y_pred_train)
train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
train_r2 = r2_score(y_train, y_pred_train)

test_mae = mean_absolute_error(y_test, y_pred_test)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
test_r2 = r2_score(y_test, y_pred_test)

print("\n" + "="*50)
print("MODEL PERFORMANCE")
print("="*50)
print(f"\nTraining Set:")
print(f"  MAE:  {train_mae:.2f} km")
print(f"  RMSE: {train_rmse:.2f} km")
print(f"  R²:   {train_r2:.4f}")

print(f"\nTest Set:")
print(f"  MAE:  {test_mae:.2f} km")
print(f"  RMSE: {test_rmse:.2f} km")
print(f"  R²:   {test_r2:.4f}")
print("="*50)

with open('ev_range_model.pkl', 'wb') as f:
    pickle.dump(model, f)

feature_metadata = {
    'num_cols': num_cols,
    'cat_cols': cat_cols,
    'feature_order': num_cols + cat_cols
}

with open('feature_metadata.pkl', 'wb') as f:
    pickle.dump(feature_metadata, f)

print("\nModel saved to 'ev_range_model.pkl'")
print("Feature metadata saved to 'feature_metadata.pkl'")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_test, alpha=0.5, s=20)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Range (km)', fontsize=12)
plt.ylabel('Predicted Range (km)', fontsize=12)
plt.title('EV Range Prediction: Actual vs Predicted', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('prediction_plot.png', dpi=100)
print("Prediction plot saved to 'prediction_plot.png'")
