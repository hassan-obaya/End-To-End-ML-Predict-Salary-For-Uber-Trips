تمام 👍
أنا هكتب لك **README.md** احترافي يشرح المشروع خطوة بخطوة، مع شرح الفولدرات والملفات وأسلوب التشغيل.

---

## README.md

```markdown
# 🚖 Predict Salary for Uber Trips

This project predicts the **fare amount (salary)** for Uber trips based on trip and environmental features, using **machine learning models**.

---

## 📂 Project Structure
```

PREDICT\_SALARY\_FOR\_UBER\_TRIPS/
│
├── data/                       # Dataset(s)
│   └── Uber\_booking\_status.csv
│
├── models/                     # Saved models (Pickle/Joblib files)
│
├── notebooks/                  # Jupyter notebooks for EDA & experiments
│   ├── uber-trip-eda.ipynb
│   └── predict-salary-for-uber-trip-...
│
├── scripts/                    # Standalone Python scripts
│   └── train.py
│
├── src/                        # Source code modules
│   ├── data\_preprocessing.py
│   ├── evaluation.py
│   ├── feature\_engineering.py
│   ├── model\_training.py
│   └── visualization.py
│
├── static/                     # Static assets (CSS, images, JS)
│
├── templates/                  # HTML templates for Flask app
│   └── index.html
│
├── app.py                      # Flask web application entry point
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

````

---

## 🧠 Machine Learning Pipeline

### 1️⃣ **Data Loading & Exploration**
- Loads `Uber_booking_status.csv` into a pandas DataFrame.
- Displays **info, statistics, null values, duplicates, unique values**.

### 2️⃣ **Data Cleaning**
- Drops irrelevant columns (`User ID`, `User Name`, `Driver Name`, `key`).
- Removes negative fare values.
- Handles missing values by dropping rows with `NaN`.

### 3️⃣ **Feature Engineering**
- Extracts **hour, day, month, weekday, weekend** from pickup datetime.
- Creates **rush hour** feature.
- Encodes categorical features (`Car Condition`, `Weather`, `Traffic Condition`) using `LabelEncoder`.
- Adds trigonometric transformation for `bearing` (`sin`, `cos`).
- Removes unused location columns (latitude/longitude).

### 4️⃣ **Outlier Detection**
- Uses `IsolationForest` to remove anomalies in numerical columns.

### 5️⃣ **Scaling**
- Scales features using `RobustScaler`.

### 6️⃣ **Model Training**
- Trains two models:
  - **RandomForestRegressor**
  - **ExtraTreesRegressor**
- Splits data into **train (80%) / test (20%)**.

### 7️⃣ **Model Evaluation**
- Metrics:
  - **RMSE**
  - **R² Score**
- Compares feature importances for both models.
- Creates **visualizations** for feature importance, actual vs predicted, and residual plots.

### 8️⃣ **Model Saving**
- Saves the trained Random Forest model as:
  ```bash
  random_forest_model.pkl
````

---

## 📊 Visualizations

* **Feature Importance** comparison between Random Forest & Extra Trees.
* **Actual vs Predicted** scatter plot.
* **Residual plot** for model performance.

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/hassan-obaya/End-To-End-ML-Predict-Salary-For-Uber-Trips.git
cd End-To-End-ML-Predict-Salary-For-Uber-Trips
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Training Script

```bash
python scripts/train.py
```

### 5️⃣ Launch the Web App

```bash
python app.py
```

* The app will be available at: `http://127.0.0.1:5000`

---

## 📌 Notes

* Make sure the dataset `Uber_booking_status.csv` exists in the `data/` folder.
* Large model files (`.pkl`) should not be pushed to GitHub — use `.gitignore`.

---

## 👤 Author

**Hassan Obaya**
📧 Contact: *hassanobaya@gmail.com*

```

---

أنا كده كتبت لك **README جاهز للـ GitHub**، بيشرح الفولدرات، البايبلاين، وطريقة التشغيل خطوة خطوة.  
لو تحب أضيف كمان **صورة من النتائج والرسوم البيانية** جوة الـ README علشان تبقى جذابة أكتر على GitHub، أقدر أعملها لك.
```
