# Personal Finance Analyzer

A Python-based command-line application for managing and analyzing personal financial transactions. Load transaction data from CSV files, add new transactions, update existing ones, and generate detailed financial reports.

## Features

- **Load Transactions**: Import financial data from CSV files
- **Add Transactions**: Create new financial transactions with validation
- **View Transactions**: Display and filter transactions by type
- **Update Transactions**: Modify existing transaction details
- **Delete Transactions**: Remove unwanted transactions
- **Financial Analysis**: Generate comprehensive financial summaries for 2022 transactions
- **Generate Reports**: Create dated financial reports
- **Save Transactions**: Export data back to CSV format

## CSV File Setup

### Required File Location
Place your `financial_transactions.csv` file in the **root directory** of the project (same folder as `program.py`).

### CSV Format
The CSV file should contain the following columns in this order:

```csv
transaction_id,date,customer_id,amount,type,description
1,2022-01-15,100,1500.00,credit,Salary payment
2,2022-01-16,101,75.50,debit,Grocery shopping
3,2022-01-17,102,250.00,transfer,Account transfer
```

### Important Notes
- The CSV file **must** be named `financial_transactions.csv`, unless you provide another file name when asked
- Headers are optional - the program can handle files with or without header rows
- Amounts should be positive numbers - the program handles debit/credit signs internally
- Dates must be in YYYY-MM-DD format

## Usage

### Starting the Program
```bash
python program.py
```

### Menu Options
The program presents a menu with 9 options:

1. **Load transactions from file** - Import data from `financial_transactions.csv`
2. **Add a new transaction** - Create new transactions with guided input
3. **View transactions** - Display transactions with optional filtering
4. **Update a transaction** - Modify existing transaction properties
5. **Delete a transaction** - Remove transactions from the dataset
6. **Analyze finances** - Generate comprehensive 2022 financial analysis
7. **Save transactions to file** - Export current data to CSV
8. **Generate a report** - Create dated financial summary reports
9. **Exit the program** - Close the application

## Generated Files

The program creates several output files:

- **`analysis.txt`**: Detailed financial analysis including percentages and customer insights
- **`report_YYYYMMDD.txt`**: Daily financial summary reports (dated)
- **`errors.txt`**: Error log for troubleshooting
- **`financial_transactions.csv`**: Updated transaction data when saved

## Financial Analysis Features

The analysis function provides:
- Total credits, debits, and transfers for 2022
- Net balance calculation
- Percentage breakdown by transaction type
- Customer with highest debit amount
- Transaction count and averages
- Automatic save to `analysis.txt`

## Error Handling

- Invalid CSV formats are automatically detected and handled
- Missing headers are replaced with default values
- Date and amount validation with user-friendly error messages
- File permission and access errors are logged to `errors.txt`

## Data Consistency

- Debit transactions are stored as negative amounts internally
- Credit and transfer transactions are stored as positive amounts
- CSV exports always use positive amounts (type field indicates debit/credit)
- All monetary values are formatted to 2 decimal places

## Troubleshooting

### "File not found" Error
- Ensure `financial_transactions.csv` is in the same directory as `program.py`
- Check that the filename is exactly `financial_transactions.csv` (case-sensitive)

### Invalid Data Errors
- Check that dates are in YYYY-MM-DD format
- Verify that amounts are valid numbers
- Ensure transaction types are `credit`, `debit`, or `transfer`