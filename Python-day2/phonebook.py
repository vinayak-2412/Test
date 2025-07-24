phonebook={
        'A':12345678,
        'B':234567,
        'C':3456789,

}
def display():
    print('1.Add contact\n2.Search contact\n3.Delete a contact\n4.List all contact')
def add_contacts():
    name=input('Enter contact name').strip()
    if name in phonebook:
        print('contact already exist')
    else:
        number=input('Enter the phonenumber').strip()
        phonebook[name]=number
        print(f'contact{name} successfully added')

def search_contact():
    name=input('Enter contact name').strip()
    if name in phonebook:
        print(f'{name}:{phonebook[name]}')
    else:
        print('no contact ')

def delete_contact():
    name=input('Enter contact name').strip()

    if name in phonebook:
        del phonebook[name]
        print(f'contact{name} successfully deleted')
    else:
        print('no contact ')
def list_contact(phonebook):
    if not phonebook:
        print('phonebook is empty')
    else:
        print('All contacts:')
        for name,number in phonebook.items():
            print(f'{name}:{number}')

# def main():
#     while True:
#         display()
#         choice=input('choose any option').strip()
#         if choice=='1':
#             add_contacts()
#         elif choice=='2':
#             search_contact()
#         elif choice=='3':
#             delete_contact()
#         elif choice=='4':
#             list_contact(phonebook)
#             break
#         else:
#             print('invalid choice')
#
#
#
#
# if __name__ == "__main__":
#     main()