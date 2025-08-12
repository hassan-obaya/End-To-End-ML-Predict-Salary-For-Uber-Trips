# End-to-End ML Project: Predicting Salary for Uber Trips

This project is an **end-to-end Machine Learning application** built using **FastAPI** that predicts the salary (fare amount) for Uber trips based on trip details such as car condition, weather, traffic, distance, and more.

---

## 🚀 Features
- **Data Preprocessing**: Cleans and prepares raw Uber trip data for model training.
- **Machine Learning Model**: Uses a trained regression model to predict fare amounts.
- **FastAPI Web Interface**: User-friendly web page for uploading trip data (CSV) and getting predictions.
- **CSV Output**: Returns predictions as a downloadable CSV file.
- **Responsive UI**: Simple and professional design for easy interaction.

---

## 📂 Project Structure
.
├── app.py # Main FastAPI application
├── templates/
│ └── index.html # Web interface
├── static/ # CSS, JS, images (if any)
├── model.pkl # Trained ML model
├── requirements.txt # Project dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/hassan-obaya/End-To-End-ML-Predict-Salary-For-Uber-Trips.git
cd End-To-End-ML-Predict-Salary-For-Uber-Trips
Create a virtual environment

bash
Copy
Edit
python -m venv venv
Activate the virtual environment

Windows:

bash
Copy
Edit
venv\Scripts\activate
macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
▶️ Running the App
bash
Copy
Edit
uvicorn app:app --reload
Visit http://127.0.0.1:8000 in your browser.

📊 Example
Upload a CSV file containing Uber trip data, and the application will return a downloadable CSV file with predicted fare amounts.

🛠️ Technologies Used
Python 3.9+

FastAPI

Scikit-learn

Pandas

HTML/CSS (Jinja2 templates)

Uvicorn
