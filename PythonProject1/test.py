#print ("Hello World")
#can vot or no
'''
a=int(input("enter ur age"))
if a > 18:
    print("can vote")
else:
    print("cant vote")

a=int(input())
b=int(input())
print(a+b)#concatenation as by default it takes string


#write a program to simulate siimple calculator with an help of if elif statement
#read 2 input from end user as well as read tone opertor
a=int(input())
b=int(input())
op=input()
if op == '+':
    print(f"sum is {a+b}")
elif op == '-':
    print(f"diff is {a-b}")

#list of prime no present between 1 to 10
n = 10
for i in range (1,n+1):
    count = 0
    for j in range(1,i+1):
            if i%j ==0:
                count+=1
    if count ==2:
        print(i)
'''
#another method
num=14
isprime = True
def primeno(num):
    for i in range(2,num-1):
        if num % i== 0 :
            return False
    return True

for i in range(2,num):
    if primeno(i):
        print(i)

'''
def date_fashion(you, date):

    if you >= 8 or date >= 8:
        return  2
    elif you <= 2 or date<=2:
        return 0
    else:
        return  1


n=date_fashion(5,10)
print(n)

#write a program to print sum of digits present in a given numbers
n=1234
sum=0
while(n!=0):
    rem=n%10
    if rem % 2 == 0:
        sum += rem
    n = n // 10

print(sum)
'''