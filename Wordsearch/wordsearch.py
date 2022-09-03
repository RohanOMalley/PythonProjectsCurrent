###
### Author: Rohan O'Malley
### Course: Csc 110
### Description: this program will go through a dictionary file that the user inputs and go through
### a puzzle file that the user also inputs. The program then finds the words in that dictionary that
### are in the puzzle, at the end of the program the words found and their locations in the grid
### will also be printed out.

def forwards_backwards (words_file):
    '''this function takes in the word file from the user
    and strips and splits each line of \n and puts each into a dictionary
    then that dictionary is returned, the word_file parameter is the input
    from the user in main'''
    # opens file and turns it into a list
    words_file = open (words_file,'r')
    words_list = words_file.readlines()
    words_dict = {}
    # loop runs through words_file and splits and strips and puts each word
    # a dictionary
    for words in words_list:
        split_word = words.strip('\n').split(' : ')
        words_dict[split_word[0]] = split_word[1]
    return words_dict


def horizontal (words_dict, grid_file):
    '''this function is used for looking for words horizontally
    in the puzzle grid. This function opens the grid file and puts it into
    a list, then loops through and formats each line to match the dictionary
    format. Then, calls the search_within_line function and then returns the lists
    of the locations of the words, what words were found, the words_dict parameter is
    what was returned from the forwards_backwards function, the grid_file parameter
    is from the user in main'''
    # opens grid file and turns it into a list
    grid_file = open (grid_file, 'r')
    grid_list = grid_file.readlines()
    # lists are used to keep track of words and locations
    # found in the lines of puzzle
    horizontal_list = []
    found_list = []
    index_list = []
    row_list = []
    i = 0
    y_position = 1

    #loop goes through and formats lines from puzzle grid into
    #lines that match the format of the dictionary, then searchs through each line to seed
    #if any words exist in that line.

    for line in grid_list:
        line = line.strip('\n')
        space_string =''
        new_string = ''
        for letter in line:
            if letter == ' ':
                letter += space_string
            else:
                new_string += letter.lower()
        horizontal_list.append(new_string)
        answer= search_within_line(words_dict,horizontal_list[i],found_list,index_list,y_position,row_list)
        i += 1
        y_position+= 1
    return(row_list,index_list,found_list)




def search_within_line (words_dict,horiz,found_list,index_list,y_position,row_list):
    '''This function goes through each line from the grid file and finds if
    words in the dictionary are apparent in the line. If they are, they get appended to
    a found list and lists that correalate with their location on by row and the index
    in that string, row_list, index_list, and found_list track what words have been found
    and what row and index they were found at. words_dict is from forwards_backwards, horiz
    is from the horizontal_list at i from horizontal function'''

    # loop goes throught the forward and backward words in dictionary to see if they
    # match with the line
    for forward, backward in words_dict.items():
        start = 0
        forward_length = len(forward)
        # this loop runs through the line to create the sliding window effect
        # to analyze if the word is in the line
        while forward_length <= len(horiz):
            if horiz[start:forward_length] == forward:
                # this appends the positon of the word and the word itself
                # to their lists
                found_list.append(forward)
                index_list.append(str(start+1))
                row_list.append(str(y_position))
                return found_list,index_list,row_list

            elif horiz[start:forward_length] == backward:
                # this appends the positon of the word and the word itself
                # to their lists
                found_list.append(forward)
                index_list.append(str(forward_length))
                row_list.append(str(y_position))
                return found_list,index_list,row_list
            start += 1
            forward_length += 1





def vertical (words_dict, grid_file):
    grid_file = open (grid_file, 'r')
    grid_list = grid_file.readlines()
    vertical_list = []
    found_list = []
    index_list = []
    row_list = []
    i = 0
    while i <= len(grid_list[0])-1:
        line = grid_list[i].strip('\n')
        vertical_string = ''
        j = 0
        while j <= len(line):
            first_character = grid_list[j][i]
            vertical_string += first_character
            j += 1
        vertical_list.append(vertical_string)
        search_within_line(words_dict,vertical_list[i],found_list,index_list,i,row_list)
        i += 1
    return(row_list,index_list,found_list)





def main():
    # inputs from user
    dict_input = input('Enter word file:\n')
    puzzle_file = input ('Enter puzzle file:\n')
    mode = input('Enter puzzle mode:\n')
    # puts the word file into a dictionary
    words_dict = forwards_backwards(dict_input)
    # if horizontal mode, functions will run
    if mode == 'h':
        row,index,found = horizontal(words_dict, puzzle_file)
    if mode == 'v':
        row,index,found = vertical(words_dict,puzzle_file)
    # loop goes through the lists returned from horizontal and prints out what
    # words were found and where
    for i in range(len(row)):
        print(found[i]+' found at ['+row[i]+', '+index[i]+']')


main()