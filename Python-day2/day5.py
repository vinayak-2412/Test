# c="H"
# n=5
# #upper cone
# for i in range(n):
#      print((i*c).rjust(n-1) + c + (i*c).ljust(n-1))
# #upper pillars
# for i in range(n):
#     print((n*c).center(n*2)+(n*c).center(n*6))
# #horizontal lines
# for i in range((n+1) // 2):
#     print((c*n*5).center(n*6))
# #lower pillars
# for i in range(n):
#     print((n*c).center(n*2)+(n*c).center(n*6))
# #lower cone
# for i in range(n):
#      print(((c*(n - i - 1)).rjust(n) + c +((c*(n - i - 1)).ljust(n))).rjust(n*6))
###########################################################################################################################
#find a string hackerrank
# def count_substring(string,sub_string):
#     count=0
#     for i in range(len(string)):
#         if string[i:(i+len(sub_string))]==sub_string:
#             count+=1
#     return count
#
# string=input().strip()
# sub_string=input().strip()
#
# count = count_substring(string,sub_string)
# print(count)
import random

#same question as above but we have to print the substring in a list
# def count_substring(string,sub_string):
#     list=[]
#     for i in range(len(string)):
#         if string[i:(i+len(sub_string))]==sub_string:
#             list.append(string[i:i+len(sub_string)])
#     return list
#
# string=input().strip()
# sub_string=input().strip()
#
# count = count_substring(string,sub_string)
# print(count)

#write a program ro check weather given number is armstrong number or not eg = 153,1634

# num=int(input('enter no:'))
# sum=0
# rem=0
# temp=num
# while temp>0:
#     rem=temp%10
#     temp=temp//10
#     sum+=rem**3
# if sum==num:
#     print(f'{num} is armstrong')
# else:
#     print('it  is not')


###############################################################################################################
#write a program to store student name ,science marks,maths mark of 4 students to store name and marks use differnt list
#write a program to print average marks of student based on entered name

# name=['ab','ac','ad','ae']
# m1=[24,22,50,23]
# m2=[50,43,33,45]
# ind=-1
# avg=0
# named=input().strip()
# for i in range(len(name)):
#     if i==named:
#       ind=i
#     # print(avg)
#
# avg=(m1[ind]+m2[ind])//2
# print(avg)

#write a program to compare adjacent elements present in a list if 2 adjacent elements r same move that 1 element to resultant list and print unique element list which is containing all the uniquely entered values
#present in a input list
# l1=['a@gmail.com','b@gmail.com','a@gmail.com','c@gmail.com']
# r=[]
# for i in l1:
#     if i not in r:
#         r.append(i)
# print(r)

#write a program to find targeted element in a given list

# l1=['a@gmail.com','b@gmail.com','a@gmail.com','c@gmail.com','g@gmail.com']
# c=-1
# target='j@gmail.com'
# for i in range(len(l1)):
#         if target==l1[i]:
#             c=i
# print(c)
#another method
# l1=['a@gmail.com','b@gmail.com','a@gmail.com','c@gmail.com']
# r='c@gmail.com'
# if r in l1:
#     print(l1.index(r))
# else:
#     print('-1')
# import random
# print('NUMBER MISSING GAME')
# num = random.randint(1,10)
#
# while True:
#
#     number=int(input())
#     if num - number == 0:
#         print('congrats')
#         break
#     elif num-number >= 2:
#         print('HOT')
#         print('\U0001F525')
#     elif num - number <=2:
#         print('COLD','\U0001F9CA')
#         print()

#write a program to display count of given number in a list
#list=[7,49,7,11,6,41,7,1,101]
# list=['7','49','7','11','6','41','7','1','101']
# count=0
# target='7'
# for i in list:
#     for j in target:
#         if j==i:
#             count+=1
# print(count)
#another method
# list=['7','49','7','11','6','41','7','1','101']
# target='7'
# count=list.count(target)
# print(count)

# s='ABCDC'
# n=3
# pallindrom=[]
#
# def check_palindrom(s1):
#     return s1==s1[::-1]
#
# for i in range(0,len(s) -n +1):
#     substr=s[i:i+n]
#     if check_palindrom(substr):
#         pallindrom.append(substr)
# print('pallindromic substrings of length',n,'are',pallindrom)

########################################################################################################
#write a python program using function that calculates and returns the total prize of a item including tax
#scenario this program works for small shop where the user enters the prize of an item and we have list of tax amount bydeafault
#llis1t=['3%','5%','7%']
#items=['books','pen','mobile']
# list1=['3%','5%','7%']
# items=['books','pen','mobile']
# combined=list(zip(list1,items))
# print(combined)
#
# for i,j in zip(list1,items):
#     print(i,j)
#
#
#
# #basics on
#
# formatting
# set and list




