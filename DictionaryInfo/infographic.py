###
### Author: Rohan O'Malley
### Course: Csc 110
### Description: This program goes through a text file, assembles the words into a dictionary,
### and finds what words occur most, which are capitalized and non-capitalized. Then it prints out
### a graphics module of a bar graph of what size words are most ocurring in
### the text file.

from graphics import graphics

def read_process (file_name):
    '''This function takes the file name from user and
    opens it in read mode and reads it into a list, then loops
    through and strips, splits and appends to a words list, then returns
    the words list to be used in main'''
    file = open (file_name,'r')
    file_list = file.readlines()
    words = []

    # loop goes through each line and strips and splits words
    # then appends to list
    for line in file_list:
        line = line.strip('\n')
        if len(line) <= 2:
            words.append(line)
        elif len(line) > 2:
            line = line.split()
            for word in line:
                words.append(word)
    return words


def count_words (words):
    '''This fucntion takes the words list and loops throughand append to
    the seen list if word has been seen, then adds it to a count dictionary
    to keep track of the apperances in the list. Then returns the count dictionary
    that has how many times each word was seen in the words list.'''
    # sets dictionaries for loops
    count_dict = {}
    max_count_dict = {}
    seen = []
    # loop is used to get the unique words from file
    for word in words:
        new_word = word.lower()
        if new_word not in seen:
            seen.append(new_word)
            if new_word not in count_dict:
                count_dict[word] = 1
            elif new_word in count_dict:
                count_dict[word] += 1
    # loop goes through and finds all the words in the file not just
    # the unique ones
    for word in words:
        if word not in max_count_dict:
            max_count_dict[word] = 1
        elif word in max_count_dict:
            max_count_dict[word] += 1
    return count_dict, max_count_dict


def count_dict_maker (count_dict,max_count_dict):
    '''This function runs through the count dictionary and finds what words
    have small, medium and large lengths, then keeps track of how many words
    fit those conditons, then returns each dictionary for the selected size'''
    size_dict = {'large':0,'medium':0,'small':0}
    small_dict = {}
    med_dict = {}
    large_dict = {}
    # loop goes through and increases the value for all the unique words
    # in the dictionary
    for key, value in count_dict.items():
        if len(key) >= 0 and len(key) <= 4:
            size_dict['small'] += value
        elif len(key) >= 5 and len(key) <= 7:
           size_dict['medium'] += value
        elif len(key) >= 8:
            size_dict['large'] += value
    # loop is used to find the total count of all the words in the file
    # by looking at the max_count_dict
    for key ,value in max_count_dict.items():
        if len(key) >= 0 and len(key) <= 4:
            small_dict[key] = value
        elif len(key) >= 5 and len(key) <= 7:
            med_dict[key] = value
        elif len(key) >= 8:
            large_dict[key] = value
    return size_dict,small_dict,med_dict,large_dict


def max_occur (small_dict,med_dict,large_dict):
    '''This function determines what occurs most in the file, it checks each size dictionary
    and appends the value and word that occurs most for each dictionary to a list
    that is returned at the end of the loop'''
    dict_list = [small_dict, med_dict, large_dict]
    max_occur_list = []
    # loop goes through each size dictionary in the list
    for dict_row in dict_list:
        num_list = []
        word_list = []
        # loop goes through and appends the keys and values to lists
        for key, value in dict_row.items():
            word_list.append(key)
            num_list.append(value)
        max_occur_word = word_list[0]
        max_occur_value = num_list[0]
        # loop finds the word that occurs the most in each size dictionary
        # and appends the word and how many times it occurs to a list
        for i in range(len(num_list)):
            if num_list[i] > max_occur_value:
                max_occur_value = num_list[i]
                max_occur_word = word_list[i]
        max_occur_list.append(max_occur_word)
        max_occur_list.append(max_occur_value)
    return max_occur_list

