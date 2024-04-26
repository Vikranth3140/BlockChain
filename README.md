# Simple Blockchain Implementation in Python

This is a simple blockchain implementation in Python. It includes functionalities such as adding users, adding transactions, mining blocks, verifying the chain's integrity, exploring the blockchain, and exiting the program through a menu-driven command-line interface (CLI).

## Functionality

- **Add User**: Add a new user to the blockchain with an initial balance.
- **Add Transaction**: Perform a transaction between users, transferring tokens from one user to another.
- **Mine Block**: Validate pending transactions, create a new block, and reward the miner with tokens.
- **Verify Chain**: Check if the blockchain is valid and has not been tampered with.
- **Explore Blockchain**: View all blocks in the blockchain and the current pending transactions.
- **Exit**: Quit the program.

## Requirements

- Python
- hashlib
- json
- time

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Vikranth3140/BlockChain.git
   ```

2. Navigate to the project directory:

   ```bash
   cd BlockChain
   ```

2. Install the requred dependancies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the BlockChain program:

   ```bash
   python main.py
   ```

5. Follow the on-screen instructions to interact with the blockchain:

   - Add users with initial balances.
   - Add transactions between users.
   - Mine blocks to validate transactions and earn mining rewards.
   - Verify the integrity of the blockchain.
   - Explore the blockchain to view blocks and transactions.
   - Exit the program.

## License

This project is licensed under the [MIT License](LICENSE).