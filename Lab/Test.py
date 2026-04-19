s = "I like your, book"
s = s.replace("your", "")

s = "cat dog cat bird cat"
s = s.replace("cat", "lion", 2)
print (s)   

s = "abc;def;ghi;jkl"
#def;ghi
start = s.index(";") + 1
end = s.rindex(";")
print(s[start:end])

s = "abc;def;ghi"
print(s.rindex(";"))

print(s.split(";"))

a = s.index(";")

print(s[a+1:])



s= "This is easy"
print(s.find(" is "))
print(s.index("is"))

s = "one two three four two six one seven one"
print(s.rindex("one"))



s="*****   hello world   ******     "

s = s.strip().strip("*").strip()
s = s.title()

print(s)
#Hello World



def  atm_withdrawal(withdrawal_amount):

    current_balance = 5000

    if withdrawal_amount <= 0:

        print("Error: Withdrawal amount must be greater than 0")

    elif withdrawal_amount >= current_balance:

        print(f"Error: Insufficient balance. Available: {current_balance}")

    elif withdrawal_amount % 500 != 0:

        print("Error: Withdrawal amount must be multiple of 500")

    else:

        rem_balance = current_balance - withdrawal_amount

        print(f"""Withdrawal successful. Amount: {withdrawal_amount} /-

 Remaining Balance: {rem_balance} /-""")

withdraw = int(input("Please enter an amount to withdraw:  "))

atm_withdrawal(withdraw)