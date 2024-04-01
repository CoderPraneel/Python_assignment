def validate_password(password, username, l):
    # Minimum Length Check
    if len(password) < 10:
        return False, "Password must be at least 10 characters long."
    
    # Character Variety Check
    u_cnt = sum(1 for c in password if c.isupper())
    l_cnt = sum(1 for c in password if c.islower())
    d_cnt = sum(1 for c in password if c.isdigit())
    s_cnt = sum(1 for c in password if not c.isalnum())
    
    if u_cnt < 2 or l_cnt < 2 or d_cnt < 2 or s_cnt < 2:
        return False, "Password must contain at least two uppercase letters, two lowercase letters, two digits, and two special characters."
    
    # Sequence and Repetition Restrictions
    for i in range(len(password) - 2):
        if password[i:i+3] in username:
            return False, "Password should not contain a sequence of three or more consecutive characters from the username."
        if password[i] == password[i+1] == password[i+2]:
            return False, "No character should repeat more than three times in a row."
    
    # Historical Password Check
    if password in l:
        return False, "Password must not be the same as the last three passwords."
    
    return True, "Password is valid."


username = input("Enter your username: ")
l = []  # Placeholder for last three passwords, assuming this list is maintained

while True:
    password = input("Enter a new password: ")
    is_valid, m = validate_password(password, username, l)
    if is_valid:
        print("Password set successfully.")
        break
    else:
        print("Invalid Password:", m)
