# List comprehension

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
        even_list.sort()

print(even_list)


----------------------------------------------
#Another code example

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [num for num in a if num % 2 == 0]
print(b)
