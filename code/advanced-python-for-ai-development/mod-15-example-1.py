from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    features: list[float]

@app.post('/predict')
def predict(data: InputData):
    result = model.predict([data.features])
    return {'prediction': result[0]}

# Run: uvicorn app:app --reload