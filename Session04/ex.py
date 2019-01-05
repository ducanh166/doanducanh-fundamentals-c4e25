#from random import randint
#customize
nums = [-1, 8, -7, 99, -99, 100]
min_num = 99999
for index, num in enumerate(nums):
    if num < min_num:
        min_num = num
        min_index = index

print(min_num)
print(min_index)
