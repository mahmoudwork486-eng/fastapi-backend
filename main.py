from fastapi import FastAPI
import joblib

app = FastAPI()

# تحميل الموديل
model = joblib.load("spam_model.pkl")

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/predict")
def predict(data: dict):
    text = data["text"]
    prediction = model.predict([text])[0]
    return {"result": int(prediction)}
