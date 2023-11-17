no = int(input("how deep into fibi do you want to go? "))

def fibonacci(num):
    for i in range(num):
        x = i
        y = x
        z = x + y
        x = z
        print(x)

fibonacci(no)