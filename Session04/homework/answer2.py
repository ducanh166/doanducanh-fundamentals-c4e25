print('''Estimate this answer (exact calculation not needed)
Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?''')
answer = ["About 55", "About 65", "About 75", "About 85"]
for index, item in enumerate(answer):
    print(index +1, item, sep=". ")
print()
m = int(input("Your choice: "))
if m != 2:
    print(":(")
elif m ==2:
    print("Bingo")
else:
    pass

print()