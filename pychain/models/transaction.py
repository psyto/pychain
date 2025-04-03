"""
Transaction class represents a single transaction.
Contains:
- sender: who is sending the coins
- receiver: who is receiving the coins
- amount: how many coins are being transferred
"""

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount 