import cloudpickle
import joblib

# Joblib better for ML models
joblib.dump(model, 'model.pkl', compress=3)
model = joblib.load('model.pkl')

# Cloudpickle for complex objects
import cloudpickle
serialized = cloudpickle.dumps(model)