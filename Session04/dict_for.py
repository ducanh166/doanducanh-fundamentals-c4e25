person = {
    "name": "Quan",
    "age": 25,
    "location": "Hanoi",

}
#for x in person.keys():
   # print(k)
#for v in person.values():
   # print(v)

for k,v in person.items():
    print(k, v, sep=": ")