import random
n=random.randint(1,10)
guess=0
while guess!=n:
    guess=int(input("enter the number"))
    if guess < n:
        print('the number is small')
    elif guess > n:
        print('the number is big')
    else:
        print('yes that is the number')