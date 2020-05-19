#!/usr/bin/python

import numpy as np
import pandas as pd
import os, argparse, datetime, random

#Example Commandline
#python3 educate.py -k add sub mult div spell -c Tim -r "/home/timcherne/PythonProjects/Education_Program/test"

def get_arg_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', '--child', help='childs name', required=True)
  parser.add_argument('-m', '--min', help='min value for problems', default=0)
  parser.add_argument('-x', '--max', help='max value for problems', default=30)
  parser.add_argument('-k', '--kind', help='add/sub/mult/div/spell', nargs='+', required=True)
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
  kind = random.choice(args.kind)
  start = args.min
  stop = args.max
  if kind == 'add':
    addition(args, random.randint(start, stop), random.randint(start, stop))
  elif kind == 'sub':
    subtraction(args, random.randint(start, stop), random.randint(start, stop))
  elif kind == 'mult':
    multiplication(args, random.randint(start, stop), random.randint(start, stop))
  elif kind == 'div':
    division(args, random.randint(start, stop), random.randint(start, stop))
  elif kind == 'spell':
    spelling()

def addition(args, num1, num2):
  correct = None
  prompt = ' '.join([str(num1), '+', str(num2), '= '])
  reply = int(input(prompt))
  answer = num1 + num2
  if reply == answer:
    print('Correct!')
    correct = True
  else:
    print('Incorrect:')
    print('\tThe correct answer is', prompt, answer)
    correct = False
  log_entry = ','.join([prompt, str(reply), str(answer), str(correct)])
  write_log(args, log_entry)
  print('\n')

def subtraction(args, num1, num2):
  correct = None
  prompt = ' '.join([str(max(num1, num2)), '-', str(min(num1,num2)), '= '])
  reply = int(input(prompt))
  answer = max(num1, num2) - min(num1, num2)
  if reply == answer:
    print('Correct!')
    correct = True
  else:
    print('Incorrect:')
    print('\tThe correct answer is', prompt, answer)
    correct = False
  log_entry = ','.join([prompt, str(reply), str(answer), str(correct)])
  write_log(args, log_entry)
  print('\n')

def multiplication(args, num1, num2):
  correct = None
  prompt = ' '.join([str(num1), '*', str(num2), '= '])
  reply = int(input(prompt))
  answer = num1 * num2
  if reply == answer:
    print('Correct!')
    correct = True
  else:
    print('Incorrect:')
    print('\tThe correct answer is', prompt, answer)
    correct = False
  log_entry = ','.join([prompt, str(reply), str(answer), str(correct)])
  write_log(args, log_entry)
  print('\n')

def division(args, num1, num2):
  correct = None
  print('First give the answer, then the remainder')
  prompt = ' '.join([str(max(num1, num2)), '/', str(min(num1,num2)), '= '])
  reply = int(input(prompt))
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
  log_entry = ','.join([prompt, str(reply), str(answer), str(correct)])
  write_log(args, log_entry)
  print('\n')

def spelling():
  print('your spelling is horrible.')
  print('\n')

def main(args):
  print(args)
  for i in range(int(args.number_of_problems)):
    generate_problem(args)

if __name__ == "__main__":
  main(get_arg_parser().parse_args())
