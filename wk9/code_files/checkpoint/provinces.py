import os
os.system('cls')

def main():
    #Open the provinces.txt file for reading.
    province_list = []
    with open('wk9\code_files\checkpoint\provinces.txt', 'rt') as province_file:
        #Read the contents of the file into a list where each 
        # line of text in the file is stored in a separate element
        # in the list.
        for line in province_file:
            province_list = line.strip()
            print (province_list)
    
if __name__ == '__main__':
    main()
                