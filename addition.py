import datetime
import os
import random
import sys

import writelog
import videoprompt

sys.path.append(os.path.abspath('/home/timcherne/PythonProjects/Education_Program/'))

def addition_problem(results_directory, min_value, max_value, videos, show_hints):
  videoprompt.print_video_message(videos, show_hints)
  num1 = random.randint(min_value, max_value)
  num2 = random.randint(min_value, max_value)
  correct = None
  prompt = ' '.join([str(num1), '+', str(num2), '= '])
  while True:
    reply = input(prompt).strip()
    if not reply.isdigit():
      print('Sorry, ' + str(reply) + ' is not a number.' )
      continue
    else:
      reply = int(reply)
      answer = num1 + num2
      if reply == answer:
        print('Correct!')
        correct = True
      else:
        print('Incorrect:')
        print('\tThe correct answer is', prompt, answer)
        correct = False
      log_entry = ','.join(['addition', prompt, str(reply), str(answer), str(correct)])
      writelog.log_writer(results_directory, log_entry)
      print('\n')
      return correct
