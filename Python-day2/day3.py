#string conversion methods
'''
a=('Hello World')
print(a)
a1=" hello"
print(a+a1)  #concatenation
print(a1 * 3)  # repetition
print(a.lower())#lower
print(a.upper())#upper
print(a.title())#first letter of string will become capital
print(a.swapcase())#swapcase
print(a.capitalize())

#searching and counting
s=('hello world')
print(s.find('d'))#finds where the letter is
print(s.count('o'))#counts the number of letter
print(s.index('o'))#tells the index of first occurrence
print(s.startswith('h'))#checks if string starts with 'h'
print(s.endswith('u'))#check if string ends with 'u'
# write a program to implement simple atm application and print the following options and perform user selected options
#1.deposit
#2.withdrawal
#3.balance check
#4.pin change

pin = 1234
balance=3000

def Deposit():
    global balance
    print('Enter your pin')
    entered_pin = int(input())
    if entered_pin == pin:
        print('Enter the amount to deposit')
        amount = int(input())
        if amount <= 0:
            print('Invalid amount')
        else:
            balance += amount
            print('Amount deposited successfully')
            print(f'Deposited amount: {amount}')
            print(f'Updated balance: {balance}')
    else:
        print('Invalid pin')


def Withdrawal():
    global balance
    print('Enter your pin')
    entered_pin = int(input())
    if entered_pin == pin:
        print('Enter the amount to withdraw')
        amount = int(input())
        if amount <= 0:
            print('Invalid amount')
        elif amount > balance:
            print('Insufficient balance')
        else:
            balance -= amount
            print('Amount withdrawn successfully')
            print(f'Withdrawal amount: {amount}')
            print(f'Updated balance: {balance}')
    else:
        print('Invalid pin')


# Example usage:
# Deposit(1000)

def validate_pin():
    entered_pin=int(input('Enter you PIN:'))
    if entered_pin==pin:
        return True
    else:
        print('Incorrect pin')
        return False


#display balance()
def Display_balance():
    global balance
    print('Enter your pin')
    entered_pin = int(input())
    if entered_pin == pin:
        print(balance)

#Display_balance()

#pin change
def Pin_change(val):
    global pin
    newpin=int(input('Enter the new pin'))
    newpin=pin

def main():

     while True:
         print('Welcome to the atm')
         print('1.Deposit\n2.Withdrawal\n3.Check balance\n4.pin change')
         sel=input()
         if sel=='1':
             Deposit()

         elif sel=='2':
             Withdrawal()

         elif sel=='3':
             Display_balance()

         else:
             Pin_change()

         break

main()

#split(separator)
#join(iterable)
#strip
#lstrip
#rstrip

s=("hello world")
s=s.split(" ")
s="&".join(s)
print (s)
'''
#password evaluation take the input as A123@a
# 1)check white space-> present remove
# 2)check alpha character-> yes
# 3)check digit character-> yes
# 4)check special character-> yes
# 5)check at least 1 lowercase character
# 6)check at least 1 uppercase character
def passeval():
    password='A123@a'
    a=False
    b=False
    c=False
    d=False

    if (any(i.islower() for i in password)):
                 a=True
    if (any(i.isupper() for i in password)):
                 b=True
    if (any(i.isalpha() for i in password)):
                 c=True
    if (any(i.isdigit() for i in password)):
                 d=True
    if (any(i.isspace() for i in password)):
                 password.strip()
    if a and b and c:
        print('strong password')
    else:
        print("weak password")

passeval()
# password=input('enter the password')
# password=password.replace(" ","")
# print(f"current password is {password}")
# special_char='!@#$%^()_+-[]{}|;:,.<>'
# up=any(i.isupper()for i in password)
# lower=any(i.islower()for i in password)
# digit=any(i.isdigit for i in password)
# alpha=any(i.isalpha() for i in password)
# special=any(i in special_char for i in password)
#
# if up and lower and special and digit and alpha:
#     print('strong password')
# else:
#     print('weak password')