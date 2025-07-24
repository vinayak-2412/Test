# strs = ["flower","flow","flight"]
# prefix=strs[0]
# for strings in strs[1:]:
#     while not strings.startswith(prefix):
#         prefix=prefix[:-1]
#         if not prefix:
#             print("")
# print(prefix)
# def function(*paramter):
#     print(paramter)
#
# function(1,3,4,5,6,7)
#########################################################################################################################
#write a program to display maximum number among 3 given integer use function to do the calculation or the logic note
#inputs r integer not a list
# def maxnumber(a,b,c):
#     return max(a,b,c)
# a=2
# b=1
# c=6
# print(maxnumber(a,b,c))
#anoter method
# def maxnumber(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
#
# a=4
# b=7
# c=12
# print(maxnumber(a,b,c))
#write a  function if the nummber is power of 2
# def powernum(a):
#         while(a>1):
#             if(a%2==0):
#                 a=a//2
#             else:
#                 return False
#         return True
#
# a=8
# print(powernum(a))
from math import factorial


# write a program to check given number is perfect square root or not

# def perfectsquare(n):
#     for i in range(1,100):
#         if n==i*i:
#             return True
#         else:
#             return False
#
# n=9
# print(perfectsquare(n))
#example of recursion
# def greet(n):
#     print(n)
#     greet(n-1)
# greet(2)

#write a program to print even numbers present in a range of 1 to 10 without using looping control statements

# def evennumber(n):
#     if( n<=10) :
#         if (n%2==0):
#             print(n)
#         evennumber(n+1)
#
# evennumber(1)

#write a program to display list of a numbers present in a range of 1 to 100 which are completely divisible by 3 and 5

# def check(n):
#     if n<=100:
#         if n%3==0 and n%5==0:
#             print(n)
#         check(n+1)
#
# check(1)
#Factorial of numbers
# def factnum(n):
#     if n<0:
#         return
#     elif n==1:
#         return 1
#     else:
#         print(factorial(n))
#     factnum(n-1)
# print(factnum(10)

#write a program to move 2 disks to source to destination with given conditions
#1.only one disk we can move at a time
#2.we should not place larger disk above the smaller one
# take 3 disks and 3 pin to complete the task
# def towergame(n,a,b,c):
#davis staircase question


