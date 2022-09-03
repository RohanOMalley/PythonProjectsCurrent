###
###
### Author: Rohan O'Malley
### Course: Csc 110
### Description:
###

def decrypter (encrypted_file,index_file):
    encrypted_file = open(encrypted_file, 'r')
    index_file = open(index_file, 'r')
    decrypted_file = open('decrypted.txt','w')
    encrypted_list = []
    index_list = []

    index_list = index_file.readlines()
    encrypted_list = encrypted_file.readlines()

    decrypted_list = ['']*len(encrypted_list)

    for i in range(len(index_list)):
        #index_list = (index_list[i-1].strip('\n'))
        #encrypted_list = (encrypted_list[i]-1).strip('\n')
        index = int(index_list[i])-1
        decrypted_list[index] = encrypted_list[i]

    for lines in decrypted_list:
        decrypted_file.write(lines)

    encrypted_file.close()
    decrypted_file.close()
    index_file.close()




def main():
    encrypted_file = input('Enter the name of an encrypted text file:\n')
    index_file = input('Enter the name of the encryption index file:\n')
    decrypter(encrypted_file,index_file)


main()