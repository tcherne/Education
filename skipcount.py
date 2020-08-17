import datetime
import os
import random
import sys

import numpy as np
import pandas as pd

import writelog
import videoprompt
sys.path.append(os.path.abspath('/home/timcherne/PythonProjects/Education_Program/'))


def skip_count_problem(results_directory, by_values, videos):
  videoprompt.print_video_message(videos)
  correct = None
  by = int(random.choice(by_values))
  number_of_times = random.randint(3, 10)
  print ('Example Input for Skip Counting: 2 4 6')
  prompt = ''.join(['Skip count by ', str(by), 's.  Your first number will be ', str(by), ' and your last number will be ', str(by*number_of_times), ': '])
  reply = input(prompt).strip().split(' ')
  answer = np.arange(by, by*number_of_times + by, by)

  while True:
    if len(reply) != len(answer):
      print('Please enter ', str(number_of_times), ' numbers. You entered ', len(reply), ' numbers.')
      reply = input(prompt).split(' ')
    else:
      reply = [r for r in reply if r.isdigit()]
      if len(reply) == len(answer):
        check = pd.DataFrame({'reply':reply, 'answer':answer})
        check['reply'] = check['reply'].astype(int)
        check['answer'] = check['answer'].astype(int)
        check['difference'] = check['reply'] - check['answer']
        if check['difference'].max() == 0 and check['difference'].min() == 0:
          correct = True
          print('Correct!')
        else:
          correct = False
          print('Incorrect.')
      else:
        correct = False
        print('Incorrect. Seems some values were not numbers')

      print(''.join(['\tSkip counting by ', str(by), ' from ', str(by), ' to ', str(by*number_of_times), ' is the same as:']))
      addition_string = ''
      for n in np.arange(by, by*number_of_times + by, by):
        if n != by*number_of_times:
          addition_string = addition_string  + str(by)+' + '
        else:
          addition_string = addition_string  + str(by) + ' = ' + str(by*number_of_times)
      print('\t', addition_string)
      multiplication_string = ''
      multiplication_string = ''.join([str(by), ' * ', str(number_of_times), ' = ', str(by*number_of_times)])
      print('\t', multiplication_string)
      log_entry = ','.join(['skip_count', prompt, str(reply), str(answer), str(correct)])
      writelog.log_writer(results_directory, log_entry)
      print('\n')
      return correct
