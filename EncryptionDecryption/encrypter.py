###
###
### Author: Rohan O'Malley
### Course: Csc 110
### Description:
###
###

import random

def encrypter(file_name):
    input_file = open(file_name, 'r')
    i = 1
    input_list = []
    index_list = []
    for lines in input_file:
        lines = lines.strip('\n')
        input_list.append(lines)
        index_list.append(i)
        i += 1
    for index in range(len(input_list)*5):
        hold_line = ''
        hold_num = 0
        random_1 = random.randint(0,len(input_list)-1)
        random_2 = random.randint(0,len(input_list)-1)
        hold_line = input_list[random_1]
        hold_num = index_list[random_1]
        input_list[random_1] = input_list[random_2]
        input_list[random_2] = hold_line
        index_list[random_1] = index_list[random_2]
        index_list[random_2] = hold_num
    input_file.close()

    index_file = open('index.txt','w')
    encrypted_file = open('encrypted.txt','w')
    for i in range(len(input_list)):
        index_file.write(str(index_list[i])+'\n')
        encrypted_file.write(input_list[i]+'\n')
    encrypted_file.close()
    index_file.close()



def main ():
    random.seed(125)
    file_name = input('Enter a name of a text file to encrypt:\n ')
    encrypter (file_name)

main ()