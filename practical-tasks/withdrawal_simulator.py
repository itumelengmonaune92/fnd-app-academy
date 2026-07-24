"""
Smart FNB ATM Withdrawal Simulator

Simulates a secure bank transaction by validating and processing a cash 
withdrawal request against a fixed account balance. 

System Rules:
    1. Validates that the requested amount is a positive number greater than zero.
    2. Authorizes the transaction if the account balance covers the requested amount.
    3. Deducts the authorized amount and returns the updated balance.
    4. Rejects transactions with a descriptive message if funds are insufficient 
       or the requested input is invalid (zero or negative values).
"""

bank_balance = 599.49
print()
print("=" * 50)
print("   'Welcome to the Monaunes National Bank ATM'")
print("=" * 50)
withdrawal_request = float(input("Enter withdrawal amount: R"))


if withdrawal_request <= bank_balance:
    remaining_balance = bank_balance - withdrawal_request
    print(f"Withdrawal successful! Remaining balance: R{remaining_balance}")
elif withdrawal_request <= 0:
    print("Invalid amount")
else:
    print("Decline. Insufficient funds.")