import os
os.system('cls')


def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    print()
    #Add code to reverse and print fruit_list
    print('Let us switch this up, shall we?')
    fruit_list.reverse()
    print(f'Reserved: {fruit_list}')
    #Add code to append "orange" to the end of 
    # fruit_list and print the list.
    print()
    fruit_list.append('orange')
    print(f'Appended: {fruit_list}')
    #Add code to find where "apple" is located in fruit_list 
    # and insert "cherry" 
    # before "apple" in the list and print the list.
    print()
    fruit_list[1] = 'cherry'
    print(f'Inserted: {fruit_list}')
    #Add code to remove "banana" from fruit_list 
    # and print the list.
    print()
    fruit_list.remove('banana')
    print(f'Removed: {fruit_list}')
    #Add code to pop the last element from fruit_list 
    # and print the popped element and the list.
    print()
    fruit_list.pop(3)
    print(f'Popped: {fruit_list}')
    #Add code to sort and print fruit_list.
    print()
    sorted_list = sorted(fruit_list)
    print(f'Sorted: {sorted_list}')
    #Add code to clear and print fruit_list.    
    fruit_list.clear()
    print(f'Cleared: {fruit_list}')
if __name__ == '__main__':
    main()    