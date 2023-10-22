
# Check the prime number 

flag = 0


while True:
    num = int(input("Enter the number : "))

    if num == 1:
        print(num, "is not a prime number !!!")

    elif num == 1111:
        break

    elif num > 1:
        # run a for loop
        for i in range(2, num):

            if num % i == 0:
                
                flag = True
                break
        if flag == True:
            print(num, "is not a prime number !!!")

        else:
            print(num,"is a prime number ")
        
