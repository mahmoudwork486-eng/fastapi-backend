from fastapi import FastAPI
import pickle

app = FastAPI()

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/predict")
def predict(data: dict):
    text = data["text"]
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    return {"result": int(prediction)}
