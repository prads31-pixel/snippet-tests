def printAge():
    print("This is a function to print age.")
    age = input("Enter your age: ")
    print("You entered age: ", age)

    if (age.isdigit()):
        age = int(age)
        if age < 18:
            print("You are a minor.")
        elif age < 65:
            print("You are an adult.")
        else:
            print("You are a senior.")
    else:
        input("Please enter a valid integer for age: ")


def add_numbers(a, b):
    return a + b


result = add_numbers(5, 10)
print("The result of adding 5 and 10 is: ", result)


def atm_withdrawal(withdrawal_amount):
    current_balance = 1000
   
    if withdrawal_amount > current_balance:
        print("Insufficient funds.")
        return False
    
    if withdrawal_amount % 500 != 0:
        print("Withdrawal amount must be in multiples of 500.")
        return False
    
    current_balance -= withdrawal_amount
    print("Withdrawal successful. Remaining balance: ", current_balance)
    return True

print("Lets check the ATM withdrawal function.")
amount = int(input("Enter withdrawal amount: "))
result = atm_withdrawal(amount)
print("return: ", str(result))

    
