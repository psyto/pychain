import hashlib
import time

# Block class represents a single block in the blockchain
# Each block contains:
# - index: position in the chain
# - previous_hash: hash of the previous block
# - timestamp: when the block was created
# - transactions: list of transactions in this block
# - hash: current block's hash
# - nonce: number used in proof of work
class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash
        self.nonce = nonce

# Transaction class represents a single transaction
# Contains:
# - sender: who is sending the coins
# - receiver: who is receiving the coins
# - amount: how many coins are being transferred
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        
# Calculates the SHA-256 hash of a block
# Combines all block data into a single string and hashes it
def calculate_hash(block):
    value = (str(block.index) + str(block.previous_hash) + str(block.timestamp) 
             + str(block.transactions) + str(block.nonce))
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

# Creates the first block in the blockchain (genesis block)
# This block has no previous block and contains a special genesis transaction
def create_genesis_block():
    transactions = [Transaction("Genesis", "Genesis", 0)]
    return Block(0, "0", int(time.time()), transactions, calculate_hash(Block(0, "0", int(time.time()), transactions, 0, 0)), 0)

# Implements the proof of work algorithm
# Finds a nonce that produces a hash with 4 leading zeros
# Returns the new block when a valid nonce is found
def proof_of_work(previous_block, transactions):
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

# Validates a transaction by checking if the amount is positive
def is_valid_transaction(transaction):
    return transaction.amount > 0

# Initialize the blockchain with the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Sample transactions to be added to the blockchain
transactions = [Transaction("Alice", "Bob", 50), Transaction("Bob", "Charlie", 25)]

# Add 10 new blocks to the blockchain
for i in range(10):
    if all(is_valid_transaction(tx) for tx in transactions):
        new_block = proof_of_work(previous_block, transactions)
        blockchain.append(new_block)
        previous_block = new_block
        print(f"Block #{new_block.index} added to the blockchain!")
        print(f"Hash: {new_block.hash}")
    else:
        print("Invalid transaction detected. Skipping block creation.")
        