import random
dub = random.randint(1,80)

terst = (1,2,3)
test_list = [1, 2]
random_num = random.choice(test_list)
num = random_num
print("Welcome tto the wonderful world of zezuz! This is a word of mystery and adventure, i wonder how youl travel these lands")
name = input("what is your name brave traveler")
cash = 20
v = 0
c = v 
q = ""
w = ""
e = ""
r = ""
t = ""
y = ""
u = ""
i = ""
o = ""

hel = 100
while hel > 0:
    worp = input("what do you want to do? (w to walk, p for inventory) ")
    inv = (f"name: {name} health: {hel} cash: {cash} other items: {q} {w} {e} {r} {t} {y} {u} {i} {o}")
    random_num = random.choice(test_list)
    num = random_num
    
    terst = (1,2,3)
    lel = random.choice(terst)
    if worp == "p":
            print(inv)
    if worp == "w":
        v = v + 5
        if v / 5 == num:
            if lel == 1 :
                 heli = 75
                 hal = dub / 0.75
                 print("you ran into a feral frogll!")
                 while heli > 0 and hel > 0:
                    dam = input("do you want to run (r) or fight (f)")
                    if dam == "r":
                        nem = random.choice(test_list)
                        if nem == 3:
                            print("you ran away!")
                        while heli > 0 and hel > 0 :
                           dub = random.randint(1,80)
                           hal = dub / 0.75 
                           hel = hel - dub
                           print(hel)
                           dub = random.randint(1,80)
                           heli = heli - dub
                           print(heli)
                           if heli <= 0:
                               print("you won!")
                               dub = random.randint(1,25)
                               dam = random.randint(1,2)
                               if dam == 2:
                                   lool = random.randint(1,3)
                                   if lool == 1:
                                       q = "frog legs"
                                   if lool == 2:
                                       w = "fly sword"
                                   if lool == 3:
                                       e = "frog tounge"  
                               cash = cash + dub
                               break
                           if hel <= 0:
                               print ("you lost!")
                               break
                    if dam == "f":
                        while heli > 0 and hel > 0:
                           dub = random.randint(1,80)
                           heli = heli - dub
                           print(heli)
                           dub = random.randint(1,80)
                           hal = dub / 0.75 
                           hel = hel - dub
                           print(hel)
                           if heli <= 0:
                               print("you won!")
                               dub = random.randint(1,25)
                               dam = random.randint(1,2)
                               if dam == 2:
                                   lool = random.randint(1,3)
                                   if lool == 1:
                                       q = "frog legs"
                                   if lool == 2:
                                       w = "fly sword"
                                   if lool == 3:
                                       e = "frog tounge" 
                               heli = heli + 25
                               cash = cash + dub
                           if hel <= 0:
                               print ("you lost!")
            if lel == 2:
                 heli = 100
                 print("you ran into a solder!")
                 while heli > 0 and hel > 0:
                    dam = input("do you want to run (r) or fight (f)")
                    if dam == "r":
                        nem = random.choice(test_list)
                        if nem == 3:
                            print("you ran away!")
                        while heli > 0 and hel > 0:
                           dub = random.randint(1,80)
                           hal = dub / 0.75 
                           hel = hel - dub
                           print(hel)
                           dub = random.randint(1,80)
                           heli = heli - dub
                           print(heli)
                           if heli <= 0:
                               print("you won!")
                               dub = random.randint(1,25)
                               dam = random.randint(1,2)
                               if dam == 2:
                                   lool = random.randint(1,3)
                                   if lool == 1:
                                       r = "knife"
                                   if lool == 2:
                                       t = "sword"
                                   if lool == 3:
                                       y = "armor" 
                               cash = cash + dub
                               break
                           if hel <= 0:
                               print ("you lost!")
                               break
                    if dam == "f":
                        while heli > 0 and hel > 0:
                           dub = random.randint(1,80)
                           heli = heli - dub
                           print(heli)
                           dub = random.randint(1,80)
                           hal = dub / 0.75 
                           hel = hel - dub
                           print(hel)
                           if heli <= 0:
                               print("you won!")
                               dub = random.randint(1,25)
                               dam = random.randint(1,2)
                               if dam == 2:
                                   lool = random.randint(1,3)
                                   if lool == 1:
                                       r = "knife"
                                   if lool == 2:
                                       t = "sword"
                                   if lool == 3:
                                       y = "armor" 
                               heli = heli + 25
                               cash = cash + dub
                               break
                           if hel <= 0:
                               print ("you lost!")
                               break 
            if lel == 3:
                heli = 50
                hal = dub * 1.25
                print("you ran into a witch!")
                while heli > 0 and hel > 0:
                    dam = input("do you want to run (r) or fight (f)")
                    if dam == "r":
                        nem = random.choice(test_list)
                        if nem == 3:
                            print("you ran away!")
                        while heli > 0 and hel > 0:
                           dub = random.randint(1,80)
                           hal = dub / 0.75 
                           hel = hel - dub
                           print(hel)
                           dub = random.randint(1,80)
                           heli = heli - dub
                           print(heli)
                           if heli <= 0:
                               print("you won!")
                               dub = random.randint(1,25)
                               dam = random.randint(1,2)
                               if dam == 2:
                                   lool = random.randint(1,3)
                                   if lool == 1:
                                       u = "potion"
                                   if lool == 2:
                                       i = "witches hat"
                                   if lool == 3:
                                       o = "wand" 
                               cash = cash + dub
                               break
                           if hel <= 0:
                               print ("you lost!")
                               break
                    if dam == "f":
                        while heli > 0 and hel > 0:
                           dub = random.randint(1,80)
                           heli = heli - dub
                           print(heli)
                           dub = random.randint(1,80)
                           hal = dub * 1.25 
                           hel = hel - dub
                           print(hel)
                           if heli <= 0:
                               print("you won!")
                               dub = random.randint(1,25)
                               dam = random.randint(1,2)
                               if dam == 2:
                                   lool = random.randint(1,3)
                                   if lool == 1:
                                       u = "potion"
                                   if lool == 2:
                                       i = "witches hat"
                                   if lool == 3:
                                       o = "wand" 
                               heli = heli + 25
                               cash = cash + dub
                               break
                           if hel <= 0:
                               print ("you lost!")
                               break
    if hel <= 0:
        print("you lost the game")
        break
    if v >= 15:
         v = 0