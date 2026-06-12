from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'model_input',
    bootstrap_servers=['localhost:9092']
)

for message in consumer:
    data = json.loads(message.value)
    prediction = model.predict(data['features'])
    producer.send('model_output', prediction)