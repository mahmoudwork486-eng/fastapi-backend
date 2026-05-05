from fastapi import FastAPI
import pickle

app = FastAPI()

# تحميل الموديل مرة واحدة
model = pickle.load(open("spam_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/predict")
def predict(data: dict):
    text = data["text"]
    prediction = model.predict([text])[0]
    return {"result": int(prediction)}
