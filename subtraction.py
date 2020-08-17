import datetime
import os
import random
import sys

import writelog
import videoprompt

sys.path.append(os.path.abspath('/home/timcherne/PythonProjects/Education_Program/'))

def subtraction_problem(results_directory, min_value, max_value, videos):
  videoprompt.print_video_message(videos)
  num1 = random.randint(min_value, max_value)
  num2 = random.randint(min_value, max_value)
  correct = None
  prompt = ' '.join([str(max(num1, num2)), '-', str(min(num1,num2)), '= '])
  while True:
    reply = input(prompt).strip()
    if not reply.isdigit():
      print('Sorry, ' + str(reply) + ' is not a number.' )
      continue
    else:
      reply = int(reply)
      answer = max(num1, num2) - min(num1, num2)
      if reply == answer:
        print('Correct!')
        correct = True
      else:
        print('Incorrect:')
        print('\tThe correct answer is', prompt, answer)
        correct = False
      log_entry = ','.join(['subtraction', prompt, str(reply), str(answer), str(correct)])
      writelog.log_writer(results_directory, log_entry)
      # write_log(args, log_entry)
      print('\n')
      return correct
