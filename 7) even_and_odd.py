### Even and odd game

# take a input

num = int(input("Enter the number : "))

# use if-else conditions

if num == 0:
    print(num, "is not including in this game !!!")

elif num % 2 == 0:
    print(num, "is Even number !!!")

else:
    print(num, "is Odd number !!!")


print("---------------------- 2 exercise ---------------------------")
num = int(input("Enter the number : "))

if num % 4 == 0:
    print(num, "is a multiple of 4")

elif num % 2 == 0:
    print(num, "is a Even number !!!")

else:
    print(num, "is a Odd number !!!")

# Is num evenly divided on  check 
check = int(input("Enter the number : "))

if num % check == 0:
    print(num, "is Evenly divided on", check)

else:
    print(num, "is not Evenly divided on", check)
