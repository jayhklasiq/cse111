import os
os.system('cls')
import math


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