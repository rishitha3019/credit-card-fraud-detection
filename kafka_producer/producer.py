import time
import pandas as pd
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

df = pd.read_csv('../data/creditcard_with_location.csv')

for _, row in df.iterrows():
    message = row.to_dict()
    producer.send('credit-transactions', message)
    time.sleep(0.5)

producer.flush()
