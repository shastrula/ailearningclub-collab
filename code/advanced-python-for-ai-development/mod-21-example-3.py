import signal

should_exit = False

def signal_handler(sig, frame):
    global should_exit
    should_exit = True
    # Complete in-flight requests
    pending_requests.join()

signal.signal(signal.SIGTERM, signal_handler)

@app.post('/predict')
async def predict(data):
    if should_exit:
        raise HTTPException(503, 'Server shutting down')
    # Process request
    return await process(data)