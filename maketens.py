import datetime
import os
import random
import sys

import writelog

sys.path.append(os.path.abspath('/home/timcherne/PythonProjects/Education_Program/'))

def make_tens_problem(results_directory):
  correct = None
  number = random.randint(0, 9)
  prompt = ' '.join(['How many do we need to add to', str(number), 'to make 10? '])
  while True:
    reply = input(prompt).strip()
    if not reply.isdigit():
      print('Sorry, ' + str(reply) + ' is not a number.' )
      continue
    else:
      reply = int(reply)
      answer = 10 - number
      if reply == answer:
        print('Correct!')
        correct = True
      else:
        print('Incorrect:')
        print('\tThe correct answer is', answer)
        correct = False
      print('\t', number, ' + ', str(10-number), ' = 10')
      print('\t10 - ', number, ' = ', str(10-number))
      log_entry = ','.join(['make_tens', prompt, str(reply), str(answer), str(correct)])
      writelog.log_writer(results_directory, log_entry)
      print('\n')
      return correct
