'''
File: sequence_len.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to take multiple inputs and 
figure out if theyare in descending or ascending order. 
If the order goes out of place then the program stops.
Then prints out how mnay numbers passed before 
the sequence went out of order.
Course: Fall CS 120
'''

ascending_count = 0
descending_count = 0
duplicate_count = 0

# loop goes through each input and sorts into a list
# turns into an int as well
while True: 
    sequence = input()
    split_seq = sequence.split(' ')
    number_list = []

    # loop turns strings into ints and
    # appends to the number list

    for number in split_seq:
        if number.isnumeric() == True:
            number_list.append(int(number))
    
    i = 0
    # this loop checks if the numbers ever go out of order
    # if it does it breaks out of the loop
    while i < len(number_list)-1:
        if number_list[i] < number_list[i+1]:
            ascending_count += 1
            i += 1
            if descending_count > 1:
                False
        elif number_list[i] > number_list[i+1]:
            descending_count += 1
            i += 1
            if ascending_count > 1:
                False
        else:
            i += 1
            duplicate_count += 1
    if ascending_count > 1 and descending_count == 1:
        break
    elif descending_count > 1 and ascending_count == 1:
        break

# final print statements that show how many numbers
# passed before they went out of order
if ascending_count > descending_count:
    new_count = (ascending_count + duplicate_count)
    print(new_count+1)
elif descending_count > ascending_count:
    new_count = (descending_count + duplicate_count)
    print(new_count+1)

    
    