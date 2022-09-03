'''
File: music_compare.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to take in the functions from 
utils.py and find the similarties from a text file filled with songs and
notes. Then the program finds which songs are most similar based
on the Jaccard Index and prints out thier melodies and the 
sets of notes in each.
Course: Fall CS 120
'''
import utils

filename = input('file:')
n = int(input('n:'))

# function read_file turns each song
# into a 3 part tuple and then appends
# all the tuples to a list which is
# the_tuples
the_tuples = utils.read_file(open(filename))


# prints out each song name and a link
# to where the info was gotten from
# and then it also prints the notes
print('--- SONG LIST ---')
for song in the_tuples:
    print(f'id={song[0]} info="{song[1]}" notes={song[2]}')

print()

# this section prints out the Jaccard Index
# of each song compared to the first song
print(f'--- COMPARISONS ---')
first_compar = the_tuples[0]
first_skip = True
similar_list = []
# outer loop goes through each song tuple
for h in range(len(the_tuples)):
    # this first if skips the first
    # tuple song because that is what
    # first_compar is
    if first_skip == True:
        first_skip = False
        continue
    # this loop iterates through each part of
    # the tuple
    for j in range(3):
        if type(the_tuples[h][j]) == type([1,2,3]):
            # takes the list of notes from the tuple and 
            # first _compar and compares their melodies
            similar = utils.compare_melodies(first_compar[2],\
                 the_tuples[h][j], n)
            similar_list.append(similar)
            # prints out the similarity number
            # that compare_melodies returned
            print(f'id_a={first_compar[0]} id_b={the_tuples[h][j-2]}\
                 similarity={similar}')

print()

print(f'--- RESULT ---')
print(f'Most similar songs:')
print(f' {first_compar[1]}')

max_value = max(similar_list)
most_similar = ''
# this loop goes through each similarity value
# and find the index of the of the max value
# then goes into the tuple list and prints out
# the names of the songs and the id numbers
for i in range(len(similar_list)):
    if similar_list[i] == max_value:
        most_similar = the_tuples[i+1]
        print(most_similar[1])
        print()
        print(f' ids: {first_compar[0]}')
        print(f' ids: {most_similar[0]}')
        break
print()
print(f'Melodies:')
# loop prints out the notes of the first song
# in the file
for i in range(len(first_compar[2])):
    if i == (len(first_compar[2]) - 1):
        print(first_compar[2][i],end = '\n')
        break
    print(first_compar[2][i], end = ' ')
# loop prints out the notes of the song most 
# similar to the first song
for i in range(len(most_similar[2])):
    if i == (len(most_similar[2]) - 1):
        print(most_similar[2][i],end = '\n')
        break
    print(most_similar[2][i], end = ' ')

print()
# here both the first song and the most similar
# song are passed into get slices to get all the 
# slices into a list
first = utils.get_slices(first_compar[2],n)
second = utils.get_slices(most_similar[2],n)
first_set =set()
second_set = set()

# these 2 loops go through each slice list
# returned by get_slices and append them to a set
for section in first:
    first_set.add(tuple(section))
for section in second:
    second_set.add(tuple(section))

print('Set 1')
# this loop goes through the set of the
# notes for the first song and prints
# out each sequence of notes
for sect in sorted(first_set):
    for i in range(len(sect)):
        if i == (len(sect) - 1):
            print(sect[i],end = '\n')
            break
        print(sect[i],end = ' ')

print('Set 2')
# this loop goes through the set of the
# notes for the most similar song and prints
# out each sequence of notes
for sect in sorted(second_set):
    for i in range(len(sect)):
        if i == (len(sect) - 1):
            print(sect[i],end = '\n')
            break
        print(sect[i],end = ' ')





