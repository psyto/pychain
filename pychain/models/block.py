"""
Block class represents a single block in the blockchain.
Each block contains:
- index: position in the chain
- previous_hash: hash of the previous block
- timestamp: when the block was created
- transactions: list of transactions
- hash: current block's hash
- nonce: number used in proof of work
"""

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash
        self.nonce = nonce 