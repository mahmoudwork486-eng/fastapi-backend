from fastapi import FastAPI
import pickle

app = FastAPI()

with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/predict")
def predict(data: dict):
    text = data["text"]
    prediction = model.predict([text])[0]
    return {"prediction": str(prediction)}
