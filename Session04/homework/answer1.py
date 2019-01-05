print("Answer the following algebra question: ")
print("if x = 8, then what is the value of 4(x + 3) ?")
ans = {
    "35" : 1,
    "36" : 2,
    "40" : 3,
    "44" : 4,
}

for i in ans:
    print(ans[i] , i , sep = ". ")

kq = 44
kq = str(k)
kq_num = ans[kq]
loop = True
while loop:
    ans = int(input("Yor answer : "))
    loop = False
    if ans == kq_num:
        print("Bingo")
    else:
        print(":(")
        loop = True