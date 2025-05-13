 💰 Banking System in Python - Project Proposal
The goal of this project is to create a simple banking system, using basic Python concepts, such as lists, dictionaries, functions and loops. We will structure the project in stages, creating essential functionalities to manage bank accounts and their operations.Detailed Features:

1.Customer Registration:
Allows the creation of bank accounts.
Each account will have the following attributes:
Name: Full name of the customer.
CPF: Unique identifier for each customer (simulating a real bank).
Initial Balance: Initial amount deposited in the account.
The CPF will be the unique key to identify customers.
Accounts will be stored in a dictionary, where the CPF will be the key and the account data will be the amount.

2. Deposit:
Allows theuser to deposit an amount into their account.
The user must provide the account CPF and the amount of the deposit.
The amount will be added to the account balance.
The transaction will be recorded on the statement as "Deposit".

3. Withdrawal:
Allows the user to withdraw an amount from their account.
The user must provide their CPF and the amount to be withdrawn.
Before withdrawing, the system checks whether the balance is sufficient.
If the balance is insufficient, an error message will be displayed.
The transaction will be recorded on the statement as "Withdrawal"

4. Transfer:
Allows the user to transfer amounts between different accounts.
The user must provide the source CPF, destination CPF and the amount to be transferred.
The system checks the balance of the source account before making the transfer.
The transaction will be recorded in the statement of both accounts:
In the source account as "Transfer Sent".
In the destination account as "Transfer Received".

5.Statement:
Displays the complete transaction history of the account.
The user must provide their CPF to view the statement.
Each transaction (deposit, withdrawal and transfer) will be recorded with date, time and amount.

6.Login/Logout:
Basic authentication system.
The user must enter their CPF and a password to access their account.
When logging in, the system checks whether the CPF and password are valid.
Logging out ends the user's session.

System Structure:
Database (simulated): We will use a dictionary to store the accounts.
Functions: Each functionality will be implemented in a separate function.
Interactive Menu: The system will have a looping menu that allows the user to choose the operation to be performed.
Exceptions and Error Handling: We will implement checks for duplicate CPF, insufficient balance, etc.

