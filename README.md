# Python Blockchain Implementation

A simple blockchain implementation in Python that demonstrates the core concepts of blockchain technology including proof of work, transaction validation, and block creation.

## Features

-   Block creation with proof of work
-   Transaction validation
-   SHA-256 hashing
-   Genesis block creation
-   Blockchain structure with linked blocks

## Project Structure

The project consists of a single Python file `pychain.py` that contains:

### Classes

1. `Block`

    - Represents a single block in the blockchain
    - Contains:
        - index: position in the chain
        - previous_hash: hash of the previous block
        - timestamp: when the block was created
        - transactions: list of transactions
        - hash: current block's hash
        - nonce: number used in proof of work

2. `Transaction`
    - Represents a single transaction
    - Contains:
        - sender: who is sending the coins
        - receiver: who is receiving the coins
        - amount: how many coins are being transferred

### Functions

1. `calculate_hash(block)`

    - Calculates the SHA-256 hash of a block
    - Combines all block data into a single string and hashes it

2. `create_genesis_block()`

    - Creates the first block in the blockchain
    - Contains a special genesis transaction

3. `proof_of_work(previous_block, transactions)`

    - Implements the proof of work algorithm
    - Finds a nonce that produces a hash with 4 leading zeros
    - Returns the new block when a valid nonce is found

4. `is_valid_transaction(transaction)`
    - Validates a transaction by checking if the amount is positive

## Usage

The blockchain is initialized with a genesis block and then adds 10 new blocks with sample transactions:

```python
# Initialize blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Sample transactions
transactions = [
    Transaction("Alice", "Bob", 50),
    Transaction("Bob", "Charlie", 25)
]

# Add blocks to the chain
for i in range(10):
    if all(is_valid_transaction(tx) for tx in transactions):
        new_block = proof_of_work(previous_block, transactions)
        blockchain.append(new_block)
        previous_block = new_block
        print(f"Block #{new_block.index} added to the blockchain!")
        print(f"Hash: {new_block.hash}")
```

## Requirements

-   Python 3.x
-   Standard library modules:
    -   hashlib
    -   time

## Running the Code

To run the blockchain implementation:

```bash
python pychain.py
```

## Security Features

-   Proof of work mechanism requiring 4 leading zeros in block hashes
-   Transaction validation to ensure positive amounts
-   Cryptographic hashing using SHA-256
-   Block linking through previous hash references

## Future Improvements

Potential enhancements could include:

-   Wallet implementation
-   Network communication between nodes
-   Transaction pool
-   Mining rewards
-   Block difficulty adjustment
-   Chain validation
