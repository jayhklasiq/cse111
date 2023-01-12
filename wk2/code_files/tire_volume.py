import os
os.system('cls')
import math
from datetime import datetime

print('This program collects data to help you calculate the volume of space in a tire.')
print('Enter the width of the tire in mm')
tire_width = int(input('do not exceed 205mm: '))
print('Enter the aspect ratio of the tire')
tire_ratio = int(input('do not exceed 60: '))
print('Enter the diameter of the wheel in inches')
wheel_diameter = int(input('do not exceed 15 inches: '))

volume = math.pi * (tire_width ** 2) * tire_ratio * (tire_width * tire_ratio + 2540 * wheel_diameter) 
volume = volume / 10000000000
print (f'The approximate volume is {volume:.2f} liters')
print()

buying_a_tire = input('Would you like to buy tires with the dimension you entered? (YES or NO)')

if buying_a_tire.upper() == 'YES':
  phone_number = input('Kindly type in your phone number: ')
  print('Thank you, your tire will be delivered by our dispatch upon calling you.')
elif buying_a_tire.upper() == 'NO':
  print('Thank you for using TIRE VOLUE!')  
      




#get the day of the week from your computers operating system
todays_date = datetime.now()

with open('volume.txt', 'at') as volume_files:
  print(f'{todays_date:%Y-%m-%d}, {tire_width}, {tire_ratio}, {wheel_diameter}, {volume:.2f}', file = volume_files)
  print(f'{phone_number} would like to buy a tire. Please call her for delivery.', file = volume_files)
  