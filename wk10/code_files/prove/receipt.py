import os
os.system('cls')
import csv
from datetime import datetime

def main():
    try:
        print()
        print(f"Klasiq Store")
        print()
        total_items = 0
        subtotal = 0

        PROCUCT_KEY_INDEX = 0
        PRODUCT_NAME = 1
        PRODUCT_PRICE = 2
        products_dict = read_dictionary('wk10\code_files\products.csv', PROCUCT_KEY_INDEX)

        with open('wk10\code_files\Request.csv') as csv_file:
            #because python is noticing the "\r" which is a carriage return,
            # the file is popping up as an error.
            #Possible fix is to either change the file name, or ensure 
            #you dont need to refernce the file from another folder
            #So, all I did was change the lower case r to an uppercase.
            readCSV = csv.reader(csv_file, delimiter=',')
            next(readCSV)
            for row_list in readCSV:
                prod_id = row_list[0]
                prod_quantity = int(row_list[1])
                total_items += prod_quantity
                
                if prod_id in products_dict:
                    details = products_dict[prod_id]
                    product_name = details[PRODUCT_NAME]
                    product_price = float(details[PRODUCT_PRICE])
                    print(f'{product_name}: {prod_quantity} @ {product_price}')
                item_prices = prod_quantity * product_price
                subtotal += item_prices
                sales_tax = 0.06 * subtotal
                total_cost = subtotal + sales_tax
        print()    
        print(f'Number of Items: {total_items}')
        print(f'Subtotal: {subtotal:1f}')
        print(f'Sales tax: {sales_tax:.2f}')
        print(f'Total: {total_cost:.2f}')
        print()
        
        if "D083" in prod_id:
            print(f'Your coupon code is: IAMBLESSED!')    
        print('Thank you for shopping at the Klasiq Store.')
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a, %b %d, %Y. %X}")
    except KeyError as key_error:
        print()
        print(key_error)
        print(f'There seem to be a wrong key input, please check'\
            'your key value input and try again.')
    except FileNotFoundError as file_errror:
        print()
        print(file_errror)
        print(f'The file on line 19 cannot be found, please'\
            'reference the correct file and try again.')    
        
        
def read_dictionary(filename, key_column_index):
    try:
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
    except (FileNotFoundError) as file_not_found:
        print()
        print(file_not_found)
        print(f'The file {filename} is not found')
        print('Please check line 16 and make sure your.'\
            'file name is correct.')               
    return dict         

   
if __name__ == '__main__':
    main()