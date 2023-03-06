import os
os.system('cls')
import csv


def main():
    PROCUCT_KEY_INDEX = 0
    PRODUCT_NAME = 1
    PRODUCT_PRICE = 2
    products_dict = read_dictionary('wk9\code_files\products.csv', PROCUCT_KEY_INDEX)
    
    print (products_dict)
    

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
    dict = {}
    
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dict[key] = row_list
    return dict         


if __name__ == '__main__':
    main()