import faker

import random

from datetime import datetime, timedelta


fake = faker.Faker()



transactions = []

for i in range(10):

    transaction = {

        "transaction_id": f"TX{i + 1}",

        "transaction_date": (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'),

        "amount": round(random.uniform(10.0, 1000.0), 2)

    }

    transactions.append(transaction)


for transaction in transactions:

    print(f"Transaction ID: {transaction['transaction_id']}, Date: {transaction['transaction_date']}, Amount: ${transaction['amount']:.2f}")