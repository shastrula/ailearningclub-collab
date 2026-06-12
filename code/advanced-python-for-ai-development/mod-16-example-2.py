from sqlalchemy.orm import Session

predictions = [
    Prediction(model_id=f'v1', result=f'{p}')
    for p in model.predict(X)
]

with Session(engine) as session:
    session.bulk_insert_mappings(
        Prediction,
        [p.__dict__ for p in predictions]
    )
    session.commit()