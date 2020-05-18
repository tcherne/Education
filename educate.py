import numpy as np
import pandas as pd
import os, argparse, datetime, random

def get_arg_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', '--child', help='childs name', required=True)
  parser.add_argument('-m', '--min', help='min value', default=0)
  parser.add_argument('-x', '--max', help='max value', default=30)
  parser.add_argument('-k', '--kind', help='add/sub/mult/div', nargs='+', required=True)
  parser.add_argument('-n', '--number_of_problems', help='number of problems', default=10)
  parser.add_argument('-r', '--results_file', help='path to the results folder', required=True)
  return parser

def generate_problem(args):
  kind = random.choice(args.kind)
  start = args.min
  stop = args.max

  if kind == 'add':
    addition(random.randint(start, stop), random.randint(start, stop))
  if kind == 'sub':
    subtraction(random.randint(start, stop), random.randint(start, stop))

def addition(num1, num2):
  prompt = ' '.join([str(num1), '+', str(num2), '= '])
  reply = int(input(prompt))
  answer = num1 + num2
  if reply == answer:
    print('Correct!')
  else:
    print('Incorrect:')
    print(prompt, answer)

def subtraction(num1, num2):
  prompt = ' '.join([str(max(num1, num2)), '-', str(min(num1,num2)), '= '])
  reply = int(input(prompt))
  answer = max(num1, num2) - min(num1, num2)
  if reply == answer:
    print('Correct!')
  else:
    print('Incorrect:')
    print('\tThe correct answer is', prompt, answer)

def main(args):
  print(args)
  for i in range(args.number_of_problems):
    generate_problem(args)

if __name__ == "__main__":
  main(get_arg_parser().parse_args())