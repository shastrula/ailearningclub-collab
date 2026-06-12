# Route 10% to new model
if random.random() < 0.1:
    model = new_model
else:
    model = current_model

predictions = model.predict(X)

# Monitor new_model metrics
if new_model_metrics > current_metrics:
    # Switch fully
    current_model = new_model