import random
dub = random.randint(1,60)

terst = (1,2,3)
test_list = [1,2]
random_num = random.choice(test_list)
num = random_num
print("Welcome to the wonderful world of zezuz! This is a word of mystery and adventure, i wonder how you'll travel these winding lands ")
name = input("what is your name brave traveler ")
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
beaster = 0
beast = 0
armor = beaster + 1
damage = beast + 1
hel = 100
while hel > 0:
    worp = input("what do you want to do? (w to walk, p for inventory) ")
    inv = (f"name: {name} health: {hel} cash: {cash} other items: {q} {w} {e} {r} {t} {y} {u} {i} {o}")
    random_num = random.choice(test_list)
    num = random_num
    if q == "frog legs":
        beaster = 0.25
    if w == "fly sword":
        beast = 0.10
    if e == "frog tounge":
        beaster = 0.3
    if q == "frog legs" and e == "frog tounge":
        beaster == 1
    if q == "frog legs" and w == "fly sword" and e == "frog tounge":
        beaster = 1.25
        beast = 0.25
    if r == "knife":
        beast = 0.25
    if t == "sword":
        beast = 0.10
    if y == "armor":
        beaster = 0.3
    if r == "knife" and t == "sword":
        beast = 0.35
    if r == "knife" and t == "sword" and y == "armor":
        beaster = 0.75
        beast = 1
    if r == "potion":
        beaster = 0.25
    if t == "witches hat":
        beast = 0.10
    if y == "wand":
        beaster = 0.15
    if r == "potion" and t == "witches hat":
        beast = 0.45
    if r == "potion" and t == "witches hat" and y == "wand":
        beaster = 1.5
        beast = 0.5
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
                    dam = input("do you want to run (r) or fight (f) ")
                    if dam == "r":
                        nem = random.choice(test_list)
                        if nem == 2:
                            print("you ran away!")
                            break
                        while heli > 0 and hel > 0 :
                           dub = random.randint(1,60)
                           hal = dub / 0.75 
                           hel = hel - (dub / armor)
                           print(hel)
                           dub = random.randint(1,60)
                           heli = heli - (dub * damage)
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
                           dub = random.randint(1,60)
                           heli = heli - (dub * damage)
                           print(heli)
                           dub = random.randint(1,60)
                           hal = dub / 0.75 
                           hel = hel - (dub / armor)
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
                               hel = hel + 25
                               cash = cash + dub
                           if hel <= 0:
                               print ("you lost!")
            if lel == 2:
                 heli = 100
                 print("you ran into a solder!")
                 while heli > 0 and hel > 0:
                    dam = input("do you want to run (r) or fight (f) ")
                    if dam == "r":
                        nem = random.choice(test_list)
                        if nem == 2:
                            print("you ran away!")
                            break
                        while heli > 0 and hel > 0:
                           dub = random.randint(1,80)
                           hal = dub / 0.75 
                           hel = hel - (dub / armor)
                           print(hel)
                           dub = random.randint(1,80)
                           heli = heli - (dub * damage)
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
                                   hel = hel + 25 
                               cash = cash + dub
                               break
                           if hel <= 0:
                               print ("you lost!")
                               break
                    if dam == "f":
                        while heli > 0 and hel > 0:
                           dub = random.randint(1,60)
                           heli = heli - (dub * damage)
                           print(heli)
                           dub = random.randint(1,60)
                           hal = dub / 0.75 
                           hel = hel - (dub / armor)
                           print(hel)
                           if heli <= 0:
                               print("you won!")
                               dub = random.randint(1,25)
                               dam = random.randint(1,2)
                               if dam == 2:
                                   lool = random.randint(1,3)
                                   if lool == 1:
                                       r = "knife"
                                       print(f"you got a {r}")
                                   if lool == 2:
                                       t = "sword"
                                       print(f"you got a {t}")
                                   if lool == 3:
                                       y = "armor" 
                                       print(f"you got {y}")
                               hel = hel + 25
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
                    dam = input("do you want to run (r) or fight (f) ")
                    if dam == "r":
                        nem = random.choice(test_list)
                        if nem == 2:
                            print("you ran away!")
                            break
                        while heli > 0 and hel > 0:
                           dub = random.randint(1,80)
                           hal = dub / 0.75 
                           hel = hel - (dub / armor)
                           print(hel)
                           dub = random.randint(1,80)
                           heli = heli - (dub * damage)
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
                                   hel = hel + 25
                               cash = cash + dub
                               break
                           if hel <= 0:
                               print ("you lost!")
                               break
                    if dam == "f":
                        while heli > 0 and hel > 0:
                           dub = random.randint(1,80)
                           heli = heli - (dub * damage)
                           print(heli)
                           dub = random.randint(1,80)
                           hali = dub * 1.25 
                           hel = hel - (dub / armor)
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
                               hel = hel + 25
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