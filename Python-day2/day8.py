
# def revstr(s, start, end):
#     s = s.lower()
#
#
#     if start >= end:
#         return True
#
#
#     if s[start] != s[end]:
#         return False
#     return revstr(s, start + 1, end - 1)
# s = input("Enter a string: ")
#
# print(revstr(s, 0, len(s) - 1))

# write a program to find nth fibonacci series with the help of recursion
# def fib(n):
#
#     if n<0:
#         return "Not defined"
#     elif n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# s=int(input("enter "))
# print(fib(s))

#write a program to display list of fibonacci numbers
# def fib(n):
#
#
#     if n<0:
#         return "Not defined"
#     elif n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#
#         return fib(n-1)+fib(n-2)
#
# def main(val):
#     li=[]
#     for i in range(val):
#         li.append(fib(i))
#     return li
#
#
# val=int(input("enter "))
# print(main(val))

# write a program to display armstrong numbers in a given range

# write a tracing of 4 stairs having n values with 1 2 3 display the number of permutations that we have to reach staircase
memo={}
# def tracing(n):
    # if n<0:
    #     return 0
    # elif n==0:
    #     return 1
    # elif n<=2:
    #     return n
    # if n in memo:
    #     memo[n]
    # memo[n]=tracing(n-1)+tracing(n-2)+tracing(n-3)
    # return memo[n]
#
# s1=1,True,6,7
# s2=set(s1)
# print(s2)
# write a program to demonstrate set methods which should contain add remove discard pop len methods and display the values
#initial set = 1,11,17,true,21,21,1,true
#add 7 to the set
#remove 1 from the set
#discard true

# s=1,11,17,True,21,21,1,True
# s1=set(s)
# s1.add(7)
# s1.remove(1)
# s1.discard(True)
# print(s1)

s={2,4,5}
print(s.clear())
print(s.remove(2))
# del s