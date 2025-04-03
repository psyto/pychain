"""
Utility functions for transaction validation.
"""
from ..models.transaction import Transaction

def is_valid_transaction(transaction):
    """Validates a transaction by checking if the amount is positive."""
    return transaction.amount > 0 