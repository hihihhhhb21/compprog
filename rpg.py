import random
test_list = [1, 2,]
random_num = random.choice(test_list)
num = random_num
print("Welcome tto the wonderful world of zezuz! This is a word of mystery and adventure, i wonder how youl travel these lands")
name = input("what is your name brave traveler")
kni = 10
gun = 20
swo = 15
v = 0
c = v 
while True:
    worp = input("what do you want to do? (w to walk, p for inventory) ")
    inv = "test"
    random_num = random.choice(test_list)
    num = random_num
    print(num)
    if worp == "p":
            print(inv)
    if worp == "w":
        v = v + 5
        if v / 5 == num:
            print(name)     
    if v >= 15:
         v = 0
    print(v)