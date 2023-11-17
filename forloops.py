

word= "paradigm"

for i in word:
    print(i)

for i in range(0,5):
    print(i)

animallist = ["cat", "dog", "tiger", "cow"]

for i in animallist:
    print(i)

flowers = ('jasmine', 'lotus', 'rose', 'sunflower')

for i in flowers:
    if i == 4:
        break
    else:
        print(i)


list1 = ['tomato','potatoes','carots','cucumbers']
list2 = ['5','10','15','20']

for i in list2:
    for j in list1:
        print(i,j)

vehicles = ['car', 'cycle', 'bus', 'tempo']

for i in vehicles:
    print(i)
    if i == 'cycle':
        break

for i in vehicles:
    print(i)
    if i == 'cycle':
        continue
            

numbers = [12,3,56,67,89,90]
count = 0

for i in numbers:
    count += 1
print(count)

sum = 0
for i in numbers:
    sum += i
    print(sum)
l = (5)
number = [2,5,6,10,15,20,25]
for i in number:
    print(i)
    if i == 2 or 6:
        break
    else:
        continue
    