test_list = (1,2,3)
import random
hel = 100
heli = 75
while True:
                    dam = input("do you want to run (r) or fight (f)")
                    if dam == "r":
                        nem = random.choice(test_list)
                        
                        if nem == 3:
                            print("you ran away!")
                            break
                        while True:
                           dub = random.randint(1,80)
                           heli = heli - dub
                           print(heli)
                           dub = random.randint(1,80)
                           hal = dub / 0.75 
                           hel = hel - dub
                           print(hel)

                    if dam == "f":
                        while True:
                           dub = random.randint(1,80)
                           heli = heli - dub
                           print(heli)
                           dub = random.randint(1,80)
                           hal = dub / 0.75 
                           hel = hel - dub
                           print(hel)
