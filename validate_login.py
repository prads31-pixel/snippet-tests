def validate_login(username, password):
    
    if len(username) < 5:
        print("Error: Username must be at least 5 characters")
        return False
    if len(password) < 8:
        print("Error: Password must be at least 8 characters")
        return False
    
    password_has_digit = False
    for char in password:        
        if char.isdigit():
            password_has_digit = True
            break
    if not password_has_digit:
        print("Error: Password must contain at least one digit")
        return False
    
    result = {"message": "Login successful", "return": True}
    return result

print("Lets check the login validation function.")
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    result = validate_login(username, password)
    if result and result.get("return"):
        print(result.get("message"))
        print("Return: ", str(result["return"]))
        break
    else:
        False