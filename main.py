with open("main.py", "w") as f:
    f.write("""
from fastapi import FastAPI

app = FastAPI()
model = joblib.load("spam_model.pkl")
@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/predict")
def predict(data: dict):
    return {"result": "ok"}
""")
