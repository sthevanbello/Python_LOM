# number = input('Enter a number: ')
# if (number.isdigit()):
#     number = int(number)
#     if (number % 2 == 0):
#         print(f'The number {number} is even')
#     else:
#         print(f'The number {number} is odd')
# else:
#     print('Not is a integer number')

name = input("Enter your First Name: ")
length_name = len(name)

if (length_name <= 4):
    print(f'The name {name} is very short')
elif (length_name > 4 and length_name <= 6):
    print(f'The name {name} is normal')
else:
    print(f'{name}, your name is very long')
