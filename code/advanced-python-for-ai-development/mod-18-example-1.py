from prometheus_client import Counter, Histogram, start_http_server

predictions_total = Counter('predictions_total', 'Total predictions')
prediction_duration = Histogram('prediction_duration_seconds', 'Prediction latency')

@prediction_duration.time()
def predict(X):
    predictions_total.inc()
    return model.predict(X)

start_http_server(8000)  # Prometheus scrapes :8000/metrics