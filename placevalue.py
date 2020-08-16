import datetime
import os
import random
import sys

import writelog
import videoprompt

sys.path.append(os.path.abspath('/home/timcherne/PythonProjects/Education_Program/'))

def place_value_problem(results_directory, min_value, max_value, videos):
  videoprompt.print_video_message(videos)
  correct = None
  number = random.randint(100, 999)
  place = random.choice(['ones', 'tens', 'hundreds'])
  answer = 0
  if place == 'hundreds':
    answer = int(str(number)[0])
  elif place == 'tens':
    answer = int(str(number)[1])
  elif place == 'ones':
    answer = int(str(number)[2])
  prompt = ' '.join(['What is the value of the', place, 'place in', str(number), '? '])
  while True:
    reply = input(prompt).strip()
    if not reply.isdigit():
      print('Sorry, ' + str(reply) + ' is not a number.' )
      continue
    else:
      reply = int(reply)
      if reply == int(answer):
        print('Correct!')
        correct = True
      else:
        print('Incorrect:')
        print('\tThe correct answer is', answer)
        correct = False
      log_entry = ','.join(['place_value', prompt, str(reply), str(answer), str(correct)])
      writelog.log_writer(results_directory, log_entry)
      print('\n')
      return correct
