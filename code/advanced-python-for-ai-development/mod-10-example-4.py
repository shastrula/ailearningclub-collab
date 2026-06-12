import pytest

@pytest.fixture
def trained_model():
    model = Model()
    X, y = generate_test_data()
    model.fit(X, y)
    yield model
    # Cleanup
    model.cleanup()

def test_prediction(trained_model):
    pred = trained_model.predict(X_test)
    assert len(pred) == len(X_test)