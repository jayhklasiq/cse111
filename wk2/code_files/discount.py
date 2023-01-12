import os
os.system('cls')
from datetime import datetime

'''
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the stores slowest sales days. 
On Tuesday and Wednesday, if a customers subtotal is $50 or greater, the store will discount the customers subtotal by 10%.

Your program must not ask the user to enter the day of the week. 
Instead, it must get the day of the week from your computers operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. 
Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. 
Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.
'''

#get the day of the week from your computers operating system
todays_date = datetime.now()
day_ofthe_week = todays_date.weekday()

day_ofthe_week = 1
sales_subtotal = float(input('Please enter the subtotal: '))
#compute the total amount due by adding sales tax of 6% to the subtotal.
if day_ofthe_week == 1 or day_ofthe_week == 2 and sales_subtotal >= 50:
  discount = 0.1 * sales_subtotal
  print(f'Discount: {discount:.2f}')
  sales_subtotal = sales_subtotal - discount
  sales_tax = 0.06 * sales_subtotal
  print (f'Sales tax: {sales_tax:.2f}')
  total_amount_due = sales_subtotal + sales_tax
  print (f'Total: {total_amount_due:.2f}')
else:  
  sales_tax = 0.06 * sales_subtotal
  print (f'Sales tax: {sales_tax:.2f}')
  total_amount_due  = sales_subtotal + sales_tax
  print (f'Total: {total_amount_due:.2f}')


    
  
  


  


