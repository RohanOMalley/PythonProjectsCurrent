###
### Author: Rohan O'Malley
### Course: Csc 110
### Description: This program looks into csv files and puts all the numbers that do not begin with
### 0 into a list, then it loops through and finds the counts of what number that the number in
### the list begins with. Then it prints out a plot with all of the percentages of all occurences
### of the first digit in the numbers. Then at the end of the plot it will either print out, that the
### number set follows benford's law or that it doesn't follow it.

def read_function (file_name):
    '''This function takes in the file name from the user and opens the file
    and reads it into a list. Then loops through the lines and strips and splits
    each line on the comma. Then loops through that line to find all the numbers that
    do not begin with a 0 and append them to num_list. Then returns that list.'''
    file = open (file_name,'r')
    file = file.readlines()
    num_list =[]

    # loop goes through each line in the list and strips
    # and splits to be used in the nested loop
    for i in range(0,len(file)):
        line = file[i].strip('\n').split(',')
        # loop goes through each section of the line and checks if does not
        # start with 0 and if the first and last characters are numeric
        # then turns string into a float and appends to list
        for i in range(0,len(line)):
            if line[i][0].isnumeric() and line[i][-1].isnumeric()and line[i][0] != '0':
                num_list.append(float(line[i]))

    return num_list



def count_occurences (num_list):
    '''This function goes through the num_list and loops through the
    first digit of each number and then adds to the counts
    dictionary depending on what number comes first. Then return the counts dictionary'''
    counts = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

    # loop goes through each number in list and turns it into
    # a string to look at the last character and turns it into
    # an int and uses that as the key for the dictionary and increases
    # the count
    for num in num_list:
        key = str(num)
        key = int(key[0])
        counts[key] += 1
    return counts

def print_plot (counts,num_list):
    '''This function prints out the plot for how many the beginning digits
    occured in the numbers. It gets the percent of that occurence compared to the
    total length of how many number were in the list. Then loops through the percents
    again to find if the percent fits the requirements of Benford's Law. Compares counts
    of the benford counts and prints out if the data does or does not follow Benford's Law.'''

    # loop prints out each horizontal bar graph of
    # according to the counts in the dictionary
    for i in range(1,10):
        print(str(i)+' | '+'#'* (int((counts[i]/len(num_list))*100)))

    # list with all the percents that follow benford's law
    percent_list = [30,17,12,9,7,6,5,5,4]
    benford_count = 0
    non_benford = 0

    # loop goes through each count and finds the percent then compares
    # it to the percent in the percent list
    for i in range(len(percent_list)):
        digit = (int((counts[i+1]/len(num_list))*100))
        if digit >= (percent_list[i]-5) and digit <= (percent_list[i]+10):
            benford_count += 1
        else:
            non_benford += 1
    print(' ')
    # the conditions for if the numbers follow
    # benford's law
    if non_benford > 0:
        print("Does not follow Benford's Law")
    elif benford_count == 9:
        print("Follows Benford's Law")



def main ():
    file_name = input('Data file name:\n')
    num_list = read_function(file_name)
    counts = count_occurences(num_list)
    print(' ')
    print_plot(counts, num_list)


main ()