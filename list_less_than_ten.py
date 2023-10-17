
###List Less Than Ten

digits = [1, 1, 2, 4, 3, 5, 8, 13, 21, 34, 55, 89]

less_fnum = []
less_num = []

for num in digits:
    if num < 5:
        less_fnum.append(num)
        less_fnum.sort()
print()

print(less_fnum)

print("-----------------------------------")

number = int(input("Enter the number : "))

for n in digits:
    if n < number:
        less_num.append(n)
        less_num.sort()

print(less_num)

print("----------- The End -------------")