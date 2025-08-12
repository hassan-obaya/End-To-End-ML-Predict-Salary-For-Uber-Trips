from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd

model = joblib.load(r"C:\Users\hassa\OneDrive\Desktop\Predict salary for uber trips\models\random_forest_model.pkl")

app = FastAPI(title="Uber Trip Fare Prediction")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    distance: float = Form(...),
    jfk_dist: float = Form(...),
    ewr_dist: float = Form(...),
    lga_dist: float = Form(...),
    sol_dist: float = Form(...),
    nyc_dist: float = Form(...),
    Car_Condition: int = Form(...),
    Weather: int = Form(...),
    Traffic_Condition: int = Form(...),
    year: int = Form(...),
    weekday: int = Form(...),
    is_weekend: int = Form(...),
    rush_hour: int = Form(...),
    bearing_sin: float = Form(...),
    bearing_cos: float = Form(...)
):
    df = pd.DataFrame([{
        "distance": distance,
        "jfk_dist": jfk_dist,
        "ewr_dist": ewr_dist,
        "lga_dist": lga_dist,
        "sol_dist": sol_dist,
        "nyc_dist": nyc_dist,
        "Car_Condition": Car_Condition,
        "Weather": Weather,
        "Traffic_Condition": Traffic_Condition,
        "year": year,
        "weekday": weekday,
        "is_weekend": is_weekend,
        "rush_hour": rush_hour,
        "bearing_sin": bearing_sin,
        "bearing_cos": bearing_cos
    }])

    prediction = model.predict(df)[0]
    return templates.TemplateResponse("index.html", {"request": request, "prediction": round(prediction, 2)})
