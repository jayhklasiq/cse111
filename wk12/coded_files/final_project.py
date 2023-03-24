import os
os.system('cls')
import csv

def main():
    print('Welcome to MoRewa!')
    prompt = (input('Would you like to log in or sign up? '))
    
    USERNAME = 0
    PASSWORD = 1
    
    login_data = sys_data('wk12\coded_files\username.csv', USERNAME)
    
    if prompt.lower() == 'login':
        print('Please type in your details below:')
        username = input('Username: ')
        if username in login_data:
            password = input('Password: ')
    


def sys_data(filename, key_column_index):
    login_detail = {}
    
    with open(filename, 'rt') as cvs_file:
        reader = csv.reader(cvs_file)
        next(reader)
        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                login_detail[key] = row
                             
    return login_detail            
            
    
    
if __name__ == '__main__':
    main()