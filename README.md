Splitwise Debt Simplification Algorithm
A Python-based algorithm to simplify debts among a group of individuals, inspired by the Splitwise app. It identifies the minimum number of transactions required to settle all debts, ensuring each individual either gets paid back or repays their owed amount.

Description
The algorithm operates on the principle of minimizing transactions by always settling the highest debt with the highest credit. By iterating through the debt matrix, it calculates the net amount for each person, taking the difference between what they owe and what they are owed. After identifying the largest debtor and creditor, a transaction is performed between them. This process continues recursively until all debts are settled.

Note: The algorithm assumes that transactions can take any fractional value, and there's no limit on the number of transactions that can be executed simultaneously.

Usage
Define the number of people involved by setting the N variable.
Provide the transactions in a 2D matrix form. Rows denote the payer, and columns denote the payee. The value at graph[i][j] indicates the amount Person i owes to Person j.

graph = [
    [0, 1000, 500, 0],  # Debts of Person 0
    [0, 0, 1500, 500],  # Debts of Person 1
    [0, 0, 0, 500],     # Debts of Person 2
    [2000, 0, 0, 0]     # Debts of Person 3
]

amountCalculate(graph)
Example
For the above graph:

Person 1 will pay $ 1000 to Person 0
Person 2 will pay $ 1500 to Person 1
Person 2 will pay $ 500 to Person 0
Person 3 will pay $ 500 to Person 2
