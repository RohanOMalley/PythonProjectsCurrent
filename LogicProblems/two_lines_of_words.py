'''
File: two_lines_of_words.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to take in two lines of 
input and print out a series of facts about the inputs. These include:
the length of all the words combined, the combined words in a list,
the words in a sorted list, then lastly each word prints out with its
pair from the other list.
Course: Fall CS 120
'''

first = input()
second = input()
# split the inputs into lists
first = first.split()
second = second.split()
# the lists themselves
print('The first line was:',first)
print('The second line was:',second)
print()
combo = len(first) + len(second)
first_len = len(first)
second_len=len(second)
# The combo number printout
print('The combination of both lines had',combo,'words.')
combo_list = first + second
# The combo list printout
print('The combined set of words was:', combo_list)
print()
# The sorted list printout
print('After sorting, the words were:',sorted(combo_list))

# if statements to determine what the length will be
# for how many pairs will be printed out
if len(first) > len(second):
    length_to_print = len(second)
elif len(first) < len(second):
    length_to_print =len(first)
elif len(first) == len(second):
    length_to_print = len(first)

# the loop to printout the pairs
print('Pairs:')
for i in range(length_to_print):
    print(str(i)+':', first[i],',',second[i])