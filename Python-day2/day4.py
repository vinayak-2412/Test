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

def palindrome(string):
    special_char = '!@#$%^()_+-[]{}|;:,.<>'    if string==string[::-1]:
        print("it is palindrome")
    else:
        print("it is not palindrome")
