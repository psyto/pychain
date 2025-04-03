"""
Main entry point for running the blockchain.
"""
from .models.transaction import Transaction
from .blockchain import Blockchain

def main():
    # Initialize blockchain
    blockchain = Blockchain()

    # Sample transactions
    transactions = [
        Transaction("Alice", "Bob", 50),
        Transaction("Bob", "Charlie", 25)
    ]

    # Add 10 blocks to the chain
    for i in range(10):
        new_block = blockchain.add_block(transactions)
        if new_block:
            print(f"Block #{new_block.index} added to the blockchain!")
            print(f"Hash: {new_block.hash}")
        else:
            print("Invalid transaction detected. Skipping block creation.")

if __name__ == "__main__":
    main() 