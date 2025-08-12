# 🚖 Predict Salary for Uber Trips

This is an **End-to-End Machine Learning Project** that predicts the salary (fare amount) for Uber trips based on various trip details such as location, distance, weather, and traffic conditions.  
The project is deployed locally using **FastAPI**.

---

## 📂 Project Structure
```

├── app.py                  # FastAPI main application
├── model.pkl               # Trained ML model
├── templates/              # HTML templates for UI
├── static/                 # CSS/JS files
├── data/                   # Dataset (ignored in .gitignore)
└── README.md               # Project documentation

````

---

## 📊 Dataset
The raw dataset contains:
- **User & Driver info**
- **Car Condition, Weather, Traffic Condition**
- **Pickup & Dropoff coordinates**
- **Date & Time features**
- **Distances from key NYC landmarks**
- **Trip distance and bearing**

---

## ⚙️ Features
- **Data Preprocessing** (handling missing values, feature engineering)
- **Model Training** using Machine Learning algorithms
- **Local Deployment** with FastAPI
- **Interactive UI** to upload CSV and get predictions

---

## 🚀 How to Run Locally
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/End-To-End-ML-Predict-Salary-For-Uber-Trips.git
   cd End-To-End-ML-Predict-Salary-For-Uber-Trips
    ````

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:

   ```bash
   uvicorn app:app --reload
   ```

4. **Open in browser**:

   ```
   http://127.0.0.1:8000
   ```

---

## 🛠 Technologies Used

* **Python**
* **Pandas, NumPy, Scikit-learn**
* **FastAPI**
* **HTML, CSS (Jinja2 templates)**

---

## 📌 Notes

* The dataset is **not included** in the repo (ignored via `.gitignore`).
* Replace `model.pkl` if retraining the model with new data.

---

## 👨‍💻 Author

**Hassan Obaya**
[GitHub Profile](https://github.com/hassan-obaya)


