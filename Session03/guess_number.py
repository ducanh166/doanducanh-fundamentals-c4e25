# sinh ra một số ngẫu nhiên từ 1 - 100
# nếu người dùng đoán đúng -> bingo
# nếu đoán sai thì đoán lại.
from random import randint
x = randint(1, 101)
print(x)
i = int(input("Enter a number: "))
while x != i:
    if i > x:
    print("A little too big")
    if i < x:
    print("A little too small")
    n = int(input("Your guess: "))
print("bingo")
