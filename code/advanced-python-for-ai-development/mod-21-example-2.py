@app.get('/health')
async def health():
    try:
        model.predict([[0]*10])
        return {'status': 'healthy'}
    except Exception as e:
        return {'status': 'unhealthy', 'error': str(e)}