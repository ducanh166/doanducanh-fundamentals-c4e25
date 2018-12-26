x = int(input("Chieu cao cua ban(cm) = "))
y = int(input("Can nang cua ban(kg) = "))
z = y / 100
bmi = y / z**2
print("BMI cua ban =",bmi)

if bmi < 16:
    print("serverly underweight")
elif bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
else:
    print("obese")

print("Have nice a nice day")