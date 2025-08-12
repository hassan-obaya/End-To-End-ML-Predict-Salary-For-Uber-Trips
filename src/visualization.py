import matplotlib.pyplot as plt
import pandas as pd

def plot_feature_importances(features, rf_importances, et_importances):
    importance_df = pd.DataFrame({
        "Feature": features,
        "RF Importance": rf_importances,
        "ET Importance": et_importances
    }).sort_values(by="RF Importance", ascending=False)

    plt.figure(figsize=(10, 5))
    plt.barh(importance_df["Feature"], importance_df["RF Importance"], color='blue', alpha=0.7, label="Random Forest")
    plt.barh(importance_df["Feature"], importance_df["ET Importance"], color='red', alpha=0.5, label="Extra Trees")
    plt.xlabel("Feature Importance")
    plt.ylabel("Features")
    plt.title("Feature Importance Comparison")
    plt.legend()
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def plot_predictions(y_test, preds, model_name):
    plt.figure(figsize=(12, 4))
    # Actual vs Predicted
    plt.subplot(1, 2, 1)
    plt.scatter(y_test, preds, color='blue', alpha=0.5, label='Predicted', marker='o')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title(f"{model_name}: Actual vs Predicted")
    plt.legend()

    # Residual Plot
    plt.subplot(1, 2, 2)
    residuals = y_test - preds
    plt.scatter(preds, residuals, alpha=0.5)
    plt.axhline(0, color='r', linestyle='--')
    plt.xlabel("Predicted")
    plt.ylabel("Residuals")
    plt.title(f"{model_name}: Residual Plot")

    plt.tight_layout()
    plt.show()
