"""
Utility functions for hash calculations and proof of work.
"""
import hashlib
import time
from ..models.block import Block
from ..models.transaction import Transaction

def calculate_hash(block):
    """Calculates the SHA-256 hash of a block."""
    value = (str(block.index) + str(block.previous_hash) + str(block.timestamp) 
             + str(block.transactions) + str(block.nonce))
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    """Creates the first block in the blockchain (genesis block)."""
    transactions = [Transaction("Genesis", "Genesis", 0)]
    return Block(0, "0", int(time.time()), transactions, 
                calculate_hash(Block(0, "0", int(time.time()), transactions, 0, 0)), 0)

def proof_of_work(previous_block, transactions):
    """Implements the proof of work algorithm.
    Finds a nonce that produces a hash with 4 leading zeros."""
    nonce = 0
    while True:
        new_block = Block(previous_block.index + 1, 
                         previous_block.hash,
                         int(time.time()), 
                         transactions, 
                         calculate_hash(Block(previous_block.index + 1, 
                                            previous_block.hash, 
                                            int(time.time()), 
                                            transactions, 
                                            previous_block.hash, 
                                            nonce)), nonce)
        if new_block.hash.startswith('0' * 4):
            return new_block
        nonce += 1 