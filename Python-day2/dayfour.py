import random
from random import randint

# s='ABCDEFGHIJK'
# res=''
#
# for i in range(0,len(s),max):
#     res=s[i:i+max]
#     print(res)
# another method
# text=textwrap.fill(string,max_width)
# return ''.join(text)

#write a program to print the given string is palindrome or not
# def palindrome(string):
#     if string==string[::-1]:
#         print("it is palindrome")
#     else:
#         print("it is not palindrome")
#
# string='teacher'
# palindrome(string)

# s='121$,mom,121l'
# cleaned=''.join(a.lower() for a in s if a.isalpha())
# print(cleaned)
# if cleaned==cleaned[::-1]:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")
 #write a program to check weather given strings r example of anagram or not
# s1=input('Enter1:')
# s2=input('Enter2:')
# cleaned1=''.join(a.lower() for a in s1 if a.isalnum())
# cleaned2=''.join(b.lower() for b in s2 if b.isalnum())
# if (sorted(cleaned1)==sorted(cleaned2)):
#     print('anagram')
# else:
#     print ('not anagram')
############################################################################
#letter case permutation
# s='a1b1'
# res=['']
# for i in s:
#     if i.isalpha():
#         res=[j+i.lower() for j in res] + [j+i.upper() for j in res]
#     else:
#         res=[j + i for j in res]
#
# print(res)

#write a program to generate random password
#take 1 list which is containing 5 names
#generate a random number between 1000 to 9999 and display the output in the format of name then number
# names=['Aam','Bam','Cam','Dam','Eam']
# random_name=random.choice(names)
# random_number=random.randint(1000,9999)
# print(f'generated pass is:{random_name}{random_number}')

# n='4'
# for i in range(4,0,-1):
#     print(i*n)
#     n=str(int(n)-1)
#


# def print_h_pattern(height):
#     for row in range(height):
#         for col in range(height):
#             if col == 0 or col == height - 1 or row == height // 2:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print()
#
# # Example usage
# print_h_pattern(7)
#
# str="H"
# n=5
# for i in range(n):
#      print((i*str).rjust(n-1) + str + (i*str).ljust(n-1))
#
# for i in range(n+1):
#     print((n*str).center(n*2)+ (n*str).center(n*6))
#
# for i in range((n+1) // 2):
#     print((str*n*5).center(n*6))
#
# for i in range(n + 1):
#     print((str*n).center(n*2) + (str*n).center(n*6))
#
# # Bottom Cone
# for i in range(n):
#     print(((str*(n - i - 1)).rjust(n) + str + (str*(n - i - 1)).ljust(n)).rjust(n*6))
#
#
#
