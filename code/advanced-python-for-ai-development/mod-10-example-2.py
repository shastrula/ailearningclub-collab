from hypothesis import given, strategies as st

@given(
    X=st.arrays(
        dtype=np.float32,
        shape=st.tuples(st.integers(10, 1000), st.just(10))
    )
)
def test_model_invariants(X):
    pred = model.predict(X)
    assert pred.shape[0] == X.shape[0]
    assert np.all(np.isfinite(pred))