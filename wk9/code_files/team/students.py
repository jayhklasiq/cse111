import os
os.system('cls')
import csv


def main():
    I_NUMBER = 0
    STUDENT_NAME = 1
    student_dictionary = read_dictionary('wk9\code_files\\team\students.csv', I_NUMBER)
     
    request_number = (input('What is your NINE digit I-Number: '))
    
    if not request_number.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(request_number) < 9:
            print("Invalid I-Number: too few digits")
        elif len(request_number) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if request_number not in student_dictionary:
                print("No such student")
            else:
                # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
                value = student_dictionary[request_number]
                name = value[STUDENT_NAME]

                # Print the student name.
                print(name)      

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        
        for row_list in reader:
            if len(row_list) != 0:
                key = int(row_list[key_column_index])
                dictionary[key] = row_list        
    return dictionary            

if __name__ == '__main__':
    main()