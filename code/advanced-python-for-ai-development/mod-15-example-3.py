import asyncio

@app.post('/predict_async')
async def predict_async(data: InputData):
    # Offload to thread pool
    result = await asyncio.to_thread(
        model.predict,
        [data.features]
    )
    return {'prediction': result[0]}