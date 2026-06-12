from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Prediction(Base):
    __tablename__ = 'predictions'
    id = Column(Integer, primary_key=True)
    model_id = Column(String)
    result = Column(String)

engine = create_engine('sqlite:///predictions.db')
Base.metadata.create_all(engine)

# Insert
with Session(engine) as session:
    pred = Prediction(model_id='v1', result='0.95')
    session.add(pred)
    session.commit()