import random
def randomize(A,n):
    print("your numbers:")
    for i in range (n):
        A.append(random.randint(0,n))
    print(A)
