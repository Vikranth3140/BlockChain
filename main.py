import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.users = {}  # User accounts with balances
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash,
            'transactions': self.current_transactions,
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - last_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    def add_user(self, username, initial_balance):
        if username not in self.users:
            self.users[username] = initial_balance
            print(f"User '{username}' added with balance {initial_balance}.")
        else:
            print(f"User '{username}' already exists.")

    def get_sender_balance(self, sender):
        return self.users.get(sender, 0)  # Default to 0 if user not found

def add_transaction(blockchain, sender, recipient, amount):
    # Validate transaction
    if sender == '' or recipient == '' or amount <= 0:
        print("Invalid transaction details.")
        return

    # Check sender balance
    sender_balance = blockchain.get_sender_balance(sender)
    if sender_balance < amount:
        print("Insufficient balance.")
        return

    # Add transaction to current transactions
    blockchain.current_transactions.append({
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    })
    print("Transaction added successfully!")

def mine_block(blockchain):
    last_block = blockchain.get_last_block()
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)
    print("Block mined successfully!")

def verify_chain(blockchain):
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        print("The blockchain is valid.")
    else:
        print("The blockchain is not valid.")

def print_blockchain(blockchain):
    print("Blockchain:")
    for block in blockchain.chain:
        print(block)
    print("Current Transactions:")
    print(blockchain.current_transactions)

def main():
    blockchain = Blockchain()
    blockchain.add_user("Alice", 100)  # Example user with initial balance

    while True:
        print("\nMenu:")
        print("1. Add User")
        print("2. Add Transaction")
        print("3. Mine Block")
        print("4. Verify Chain")
        print("5. Explore Blockchain")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            balance = float(input("Enter initial balance: "))
            blockchain.add_user(username, balance)

        elif choice == '2':
            sender = input("Enter sender: ")
            recipient = input("Enter recipient: ")
            amount = float(input("Enter amount: "))
            add_transaction(blockchain, sender, recipient, amount)

        elif choice == '3':
            mine_block(blockchain)

        elif choice == '4':
            verify_chain(blockchain)

        elif choice == '5':
            print_blockchain(blockchain)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()