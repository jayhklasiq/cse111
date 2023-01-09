import math
import os
os.system('cls')

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

print('Hello there!')
age = int(input('How old are you? '))
#subtract your age from 220
max_heart_rate_per_min = 220 - age
#you should keep your heart rate between 65% and 85% of your heart’s maximum rate
heart_rate_while_excercising = (f'{(0.65 * max_heart_rate_per_min):.0f} and {(0.85 * max_heart_rate_per_min):.0f}')
print(f'When you exercise to strengthen your heart, you should keep your heart rate between {heart_rate_while_excercising} beats per minute.')