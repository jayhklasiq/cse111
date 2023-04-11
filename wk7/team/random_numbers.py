import os
os.system('cls')
import random

def main():
    numbers_list = [16.2, 75.1, 52.3]
    print (numbers_list)
    
    append_random_numbers(numbers_list)
    print (numbers_list)
    
    append_random_numbers(numbers_list, 3)
    print(f"numbers {numbers_list}")
    
    
    
def append_random_numbers(numbers_list, quantity = 1):
    for _ in numbers_list(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)