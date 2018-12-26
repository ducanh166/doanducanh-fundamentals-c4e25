loop = True
while loop:
    pwd = input("Enter your password: ")
    loop = False
    if len(pwd) < 8:
        loop = True
    if pwd.isalnum():
        loop =  True
    if pwd.isdigit():
        loop = True
    if pwd.isalpha():
        loop =  True

print("Password ok")