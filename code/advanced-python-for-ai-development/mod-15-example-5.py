@app.post('/predict_batch')
def predict_batch(data: BatchInputData):
    predictions = model.predict(data.batch)
    return {
        'predictions': predictions.tolist(),
        'count': len(predictions)
    }