import pandas as pd
import numpy as np

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    df.drop(columns=["User ID", "User Name", "Driver Name", "key"], inplace=True)
    df = df[df['fare_amount'] >= 0].dropna()
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['hour'] = df['pickup_datetime'].dt.hour
    df['day'] = df['pickup_datetime'].dt.day
    df['month'] = df['pickup_datetime'].dt.month
    df['weekday'] = df['pickup_datetime'].dt.weekday
    df['is_weekend'] = (df['weekday'] >= 5).astype(int)
    df['rush_hour'] = df['hour'].apply(lambda x: 1 if (7 <= x <= 9) or (17 <= x <= 19) else 0)
    df["bearing_sin"] = np.sin(df["bearing"])
    df["bearing_cos"] = np.cos(df["bearing"])
    df.drop(columns=["bearing", 'pickup_datetime', 'pickup_longitude',
                     'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude'], inplace=True)
    return df
