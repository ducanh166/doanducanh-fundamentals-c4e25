a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))

delta = b*b - 4*a*c

if delta < 0:
    print("no solution")
elif delta == 0:
    x = -b/(2*a)
    print("1 solution x=",x)
else:
    delta_sqrt = delta**0,5
    x1 = (-b + delta_sqrt)/(2*a)
    x2 = (-b - delta_sprt)/(2*a)
    print("2 solution, x1=",x1, "x2=",x2)