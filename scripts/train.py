
import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.resolve()
sys.path.append(str(project_root))

import joblib
from sklearn.model_selection import train_test_split
from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import encode_categoricals, remove_anomalies, scale_features
from src.model_training import train_models
from src.evaluation import evaluate_model
from src.visualization import plot_feature_importances, plot_predictions




# Load and clean
df = load_data(r"C:\Users\hassa\OneDrive\Desktop\Predict salary for uber trips\data\Uber_booking_status.csv")
df = clean_data(df)

# Feature engineering
cat_columns = ['Car Condition', 'Weather', 'Traffic Condition']
numeric_columns = ['fare_amount', 'distance','jfk_dist','ewr_dist','lga_dist','sol_dist','nyc_dist']
df = encode_categoricals(df, cat_columns)
df = remove_anomalies(df, numeric_columns)
df['year'] = df['year'] - df['year'].min()

# Prepare features
X = df.drop(columns=["fare_amount"])
y = df["fare_amount"]
X = scale_features(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
rf_model, et_model = train_models(X_train, y_train)

# Evaluate
evaluate_model(y_test, rf_model.predict(X_test), "Random Forest Regressor")
evaluate_model(y_test, et_model.predict(X_test), "Extra Trees Regressor")

# Feature importance plot
plot_feature_importances(X.columns, rf_model.feature_importances_, et_model.feature_importances_)

# Prediction plots
plot_predictions(y_test, rf_model.predict(X_test), "Random Forest")

# Save model
joblib.dump(rf_model,r"C:\Users\hassa\OneDrive\Desktop\Predict salary for uber trips\models\random_forest_model.pkl")
