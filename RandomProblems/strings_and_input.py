'''
File: strings_and_input.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to take an input
 and print out the length of input,the second character,
 the first 10 characters,
 the last 5 characters, entire string but in
uppercase, classify the first character, if 
the first character is in 'qwerty or 'ioup' print
either or. Also will print if it first char
 is a digit or a letter.
Course: Fall CS 120
'''

user_input = input('input string: ')

print(len(user_input))
print(user_input[1])

if len(user_input) <= 10:
    print(user_input)
elif len(user_input) > 10:
    print(user_input[0:10])

print(user_input[-5:len(user_input)])

print(user_input.upper())


first_char = user_input[0]
qwerty = ('q','w','e','r','t','y')
uiop = ('u','i','o','p')

if first_char.lower() in qwerty:
    print('QWERTY')

elif first_char in uiop:
    print('UIOP')

elif first_char.isnumeric() == False:
    print('LETTER')

elif first_char.isnumeric() == True:
    print('DIGIT')

else:
    print('OTHER')

first_num = int(input())

second_num = int(input())

mult = first_num * second_num
print(mult)