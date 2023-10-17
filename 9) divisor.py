__author__ = 'Talha Razzaq'
print("Author is : ",__author__)

print("------------------------")

number = int(input("Enter the number : ")) #take input E.g 6

listrange = list(range(1,number+1))#range is 1,6+1=7 range(1,7)

divisorlist = [] #empty list in which we wil append all divisor

for num in listrange:
    if number % num == 0:
        divisorlist.append(num)
        divisorlist.sort()

print(divisorlist)
