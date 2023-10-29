
# Remove duplicate list

#First we will take input for list.

mylist = []

while True:
    num = input("Enter the number : ")

    if num == "q":
        break

    mylist.append(num)

print(mylist)

def duplicate(mylist):
    empty_list = []

    for i in mylist:
        if i not in empty_list:
            empty_list.append(i)

    return empty_list

print(duplicate(mylist))