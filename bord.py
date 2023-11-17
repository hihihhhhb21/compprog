nam = input("what is your name?")
q = input(f"{nam} what job do you want?(computer programer, software enginer, team leader, analyst, senior developer, junior developer) ")
w = 6
if q == "computer programer":
    e = "36000 to 64000"
    r = 2
    t = 36000
    y = 64000
if q == "software enginer":
    e = "74000 to 190000"
    r = 3
    t = 74000
    y = 190000
if q == "team leader":
    e = "32000 to 98000"
    r = 2
    t = 32000
    y = 98000
if q == "analyst":
    e = "57000 to 110000"
    r = 2
    t = 57000
    y = 110000
if q == "senior developer":
    e = "120000 to 170000"
    r = 3
    t = 120000
    y = 170000
if q == "junior developer":
    e = "87000 to 130000"
    r = 3
    t = 87000
    y = 130000 
u = input(f"{nam} how many years of experience do you have? ")
if int(r) > int(u):
    z1 = 2
elif int(r) < int(u):
    z1 = 1
i = input(f"{nam} do you have a healthy socal life? ")
o = input(f"{nam} what age are you? ")
if int(o) - int(u) <= 18:
    z2 = 2
elif int(o) - int(u) >= 18:
    z2 = 1
p = input(f"{nam} are you emploed? ")
a = input(f"{nam} where are you living right now?")
s = input(f"{nam} what sallery do you want to be paid? ({e}) ")
if int(s) > int(y):
    z3 = 2
elif int(s) < int(y):
    z3 = 1
zz = z1 + z2 + z3
d = input(f"{nam} are you happy with your current living situation? ")
f = input(f"{nam} are you deppresed? ")
if z1 + z2 + z3 - w <= 2:
    g = "passed"
elif z1 + z2 + z3 - w >= 2:
    g = "didn't pass"
print(f"{nam} you {g}, job applied for {q}, years of exp {u}, social life {i}, age {o}, emploed {p}, place of living {a}, sallery wanted {s}, happy with home {d}, depresed {f} (you passed with a {zz} out of 6)")