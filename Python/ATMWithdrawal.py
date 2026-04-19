# Question 1: ATM Withdrawal System

from unittest import result


def atm_withdrawal(withdrawal_amount):
    current_balance = 5000

    # Validation 1: Withdrawal amount must be greater than 0
    if withdrawal_amount <= 0:
        print("Error: Withdrawal amount must be greater than 0")
        return False   
    
    # Validation 2: Withdrawal amount must be a multiple of 500
    if withdrawal_amount % 500 != 0:
        print("Error: Withdrawal amount must be multiple of 500")
        return False   

    # Validation 3: Account balance must be sufficient for withdrawal
    if withdrawal_amount > current_balance:
        print(f"Error: Insufficient balance. Available: {current_balance}")
        return False    

    # Validations passed, perform withdrawal
    current_balance -= withdrawal_amount
    print("Withdrawal successful. Remaining balance: ", current_balance)
    result = {"amount": withdrawal_amount, "remaining_balance": current_balance, "status": "success", "return": True}
    return result



print("Lets check the ATM withdrawal function.")
while True:
    amount = int(input("Enter withdrawal amount: "))
    result = atm_withdrawal(amount)
    if result and result.get("return"):
        print("Withdrawal successful. Amount: ", str(result["amount"]))
        print("Remaining balance: ", str(result["remaining_balance"]))
        print("Return: ", str(result["return"]))
        break
    else:
        False