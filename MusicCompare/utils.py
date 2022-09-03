'''
File: utils.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to create a series of
functions to be used in compare_music.py. read_file is used to 
pass in a .txt file and go through and format the song to be put into
a 3 part tuple. get_slices finds sequences of notes based on user
input and appends each sequence to a list. compare_sets find the jaccard
index between 2 sets. compare_melodies takes in 2 lists of notes and
turns them into sets then compares both.
Course: Fall CS 120
'''

from typing import Union


def read_file(file):
    '''This takes in a file and loops through each line
    and formats the line to be put into a list. Then takes
    info from the list and turns it into a 3 part tuple which
    is then appended to a list. file is a name of a text file 
    given from the user. A tuple list is returned.'''
    tuple_list = []
    file_list = file.readlines()
    stripped_list = []
    # loop goes through each line in
    # the file 
    for line in file_list:
        # if line is blank loop continues
        if line == '\n':
            continue
        else:
            # line is formatted and appended
            # to a list
            line = line.strip()
            if line[0] == '@':
                stripped_list.append(int(line[3:5]))
                stripped_list.append(line[6:len(line)])
            else:
                line = line.split()
                stripped_list.append(line)
    # loop goes through each part of the list
    # and turns elements into a 3 part tuple
    # which is then appended to a list and
    # returned
    for i in range(2,len(stripped_list),3):
        tuple_list.append(tuple([stripped_list[i-2],\
            stripped_list[i-1],stripped_list[i]]))

    return tuple_list


def get_slices (data, n):
    '''goes through data and appends each slice of 
    the data to a list then returns the list. Data is a
    list of notes and n is a integer given by the user.
    A list of slices from the data is returned'''
    slice_list = []
    for i in range(n,(len(data)+1)):
        slice_list.append(data[ (i - n) : i ])
    return slice_list

def compare_sets (a, b):
    '''intersects sets a and b and
    unions a and b as well. Then divides
    the length of the intersection by the 
    length of the union. a and b are both lists
    of notes. The a set should be the first song 
    in the file.'''
    numerator = a.intersection(b)
    denom = a.union(b)
    # incase denominator is 0
    if len(denom) == 0:
        jaccard = 0.0
        return jaccard

    jaccard = len(numerator) / len(denom)
    return jaccard

def compare_melodies (m1, m2, n):
    '''takes in 2 lists of notes and gets slices from 
    both lists and adds them into a set. Then compares
    both sets for similarity. m1 and m2 are a list of notes
    and n is a integer given by the user, a similarity number
    based on the jaccard index is returned'''
    first = get_slices(m1, n)
    second = get_slices(m2, n)
    first_set =set()
    second_set = set()
    # loops add each sequence to a set
    for section in first:
        first_set.add(tuple(section))
    for section in second:
        second_set.add(tuple(section))
    # sets are compared
    similarity = compare_sets(first_set, second_set)
    return similarity

