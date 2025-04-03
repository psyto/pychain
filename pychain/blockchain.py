"""
Main Blockchain class that manages the chain of blocks.
"""
from .models.transaction import Transaction
from .utils.hash_utils import create_genesis_block, proof_of_work
from .utils.validation import is_valid_transaction

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]
        self.previous_block = self.chain[0]

    def add_block(self, transactions):
        """Adds a new block to the chain if all transactions are valid."""
        if all(is_valid_transaction(tx) for tx in transactions):
            new_block = proof_of_work(self.previous_block, transactions)
            self.chain.append(new_block)
            self.previous_block = new_block
            return new_block
        return None

    def get_chain(self):
        """Returns the entire blockchain."""
        return self.chain 