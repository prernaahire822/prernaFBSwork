actual_user_id = "metauser"
actual_password = "metapass"

user_id = input("Enter user ID: ")
password = input("Enter password: ")

if user_id == actual_user_id and password == actual_password:
    print("Login successful!")
else:
    print("Incorrect user ID or password.")


