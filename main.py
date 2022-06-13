import random
option = ["R","P","S"]
for x in option:
    user = input("Choose[R for Rock, P for Paper, S for Scissors)]: ")
    user =user.upper()
    computer = random.choice(option)
    if user == "R":
        print(f"Player:{user}, CPU:{computer}")
        if computer == "S":
            print("User Wins!")
        elif user==computer:
            print("It's a tie")
        else:
            print("CPU Wins!")
            break
    elif user == "P":
        print(f"Player:{user}, CPU:{computer}")
        if computer=="S":
            print("CPU Wins")
        elif user==computer:
            print("It's a tie")
        else:
            print("User Wins!")
            break
    elif user=="S":
        print(f"Player:{user}, CPU:{computer}")
        if computer=="P":
            print("User Wins!")
        elif user==computer:
            print("It's a tie")
        else:
            print("CPU WIns!")
            break

