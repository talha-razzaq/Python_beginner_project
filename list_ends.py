### list ends


#first we take input and put it into a empty list.
end_list = []

while True:
    num = input("Enter the input here : ")

    if num == "q":
        break

    end_list.append(num)

print("This is your desire list : ", end_list)

#then create a def funcation in this code

def list_end(end_list):

    if len(end_list) >= 2:

        result = [end_list[0], end_list[-1]]

        return result
    
    else:
        return []
    

end_result = list_end(end_list)
print("This is our first and last value : ", end_result)