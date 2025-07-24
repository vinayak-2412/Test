# List
'''
a=[1,2,3,4]
print(a)
print(type(a))
print(len(a))
a[0]=20
for i in range(len(a)):
    print(a[i])

from os.path import split

#split method val= input().strip().split()
a=123456789
sum=0
rem=0
while a!=0:
    rem=a%10
    a=a//10
    sum+=rem

print(sum)


#Digital Root=1+(num - 1)%9*if num > 0) -> formula fro sum of digits

import numpy as np
list=[1,2,3]
a=np.array(list)
print(type (a))

arr.sort()
   print(sum(arr[:4]),sum(arr[:1]))

#finsinf second largest number in a array
def secondlarge(arr):
    arr.sort()
    num=arr[len(arr)-2]
    return num

array=[4,5,2,8,1,11]
result=secondlarge(array)
print(result)

#triangle quest
n='5'
for i in range(1,5):
    print(i*n)
    #go through list


#write a program to print prime numbers present in a given array. arrray limits are [1,7,17,19,24,36,11,2,39]
#function -> to check prime -> return true or false ->check_prime(n)
#for i in range(n):
#    result=check_prime(arr[i])
#    if(result==True):


def primenumber(n):
    for i in range(1,n+1):
        count=0
    for j in range(1,i+1):
        if i%j == 0:
            count+=1
    if count==2:
        return True
    else:
        return False

array=[1,7,17,19,24,36,11,2,39]
for i in array:
    if primenumber(i)==True:
        print(i)
'''
arr=[2,7,11,15]
target=int(input("enter the target"))
for i in arr:
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print[i,j]
