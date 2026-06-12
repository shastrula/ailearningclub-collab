import mlflow

mlflow.set_experiment('model_training')

with mlflow.start_run():
    mlflow.log_param('learning_rate', 0.001)
    mlflow.log_param('batch_size', 32)
    
    model.fit(X, y)
    
    mlflow.log_metric('accuracy', 0.95)
    mlflow.log_metric('f1_score', 0.92)
    mlflow.sklearn.log_model(model, 'model')