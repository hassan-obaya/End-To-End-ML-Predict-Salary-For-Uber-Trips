from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor

def train_models(X_train, y_train):
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    et_model = ExtraTreesRegressor(n_estimators=100, random_state=42)
    et_model.fit(X_train, y_train)

    return rf_model, et_model
