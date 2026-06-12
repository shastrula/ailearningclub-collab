from fastapi import HTTPException, status

@app.post('/predict')
def predict(data: InputData):
    try:
        if len(data.features) != 10:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Expected 10 features'
            )
        result = model.predict([data.features])
        return {'prediction': result[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))