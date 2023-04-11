import os
os.system('cls')
import csv
import random
from pprint import pprint

def main():
    #Index to determine key
    KEY_INDEX = 0
    
    login_data = sys_data("wk12\coded_files\prove\\username.csv", KEY_INDEX)
    #Indexes for the list in the value of the key in the dictionary.
    USERNAME = 0
    PASSWORDS = 1
    
    #call the number_list function
    phonebook = number_list('wk12\coded_files\prove\phone_numbers.txt')
    
    #Print a welcome message!
    print('Welcome to Password Retriever.')
    print('To retreive your password, please type your phone number to generate OTP:')
    
    #request phone number from user to verify if they already have an account.
    phone_number = input('Type Here: ')
    print()
    
    #call the get_otp function
    otp = get_otp(phonebook, phone_number)
    print(otp)
    print()
    
    verify_otp = input('Type in your generated OTP here: ')
    print()
    
    if verify_otp == otp:
        #get username from user who is trying to get their password back.
        username = input('Username: ')
        print()
        #check if the username is in the dictionary
        if username in login_data:
            #Retreive the username and password list
            value = login_data[username]
            #Get the usernamee and password from the list
            u_name = value[USERNAME]
            password = value[PASSWORDS]

            print(f'Your forgotten password is: {password}')
    else:
        print('Incorrect OTP. Please re-run the program and try again.')        
        
def number_list(filename):
    try:
        phonebook = []
        with open(filename, "rt") as text_file:
            for numbers in text_file:
                number_list = numbers.strip()

                phonebook.append(number_list)
        return phonebook        
    except FileNotFoundError as file_not_found:
        print(file_not_found)
        print(f'The filename {filename} cannot be found, '\
            'ensure the relative path is correct.')
        
def get_otp(phonebook, phone_number):
    #if phone number is found in the file above, then an otp is generated
    if phone_number in phonebook:
        otp_generator = ['0SHT5', '78DHY', '46D7D', '5H5IW', 'EON38', '3HBOD', 'WGI39']
        otp = random.choice(otp_generator)
    else:
        print ('This phone number does not belong to a registered account. ' \
            'Please check the number again and restart the program to ' \
                'retrieve your password.')    
    return otp

def sys_data(filename, key_index):
    try:
        login_detail = {}

        with open(filename, 'rt') as cvs_file:
            reader = csv.reader(cvs_file)
            next(reader)
            for row in reader:
                if len(row) != 0:
                    key = row[key_index]
                    login_detail[key] = row                          
        return login_detail
    
    except FileNotFoundError as file_not_found:
        print(file_not_found)
        print(f'The filename {filename} cannot be found,'\
            'ensure the relative path is correct.')            
            
if __name__ == '__main__':
    main()