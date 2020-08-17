import datetime
import os
import random
import sys

import writelog
import videoprompt

sys.path.append(os.path.abspath('/home/timcherne/PythonProjects/Education_Program/'))

def multiplication_problem(results_directory, max_one, max_two, videos):
  videoprompt.print_video_message(videos)
  num1 = random.randint(0, max_one)
  num2 = random.randint(0, max_two)
  correct = None
  prompt = ' '.join([str(num1), '*', str(num2), '= '])
  while True:
    reply = input(prompt).strip()
    if not reply.isdigit():
      print('Sorry, ' + str(reply) + ' is not a number.' )
      continue
    else:
      reply = int(reply)
      answer = num1 * num2
      if reply == answer:
        print('Correct!')
        correct = True
      else:
        print('Incorrect:')
        print('\tThe correct answer is', prompt, answer)
        correct = False
      log_entry = ','.join(['multiplication', prompt, str(reply), str(answer), str(correct)])
      writelog.log_writer(results_directory, log_entry)
      print('\n')
      return correct
