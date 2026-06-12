import ray

ray.init()

@ray.remote
def train_model(config):
    model = Model(**config)
    model.train(X, y)
    return model.evaluate(X_test)

futures = [
    train_model.remote(config) for config in configs
]
results = ray.get(futures)