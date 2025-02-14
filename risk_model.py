import openai
import json

openai.api_key = "YOUR_FREE_OPENAI_API_KEY"

def check_sanctions(transaction):
    query = f"Does this transaction violate any sanctions? {json.dumps(transaction)}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return response["choices"][0]["message"]["content"]

txn = {"name": "Ivan Petrov", "amount": 2000, "currency": "EUR", "country": "Iran"}
print(check_sanctions(txn))
