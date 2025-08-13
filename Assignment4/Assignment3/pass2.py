user_id = input("Enter user ID: ")
password = input("Enter password: ")

confirm_user_id = input("Confirm user ID: ")
confirm_password = input("Confirm password: ")

if user_id == confirm_user_id and password == confirm_password:
    captcha = "1234"
    print(f"CAPTCHA: {captcha}")
    user_captcha = input("Enter the CAPTCHA number: ")
    
    if user_captcha == captcha:
        print("Success! CAPTCHA entered correctly.")
    else:
        print("Failed. CAPTCHA did not match.")
else:
    print("User ID or password did not match confirmation.")
