#!/usr/bin/python

import numpy as np
import pandas as pd
import os, argparse, datetime, random
from fractions import Fraction

#Example Commandline
#python3 educate.py -k skip -c Tim -r "/home/timcherne/PythonProjects/Education_Program/test"

def get_arg_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', '--child', help='childs name', required=True)
  parser.add_argument('-m', '--min', help='min value for problems', default=0)
  parser.add_argument('-x', '--max', help='max value for problems', default=30)
  parser.add_argument('-k', '--kind', help='add/sub/mult/div/frac/skip', nargs='+', required=True)
  parser.add_argument('-n', '--number_of_problems', help='number of problems', default=10)
  parser.add_argument('-r', '--results_directory', help='path to the results folder', required=True)
  return parser

def write_log(args, line):
  date = datetime.datetime.now().strftime('%Y%m%d')
  directory = '/'.join([args.results_directory, args.child])
  filename = '/'.join([args.results_directory, args.child, date])
  if not os.path.exists(directory):
    os.makedirs(directory)
  with open(filename, "a") as file:
    file.writelines(line + '\n')

def generate_problem(args):
  print('\n-----------------------------------------------------')
  kind = random.choice(args.kind)
  start = int(args.min)
  stop = int(args.max)
  if kind == 'add':
    addition(args, random.randint(start, stop), random.randint(start, stop))
  elif kind == 'sub':
    subtraction(args, random.randint(start, stop), random.randint(start, stop))
  elif kind == 'mult':
    multiplication(args, random.randint(start, stop), random.randint(start, stop))
  elif kind == 'div':
    division(args, random.randint(max(1, start), max(1, stop)), random.randint(max(1, start), max(1, stop)))
  elif kind == 'frac':
    frac1 = Fraction(random.randint(max(1, start), max(1, stop)), random.randint(max(1, start), max(1, stop)))
    frac2 = Fraction(random.randint(max(1, start), max(1, stop)), random.randint(max(1, start), max(1, stop)))
    fraction(args, frac1, frac2)
  elif kind == 'skip':
    skip_count(args)


def addition(args, num1, num2):
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
      write_log(args, log_entry)
      print('\n')
      #needed to exit the valid loop
      break

def subtraction(args, num1, num2):
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
      write_log(args, log_entry)
      print('\n')
      #needed to exit the valid loop
      break

def multiplication(args, num1, num2):
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
      write_log(args, log_entry)
      print('\n')
      #needed to exit the valid loop
      break

def division(args, num1, num2):
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
      write_log(args, log_entry)
      print('\n')
      #needed to exit the valid loop
      break

def fraction(args, num1, num2):
  correct = None
  prompt = ' '.join(['Which fraction is bigger (1 or 2)? \n1: ', str(num1), '\n2: ', str(num2), '\n'])
  while True:
    reply = input(prompt).strip()
    if not reply.isdigit() and reply:
      print('Sorry, ' + str(reply) + ' is not an option pick 1 or 2, if they are equal enter 0.' )
      continue
    else:
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
      log_entry = ','.join(['fraction', prompt, str(reply), str(answer), str(correct)])
      write_log(args, log_entry)
      print('\n')
      #needed to exit the valid loop
      break

def skip_count(args):
  correct = None
  by = random.randint(1, 10)
  number_of_times = random.randint(3, 10)
  prompt = ''.join(['Skip count by ', str(by), 's.  Your first number will be ', str(by), ' and your last number will be ', str(by*number_of_times), '.\nExample Input: 2 4 6\n:'])
  reply = input(prompt).split(' ')
  answer = np.arange(by, by*number_of_times + by, by)

  while True:
    if len(reply) != len(answer):
      print('Please enter ', str(number_of_times), ' numbers. You entered ', len(reply), ' numbers.')
      reply = input(prompt).split(' ')
    else:
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
      write_log(args, log_entry)
      print('\n')
      return correct

def comparator(num1, num2):
  if num1>num2:
    return 1
  elif num1<num2:
    return 2
  else:
    return 0

def main(args):
  print(args)
  for i in range(int(args.number_of_problems)):
    generate_problem(args)

if __name__ == "__main__":
  main(get_arg_parser().parse_args())
