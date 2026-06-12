from functools import lru_cache

@lru_cache(maxsize=1)
def get_model():
    return load_model('model.pkl')

@app.on_event('startup')
async def startup():
    get_model()  # Preload model

@app.post('/predict')
def predict(data: InputData):
    model = get_model()
    return {'prediction': model.predict([data.features])[0]}