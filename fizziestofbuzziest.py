lol = input("what for fizz? ")
lal = input("what for buzz? ")
lel = input("what num to buzz? ")
for i in range(int(lel)+1):
    if i % 2 != 0 and i % 3 != 0 and i % 4 != 0 and i % 5 != 0 and i % 6 != 0 and i % 7 != 0 and i % 8 != 0 and i % 9 != 0:
        print("prime")
    elif i % 3 == 0 and i % 5 == 0:
        print(f"{lol}{lal}")
    elif i % 5 == 0:
        print(lal)
    elif i % 3 ==0:
        print(lol)
    elif i % 3 != 0 and i % 5 != 0:
        print(i)