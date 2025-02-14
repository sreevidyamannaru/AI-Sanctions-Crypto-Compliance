from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_transaction():
    transactions = [
        {"id": 1, "name": "John Doe", "amount": 1000, "currency": "USD", "country": "Russia"},
        {"id": 2, "name": "Alice Smith", "amount": 500, "currency": "USD", "country": "USA"},
        {"id": 3, "name": "Ivan Petrov", "amount": 2000, "currency": "EUR", "country": "Iran"},
    ]
    return random.choice(transactions)

while True:
    txn = generate_transaction()
    producer.send('transactions', txn)
    print(f"Sent transaction: {txn}")
    time.sleep(2)
