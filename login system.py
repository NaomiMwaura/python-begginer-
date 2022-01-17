print("create account")
username = input("enter user name: ")
password = input("enter password: ")
passwordb = input("re-enter the password for confirmation: ")
if password == passwordb:
    print("account has been created successfully")
else:
    print("the passwords do not match!")

print("Login now!")
username2 = input("enter the username: ")
password2 = input("enter the password: ")

if username == username2 and password == password2:
    print("you have loged in successfully!")
else:
    print("incorrect username or password. Please try again!")