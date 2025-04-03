# Python Blockchain Implementation

A simple blockchain implementation in Python that demonstrates the core concepts of blockchain technology including proof of work, transaction validation, and block creation.

## Features

-   Block creation with proof of work
-   Transaction validation
-   SHA-256 hashing
-   Genesis block creation
-   Blockchain structure with linked blocks

## Project Structure

```
pychain/
├── __init__.py
├── __main__.py
├── blockchain.py
├── models/
│   ├── __init__.py
│   ├── block.py
│   └── transaction.py
└── utils/
    ├── __init__.py
    ├── hash_utils.py
    └── validation.py
```

### Components

1. **Models**

    - `Block`: Represents a single block in the blockchain
    - `Transaction`: Represents a single transaction

2. **Utils**

    - `hash_utils.py`: Contains hash calculation and proof of work functions
    - `validation.py`: Contains transaction validation functions

3. **Core**
    - `blockchain.py`: Main Blockchain class that manages the chain
    - `__main__.py`: Entry point for running the blockchain

## Usage

### As a Package

```python
from pychain import Blockchain, Transaction

# Initialize blockchain
blockchain = Blockchain()

# Create transactions
transactions = [
    Transaction("Alice", "Bob", 50),
    Transaction("Bob", "Charlie", 25)
]

# Add blocks to the chain
new_block = blockchain.add_block(transactions)
if new_block:
    print(f"Block #{new_block.index} added to the blockchain!")
    print(f"Hash: {new_block.hash}")
```

### Running the Demo

To run the demo implementation:

```bash
python -m pychain
```

## Requirements

-   Python 3.x
-   Standard library modules:
    -   hashlib
    -   time

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
