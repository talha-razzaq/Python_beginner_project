
### list overlap



mylist1 = []
mylist2 = []

result_list = []

while True:
    num1 = input("Enter the input for num1 : ")
    if num1 == "q":
        break
    
    mylist1.append(num1)

print()

while True:
    num2 = input("Enter the input for num2 : ")
    if num2 == "q":
        break
    
    mylist2.append(num2)

print()

print("This is list 1: ", mylist1)
print()
print("This is list 2: ", mylist2)

print()
for elements in mylist1:
    if elements in mylist2:
        result_list.append(elements)

print("All are common in both lists", result_list)