def count_capitals (words):
    '''This function loops through the words list to find how many capitals
    and non_capitals are in the file. It checks each line at the first index
    to check if the word it capitalized or not. And it will increse the counts
    respectivley, then those counts are returned in a dictionary'''
    cap_dict = {'cap':0,'non cap':0}
    # loop find how many words are capitalized and
    # how many are not capitalized
    for word in words:
        if len(word) > 0:
            if word[0].isupper():
                cap_dict['cap'] += 1
            elif word[0].islower():
                cap_dict['non cap'] += 1
    return cap_dict

def graphic_numbers (size_dict,cap_dict):
    '''This function goes through the size dictionary and capital dictionary
    and finds the numbers to divide each section of the graphics column by so it fits
    withn the canvas. Also, it loops through each dictionary to find the total counts
    of each number that are used to divide by 450'''
    total_count = 0
    cap_count = 0
    # loop find total count of unquie words
    for key in size_dict:
        total_count += size_dict[key]
    # loop find the total count of capitalized
    # and non-cap words in the file
    for key in cap_dict:
        cap_count += cap_dict[key]
    # these numbers are used to set the sections in the
    # right spots
    small =((450/total_count)*size_dict['small'])
    medium =((450/total_count)*size_dict['medium'])
    large =((450/total_count)*size_dict['large'])
    cap = ((450/cap_count)*cap_dict['cap'])
    non_cap = ((450/cap_count)*cap_dict['non cap'])
    return small,medium,large,cap,non_cap

def canvas_titles (gui,file_name,size_dict,max_occur_list):
    '''This function draws the title pieces on the canvas, it types out the
    name of the file, the background, the most used words from the max_occur
    list and the titles of each of the bars'''
    m_x = max_occur_list
    unique_count = 0
    # loop finds the unique count in the size dictionary
    for key in size_dict:
        unique_count += size_dict[key]
    # all the pieces for the titles on the canvas
    gui.rectangle(-10,-10,700,700,'gray')
    gui.text(25,10,file_name,'light blue',15)
    gui.text(25,40,'Total Unique Words:','white',12)
    gui.text(170,40,str(unique_count),'white',12)
    gui.text(25,65,'Most used words (s/m/l):','white',10)
    gui.text(176,65, m_x[0]+'('+str(m_x[1])+'x) '+m_x[2]+\
    '('+str(m_x[3])+'x) '+m_x[4]+'('+str(m_x[5])+'x) ','white',8)
    gui.text(25,90,'Word Lengths','white',15)
    gui.text(180,90,'Cap/Non-Cap','white',15)

def graphic_word_length_bar (gui,small,medium,large):
    '''This function draws the bar for the lengths of the words
   in the file, it takes in the values from the graphics_numbers function
   and uses them to make sure the sections match up on the canvas, Also
   prints out titles of sections'''
    gui.rectangle(25,120,125,small,'green')
    gui.rectangle(25,(120+small),125,medium,'red')
    gui.rectangle(25,(120+small+medium),125,large,'navy')
    gui.text(26,121,'small words','white',8)
    gui.text(26,(121+small),'medium words','white',8)
    gui.text(26,(121+small+medium),'large words','white',8)


def graphic_cap_bar (gui,cap,non_cap):
    '''This function draws the non_cap and capital bar on the canvas
    it takes the values from the graphics_numbers function and uses them
    to make sure the sections match up on the canvas, also prints out titles
    for the sections'''

    gui.rectangle(175,120,125,cap,'red')
    gui.rectangle(175,(120+cap),125,non_cap,'green')
    gui.text(175,121,'Capitalizied','white',8)
    gui.text(175,(121+cap),'Non-Capitalized','white',8)


def main ():
    gui = graphics (600,600,'Word Length')
    file_name = input('What file do you want to open?\n')
    words = read_process(file_name)
    count_dict,max_count_dict = count_words(words)
    size_dict,small_dict, med_dict, large_dict = count_dict_maker(count_dict,max_count_dict)
    max_occur_list = max_occur(small_dict,med_dict,large_dict)
    cap_dict = count_capitals(words)
    small,medium,large,cap,non_cap = graphic_numbers(size_dict,cap_dict)
    canvas_titles (gui,file_name,size_dict,max_occur_list)
    graphic_word_length_bar(gui,small,medium,large)
    graphic_cap_bar(gui,cap,non_cap)

main()