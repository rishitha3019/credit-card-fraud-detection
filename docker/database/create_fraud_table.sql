CREATE TABLE fraud_predictions (
    id SERIAL PRIMARY KEY,
    transaction_time TIMESTAMP,
    amount FLOAT,
    latitude FLOAT,
    longitude FLOAT,
    prediction INT
);
