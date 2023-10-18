
number = int(input("Enter the number : ")) # 6

rangelist = list(range(1, number+1)) # (1,7)

divisorlist = []

for num in rangelist:
    if number % num == 0:
        divisorlist.append(num)


print(divisorlist)