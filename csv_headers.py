class TransactionHeaders:
    """Define expected CSV headers for transaction files."""
    
    TRANSACTION_ID = "transaction_id"
    DATE = "date"
    CUSTOMER_ID = "customer_id"
    AMOUNT = "amount"
    TYPE = "type"
    DESCRIPTION = "description"
    
    @classmethod
    def get_all_headers(cls):
        """Return a list of all expected headers in order."""
        return [
            cls.TRANSACTION_ID,
            cls.DATE,
            cls.CUSTOMER_ID,
            cls.AMOUNT,
            cls.TYPE,
            cls.DESCRIPTION
        ]
    
    @classmethod
    def validate_headers(cls, headers):
        """Check if all required headers are present."""
        required = {cls.TRANSACTION_ID, cls.CUSTOMER_ID, cls.DATE, cls.AMOUNT, cls.TYPE, cls.DESCRIPTION}
        present = set(headers)
        missing = required - present
        return len(missing) == 0, missing