import datetime
import os
import random
import sys

import writelog
import videoprompt

sys.path.append(os.path.abspath('/home/timcherne/PythonProjects/Education_Program/'))

def division_problem(results_directory, numerator_max_value, denominator_max_value, videos, show_hints):
  videoprompt.print_video_message(videos, show_hints)
  # num1 = random.randint(max(1, min_value), max(1, max_value))
  # num2 = random.randint(max(1, min_value), max(1, max_value))
  num1 = random.randint(1, numerator_max_value)
  num2 = random.randint(numerator_max_value, denominator_max_value)
  correct = None
  print('First give the answer, then the remainder')
  prompt = ' '.join([str(max(num1, num2)), '/', str(min(num1,num2)), '= '])
  while True:
    reply = input(prompt).strip()
    if not reply.isdigit():
      print('Sorry, ' + str(reply) + ' is not a number.' )
      continue
    else:
      reply = int(reply)
      reply_remainder = int(input('remainder = '))
      answer = int(max(num1, num2) / min(num1, num2))
      answer_remainder = max(num1, num2)%min(num1,num2)
      if reply == answer and reply_remainder == answer_remainder:
        print('Correct!')
        correct = True
      else:
        print('Incorrect:')
        print('\tThe correct answer is', prompt, answer, ' remainder = ', answer_remainder)
        correct = False
      log_entry = ','.join(['division', prompt, str(reply), str(answer), str(correct)])
      writelog.log_writer(results_directory, log_entry)
      print('\n')
      return correct
