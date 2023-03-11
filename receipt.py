import os
os.system('cls')
import csv
from datetime import datetime

def main():
    print()
    print(f"Klasiq Store")
    print()
    total_items = 0
    
    PROCUCT_KEY_INDEX = 0
    PRODUCT_NAME = 1
    PRODUCT_PRICE = 2
    products_dict = read_dictionary('products.csv', PROCUCT_KEY_INDEX)
    
    with open('request.csv') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        next(readCSV)
        for row_list in readCSV:
            prod_id = row_list[0]
            prod_quantity = int(row_list[1])
            
            if prod_id in products_dict:
                details = products_dict[prod_id]
                product_name = details[PRODUCT_NAME]
                product_price = float(details[PRODUCT_PRICE])
                print(f'{product_name}: {prod_quantity} @ {product_price}')

            

                
    print()    
    print(f'Number of Items: {total_items}')
    # print(f'Subtotal: {subtotal}')
    
    print()
    print('Thank you for shopping at the Klasiq Store.')
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%A %I:%M %p}")
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