p1 = input("what is player one? ")  
p2 = input("what is player two? ")

if p1 == "sissors" and p2 == "paper":
    print("you won player one!")
elif p1 == "rock" and p2 == "sissors":
    print("you won player one!")
elif p1 == "paper" and p2 == "rock":
    print("you won player one!")
elif p2 == "sissors" and p1 == "paper":
    print("you won player two!")
elif p2 == "rock" and p1 == "sissors":
    print("you won player two!")
elif p2 == "paper" and p1 == "rock":
    print("you won player two!")
elif p2 == p1:
    print("its a tie")