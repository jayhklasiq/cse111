import os
os.system('cls')
# Import the csv module so that it can be used
# to read from the accidents.csv file.
import csv


# Column numbers from the accidents.csv file.
YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9


def main():
    # Prompt the user for a filename and open that text file.
    try:
        filename = input("Name of file that contains NHTSA data: ")
        with open(filename, "rt") as text_file:

            # Prompt the user for a percentage.
            perc_reduc = get_float("Percent reduction of texting while driving [0, 100]: ", 0, 100)

            print()
            print(f"With a {perc_reduc}% reduction in using a cell",
                "phone while driving, approximately the",
                "following number of injuries and deaths",
                "would have been prevented in the USA.", sep="\n")
            print()
            print("Year, Injuries, Deaths")

            # Use the csv module to create a reader
            # object that will read from the opened file.
            reader = csv.reader(text_file)

            # The first line of the CSV file contains column headings
            # and not a student's I-Number and name, so this statement
            # skips the first line of the CSV file.
            next(reader)

            # Process each row in the CSV file.
            for row in reader:
                year = row[YEAR_COLUMN]

                # Call the estimate_reduction function.
                injur, fatal = estimate_reduction(
                        row, PHONE_COLUMN, perc_reduc)

                # Print the estimated reductions
                # in injuries and fatalities.
                print(year, injur, fatal, sep=", ")
                
    except FileNotFoundError as not_found_error:
        #if the user enters a wrong filename, then this code
        # activate a filename error message
        print()
        print(not_found_error)
        print(f'The file {filename} does not exist.')
        print('Please run the program again and enter '\
            ' the name of an existing file.')
    
    except PermissionError as permisssion_error:
        #If a filename that is not to be executed by this appplication is inputed,
        # the code below will trigger a permission error message
        print()
        print(permisssion_error)
        print(f'{filename} cannot be opened because you do not have permission' \
            'to read it.')
        print('Please run the program again, and enter a file name you are' \
            'allowed to read.')
    
    except ValueError as value_error:
        #This code activates when you input an incorrect integer when asked from the user
        print()
        print(value_error)
        print('Seems like you missed the numbers up.')
        print('Please run the program again, and enter a correct value')
     
        
def get_float(question, min, max):
    number = None
    while number == None:
        try:
            number = float(input(question))
            if number < 0:
                print()
                print(f'The {number} you entered is a negative number')
                print('Please run the program again, and enter a correct value')
                number = None
            elif number > 100:
                print()
                print(f'The {number} you entered is over 100.')
                print('Please run the program again, and enter a correct value')
                number = None
        except ValueError as value_err:
            print(value_err)
    return number        

def estimate_reduction(row, behavior_key, perc_reduc):
    """Estimate and return the number of injuries and deaths that
    would not have occurred on U.S. roads and highways if drivers
    had reduced a dangerous behavior by a given percentage.

    Parameters
        row: a CSV row of data from the U.S. National Highway Traffic
            Safety Administration (NHTSA)
        behavior_key: heading from the CSV file for the dangerous
            behavior that drivers could reduce
        perc_reduc: percent that drivers could reduce a dangerous
            behavior
    Return: The number of injuries and deaths that may have been
        prevented
    """
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal


# If this file was executed like this:
# > python accidents.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
