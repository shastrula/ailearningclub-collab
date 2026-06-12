with Session(engine) as session:
    try:
        session.add(prediction1)
        session.add(prediction2)
        session.commit()
    except Exception:
        session.rollback()
        raise