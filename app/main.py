from fastapi import FastAPI
from app.model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD is working 🚀"}

@app.post("/predict")
def get_prediction(text: str):
    result = predict(text)
    return {"prediction": result}
