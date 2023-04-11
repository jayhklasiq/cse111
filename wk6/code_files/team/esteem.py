import os
os.system('cls')

def main():
  print(' This program is an implementation of the Rosenberg\n\
  Self-Esteem Scale. This program will show you ten\n\
  statements that you could possibly apply to yourself.\n\
  Please rate how much you agree with each of the\n\
  statements by responding with one of these four letters:\n')
  
  print(' D means you strongly disagree with the statement. \n\
  d means you disagree with the statement. \n\
  a means you agree with the statement. \n\
  A means you strongly agree with the statement.')
  #assesment questions asked
  point = 0   
  point += positive_question(
    "1. I feel that I am a person of worth, at least on an"
    "equal plane with others.")
  point += positive_question(
    "2. I feel that I have a number of good qualities.")
  point += negative_question(
    "3. All in all, I am inclined to feel that I am a failure.")
  point += positive_question(
    "4. I am able to do things as well as most other people.")
  point += negative_question(
    "5. I feel I do not have much to be proud of.")
  point += positive_question(
    "6. I take a positive attitude toward myself.")
  point += positive_question(
    "7. On the whole, I am satisfied with myself.")
  point += negative_question(
    "8. I wish I could have more respect for myself.")
  point += negative_question(
    "9. I certainly feel useless at times.")
  point += negative_question(
    "10. At times I think I am no good at all.")
  
  
  print(f"Your point is {point}.")
  print("A point below 15 may indicate problematic low self-esteem.")


def positive_question(response):
  print (response)
  answer = input(' Enter D, d, a, or A: ')
  point = 0
  if answer == 'D':
    point = 0
  elif answer == 'd':
    point = 1
  elif answer == 'a':
    point = 2
  elif answer == 'A':
    point = 3
           
  return point
 
def negative_question(response):
  print (response)
  answer = input(' Enter D, d, a, or A: ')
  point = 0
  if answer == 'D':
    point = 3
  elif answer == 'd':
    point = 2
  elif answer == 'a':
    point = 1
  elif answer == 'A':
    point = 0
  
  return point  
    
if __name__ == "__main__":
    main()  
