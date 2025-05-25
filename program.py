import finance_actions

transaction_file_name = 'financial_transactions.csv'

transactions = finance_actions.load_transactions(transaction_file_name)

print(f"Loaded {len(transactions)} transactions from {transaction_file_name}.")

for transaction in transactions[:5]:
    print(transaction)