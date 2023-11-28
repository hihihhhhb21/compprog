import random
def get_random_word():
    with open('sowpods.txt', 'r') as f:
        lines = f.readlines()
        words = [word for line in lines for word in line.split()]
        return random.choice(words)
v = 0
z = "|‾‾‾˥","|   (", "|   )", "|    ", "|      ", "|     ","L_______"
x = "|‾‾‾˥","|   (", "|   )", "|   O", "|      ", "|     ","L_______"
r = "|‾‾‾˥","|   (", "|   )", "|   O", "|   |  ", "|     ","L_______"
c = "|‾‾‾˥","|   (", "|   )", "|   O", "|  /| ", "|     ","L_______"
b = "|‾‾‾˥","|   (", "|   )", "|   O", "|  /|\ ", "|     ","L_______"
p = "|‾‾‾˥","|   (", "|   )", "|   O", "|  /|\ ", "|    \ ","L_______"
o = "|‾‾‾˥","|   (", "|   )", "|   O", "|  /|\ ", "|  / \ ","L_______"
print("Welcome to Hangman!")
for i in z:
    print(i)
word = get_random_word()
guessed_letters = [] 
def display_clue(word, guessed_letters):
    clue = ""
    for letter in word:
        if letter.lower() in guessed_letters or letter.upper() in guessed_letters:
            clue += letter + " "
        else:
            clue += "_ "
    return clue
while True:
    #print(word)
    print(display_clue(word, guessed_letters))
    guess = input("Guess your letter: ").upper() 
    if guess in guessed_letters:
        print(f"You've already guessed that letter!")
        continue
    if guess not in word:
       v = v + 1
    if v == 0:
        for i in z:
               print(i) 
    if v == 1:
           for i in x:
               print(i) 
    if v == 2:
           for i in r:
               print(i) 
    if v == 3:
           for i in c:
               print(i) 
    if v == 4:
           for i in b:
               print(i) 
    if v == 5:
           for i in p:
               print(i)
    if v == 6:
           for i in o:
               print(i)
    if v >= 6:
        print(f"your word was {word}")
        guessed_letters = [] 
        word = get_random_word()
        w = input("reastart?(y or n) ")
        if w == 'y':
           v = 0
        elif w == 'n':
              break
    print(f"you have failed {v} times out of 6 ")
    guessed_letters.append(guess)
    if all(letter.lower() in guessed_letters or letter.upper() in guessed_letters for letter in word):
        print(f"Congratulations! You guessed the word: {word}")
        guessed_letters = [] 
        word = get_random_word()
        w = input("reastart?(y or n) ")
        if w == 'y':
            v = 0
        elif w == 'n':
            break
