nam = input("welcome to the interview, what is your name?")
choice = input(f"ok {nam} what position are you interested in?(computer programer, software enginer, team leader, analyst, senior developer, or junior developer)")
cho = choice
q = input(f"your interested in being a {choice} is this correct?")
if q == "n":
    print("restart code please")
elif q == "y":
    if choice == "computer programer":
        w = input(f"{nam} how many years of experiance do you have? ")
        if int(w) <= 2:
            e = input(f"so {nam}, the starting sallery for your experience is 63k and up to 100k. are you still interested? ")
        if e == "y":
            print("you got the job.")
        if e == "n":
            print("ok, thank you for your time.")
        if int(w) >= 2:
            print("you are not qualified for this job.")
elif q == "y":
    if choice == "software enginer":
        w = input(f"{nam} how many years of experiance do you have? ")
        if w <= 3:
            e = input(f"so {nam}, the starting sallery for your experience is 32k and up to 98k. are you still interested? ")
        if e == "y":
            print("you got the job.")
        if e == "n":
            print("ok, thank you for your time.")
        if w >= 3:
            print("you are not qualified for this job.")
elif q == "y":
    if choice == "team leader":
        w = input(f"{nam} how many years of experiance do you have? ")
        if w <= 2:
            e = input(f"so {nam}, the starting sallery for your experience is 32k and up to 98k. are you still interested? ")
        if e == "y":
            print("you got the job.")
        if e == "n":
            print("ok, thank you for your time.")
        if w >= 2:
            print("you are not qualified for this job.")
elif q == "y":
    if choice == "analyst":
        w = input(f"{nam} how many years of experiance do you have? ")
        if w <= 2:
            e = input(f"so {nam}, the starting sallery for your experience is 32k and up to 98k. are you still interested? ")
        if e == "y":
            print("you got the job.")
        if e == "n":
            print("ok, thank you for your time.")
        if w >= 2:
            print("you are not qualified for this job.")
elif q == "y":
    if choice == "senior developer":
        w = input(f"{nam} how many years of experiance do you have? ")
        if w <= 2:
            e = input(f"so {nam}, the starting sallery for your experience is 32k and up to 98k. are you still interested? ")
        if e == "y":
            print("you got the job.")
        if e == "n":
            print("ok, thank you for your time.")
        if w >= 2:
            print("you are not qualified for this job.")
elif q == "y":
    if choice == "junior developer":
        w = input(f"{nam} how many years of experiance do you have? ")
        if w <= 2:
            e = input(f"so {nam}, the starting sallery for your experience is 32k and up to 98k. are you still interested? ")
        if e == "y":
            print("you got the job.")
        if e == "n":
            print("ok, thank you for your time.")
        if w >= 2:
            print("you are not qualified for this job.")
#2 - 4 years exp for computer programer
#63k - 100k sallery for computer programer
#3 - 5 years exp for software enginer
#74k - 190k sallery for software enginer
#2 years on job exp for team leader
#32k - 98k sallery for team leader
#2 - 4 years exp for analyst
#57k - 110k sallery for analyst
#3 - 7 years exp for senior developer
#120k - 170k sallery for senior developer
#3 - 5 years exp for junior developer
#87k - 130k sallery for junior developer