yob_str = (input("Your year of birth?"))

    
while not yob_str.isdigit():
    print("Not a number, enter a again")
    yob_str = input("You year of birth")   
    
yob = int(yob_str)
age = 2018 - yob
print(age)
 