def validate_model(model, X_test, y_test):
    # Check inference works
    predictions = model.predict(X_test)
    assert predictions.shape[0] == len(X_test)
    
    # Check metrics
    accuracy = (predictions == y_test).mean()
    assert accuracy > 0.90
    
    # Check edge cases
    assert model.predict(np.zeros((1, 10))).shape == (1,)
    
    return accuracy