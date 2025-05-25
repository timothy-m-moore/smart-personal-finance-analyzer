import unittest
import tempfile
import os
from datetime import datetime
import finance_actions

class TestLoadTransactions(unittest.TestCase):
    
    def test_valid_transactions(self):
        # Create a temporary CSV file with valid data
        csv_content = """transaction_id,customer_id,date,amount,type
                            1,100,2024-01-01,50.00,credit
                            2,101,2024-01-02,20.00,debit"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(csv_content)
            temp_filename = f.name
        
        try:
            transactions = finance_actions.load_transactions(temp_filename)
            
            self.assertEqual(len(transactions), 2)
            self.assertEqual(transactions[0]['transaction_id'], 1)
            self.assertEqual(transactions[0]['amount'], 50.0)
            self.assertEqual(transactions[1]['amount'], -20.0)
            self.assertIsInstance(transactions[0]['date'], datetime)
        finally:
            os.unlink(temp_filename)
    
    def test_file_not_found(self):
        transactions = finance_actions.load_transactions('nonexistent.csv')
        self.assertEqual(transactions, [])
    
    def test_invalid_data(self):
        # CSV with invalid data that should cause ValueError
        csv_content = """transaction_id,customer_id,date,amount,type
invalid_id,100,2024-01-01,50.00,credit"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(csv_content)
            temp_filename = f.name
        
        try:
            transactions = finance_actions.load_transactions(temp_filename)
            self.assertEqual(len(transactions), 0)  # Invalid row should be skipped
        finally:
            os.unlink(temp_filename)

if __name__ == '__main__':
    unittest.main()