from sklearn.preprocessing import LabelEncoder, RobustScaler
from sklearn.ensemble import IsolationForest
import pandas as pd

def encode_categoricals(df, columns):
    le = LabelEncoder()
    for col in columns:
        df[col] = le.fit_transform(df[col])
    return df

def remove_anomalies(df, numeric_columns):
    model = IsolationForest(contamination=0.10, random_state=42)
    df["anomaly"] = model.fit_predict(df[numeric_columns])
    df = df[df["anomaly"] != -1].drop(columns=["anomaly"])
    return df

def scale_features(X):
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)
    return pd.DataFrame(X_scaled, columns=X.columns)
