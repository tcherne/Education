import datetime
import os
import random
import sys

import writelog

sys.path.append(os.path.abspath('/home/timcherne/PythonProjects/Education_Program/'))

def comparator(num1, num2):
  if num1>num2:
    return 1
  elif num1<num2:
    return 2
  else:
    return 0

def gle_problem(results_directory, min_value, max_value):
  num1 = random.randint(min_value, max_value)
  num2 = random.randint(min_value, max_value)

  correct = None
  equal = ' '.join([str(num1), '=', str(num2)])
  gt = ' '.join([str(num1), '>', str(num2)])
  lt = ' '.join([str(num1), '<', str(num2)])

  prompt = ' '.join(['Which answer is correct? \n0: ', equal, '\n1: ', gt, '\n2: ', lt, '\n'])
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
          text_answer = ' '.join([str(num1), '>', str(num2), '(enter 1)', '\n\t', str(num1), 'is bigger than', str(num2)])
        elif answer == 2:
          text_answer = ' '.join([str(num1), '<', str(num2), '(enter 2)', '\n\t', str(num1), 'is smaller than', str(num2)])
        print('\tThe correct answer is ', text_answer)
        correct = False
      log_entry = ','.join(['decimal', prompt.replace('\n', ' '), str(reply), str(answer), str(correct)])
      writelog.log_writer(results_directory, log_entry)
      print('\n')
      return correct
