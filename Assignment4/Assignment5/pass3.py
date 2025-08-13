actual_user_id = input("Set user ID for this session: ")
actual_password = input("Set password for this session: ")

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_id = input("Enter user ID: ")
    password = input("Enter password: ")
    
    if user_id == actual_user_id and password == actual_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect credentials. {remaining_attempts} attempts remaining.")
else:
    print("Max attempts reached. Program terminating.")

