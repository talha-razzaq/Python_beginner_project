
######Voting machine 
"""This is a voting macine in which there are two input name after this enter voter id which is in the form of list."""
#take two input

nominee1 = input("Enter the name of 1st nominess1 : ")
nominee2 = input("Enter the name of 1st nominess2 : ")

#Where loop start
nm1_vote = 0
nm2_vote = 0

#take voter id
voter_id = [1,2,3,4,5,6,7,8,9,10]

#how many votes should be
no_of_voter = len(voter_id)

#start loop
while True:
    voter = int(input("Enter the voter id : "))

    if voter in voter_id:
        print("Ok, you are a voter !!!")
        voter_id.remove(voter) #remove the voter id whose already voted

        print("-------------------------------------")
        print("To give vote ",nominee1, "| Press 1 |")
        print("To give vote ",nominee2, "| Press 2 |")
        print("-------------------------------------")

        vote = int(input("Enter the your previous vote : "))

        if vote == 1:
            nm1_vote += 1
            print(nominee1,"Thank you for vote to give me !!!")

        elif vote == 2:
            nm1_vote += 1
            print(nominee2,"Thank you for vote to give me !!!")

        elif vote > 2:
            print("You pressed",vote,"Please enter valid key")

        else:
            print("You are not vote OR You already have voted !!!")
    
    if voter_id == []:
        print("The voting session has over !!!")

        if nominee1 > nominee2:
            percent = (nm1_vote / no_of_voter) * 100
            print(nominee1,"has won the election with", percent,"% of votes !!!")

            break

        elif nominee1 > nominee2:
            percent = (nm1_vote / no_of_voter) * 100
            print(nominee1,"has won the election with", percent,"% of votes !!!")
            break

        else:
            print("Both opponent are equal !!! So, country law will dicide who will rule !!!")

            print()


print("Thank you for this !!!")
