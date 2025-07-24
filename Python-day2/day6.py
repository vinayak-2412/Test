#Tuple
# t1=(1,)
# t2=1,3,2,2,4
# #check type
# print(type(t2))
# print(type(t1))
# #tuple methods
# print(len(t2))
# print(min(t2))
# print(max(t2))
# print(t2.count(2))
# print(t2.index(4))
# #conversion
# l1=list(t2)
# print(type(l1))

#######################################################################################################################
# write a program to create insert , delete and display tuple values where input is 1,4,6,9,2 add element as  10 remove element 2
#display tuple elements
#
# tup=(1,4,6,9,2)
# l1=list(tup)
# l1.append(10)
# l1.pop(4)
# l1=tuple(tup)
# print(l1)

#membership operation(print with for)
# for i in t2:
#     print(i)
# dictionary
# d={
#     'name':'abc',
#
#     'id':122334,
# }
# # print(d)
# # for i,h in zip(d.keys(),d.values()):
# #     print(i,h)
# #write a program to declare dictionary with 3 key and value pair and print the dictionary
# print(type(d.keys()))
# print(type(d.values()))
# print(d.pop('id'))
# print(type(d.popitem()))
# # #print((d.append({'email':'a@gmail.com'}))) #append works with list from list we can convert
# print((d.update({'email':'a@gmail.com'})))
# print(d)

# write a program to display many of a restaurant with a key and value pair where keys r items available in a restaurant
# and values are prices of the respective items take the order from end user and generate bill or invoice and display it
# print('Here is our menu')
# items={
#         'dal':100,
#         'breads':26,
#         'juice':10,
#         'paneer gravy':160,
# }
#
# for item,price in items.items():
#     print(f'{item}:{price}')
# order=input("please enter the order")
# quantity=int(input('enter the quantity'))
# if order in items:
#     total_price=items[order]*quantity
#     print(f'you total bill is{total_price}')


# write a program to maintain a phone book with the name and phone number declare 4 methods such as:
#add new contact
#remove existing contact
#search the contact with the help of contact name adn display

###########################################################################################################################

# write  a program to check weather user entered number is circular prime or not
#ex:13 and 31 both r prime
#
# def prime_check(n):
#     for i in range(1, n + 1):
#         count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False


# def reverse(n):
#     while True:
#
#
#         rem=n%10
#         rev=n//10
#         rev=rev+rem*10
#         return rev
#
# n=13
# print(reverse(n))

# def main():
#     a=int(input('enter the number'))
#     count=0
#     if prime_check((a))==True:
#         count+=1
#         b=reverse(a)
#     if prime_check(b)==True:
#         count+=1
#     if count==2:
#
#
#         print('it is a circular prime number')
#     else:
#         print('it is not')