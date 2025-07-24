number=int(input("enter the number"))
count = 0
if number <=0:
    print(f"{number} is not prime")
else:
    for i in range(1,number+1):
        if number%i==0:
            count+=1
        if count ==2:
            print("it is a prime number")
        else:
            print("not")
