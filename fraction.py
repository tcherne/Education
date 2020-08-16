import datetime
import os
import random
import sys
from fractions import Fraction

import writelog

sys.path.append(os.path.abspath('/home/timcherne/PythonProjects/Education_Program/'))

def comparator(num1, num2):
  if num1>num2:
    return 1
  elif num1<num2:
    return 2
  else:
    return 0

def fraction_problem(results_directory, min_value, max_value):
  num_1a = random.randint(1, max_value)
  num_1b = random.randint(1, max_value)
  num_2a = random.randint(1, max_value)
  num_2b = random.randint(1, max_value)

  num1 = Fraction(min(num_1a, num_1b), max(num_1a, num_1b))
  num2 = Fraction(min(num_2a, num_2b), max(num_2a, num_2b))

  print(num1, ':', num2)
  correct = None
  prompt = ' '.join(['Which fraction is bigger (1 or 2)? \n1: ', str(num1), '\n2: ', str(num2), '\n'])
  while True:
    reply = input(prompt).strip()
    if not reply.isdigit() or int(reply) > 2:
      print('Sorry, ' + str(reply) + ' is not an option pick 1 or 2, if they are equal enter 0.' )
      continue
    else:
      print('the reply is : ', reply)
      reply = int(reply)
      answer = comparator(num1, num2)
      if reply == answer:
        print('Correct!')
        correct = True
      else:
        print('Incorrect:')
        text_answer = ''
        if answer == 0:
          text_answer = 'they are equal (enter 0)'
        elif answer == 1:
          text_answer = ' '.join([str(num1), '>', str(num2), '(enter 1)'])
        elif answer == 2:
          text_answer = ' '.join([str(num1), '<', str(num2), '(enter 2)'])
        print('\tThe correct answer is ', text_answer)
        correct = False
      log_entry = ','.join(['fraction', prompt.replace('\n', ' '), str(reply), str(answer), str(correct)])
      writelog.log_writer(results_directory, log_entry)
      print('\n')
      return correct
