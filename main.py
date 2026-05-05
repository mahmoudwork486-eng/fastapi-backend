with open("main.py", "w") as f:
    f.write("""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/predict")
def predict(data: dict):
    return {"result": "ok"}
""")
