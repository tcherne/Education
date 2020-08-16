#!/usr/bin/python
import argparse
import datetime
import importlib
import json
import os
import random
import sys

import numpy as np
import pandas as pd

import addition
import decimalplace
import division
import fraction
import greaterless
import maketens
import multiplication
import placevalue
import skipcount
import subtraction

sys.path.append(os.path.abspath('/home/timcherne/PythonProjects/Education_Program/'))

CONFIG = '/home/timcherne/PythonProjects/Education_Program/config'

def read_config(name):
  with open(CONFIG, 'r') as json_file:
    config_text = json.load(json_file)
    config = json.loads(config_text)
  return config[name]

def call_python_file(path):
  call(['python3', '{}'.format(path)])

def get_arg_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', '--name', help='childs name', required=True)
  return parser

def generate_problems(name, config):
  print('-----------------------------------------------------')
  question_types = []
  for qt in config['questions']:
    question_types.append(qt)
  kind = random.choice(question_types)
  print('kind:', kind)

  if kind == 'addition':
    min_value = config['questions']['addition']['min']
    max_value = config['questions']['addition']['max']
    result = addition.addition_problem(config['results_directory'], int(min_value), int(max_value))
  elif kind == 'subtraction':
    min_value = config['questions']['subtraction']['min']
    max_value = config['questions']['subtraction']['max']
    result = subtraction.subtraction_problem(config['results_directory'], int(min_value), int(max_value))
  elif kind == 'multiplication':
    min_value = config['questions']['multiplication']['min']
    max_value = config['questions']['multiplication']['max']
    result = multiplication.multiplication_problem(config['results_directory'], random.randint(min_value, max_value), random.randint(min_value, max_value))
  elif kind == 'division':
    min_value = config['questions']['division']['min']
    max_value = config['questions']['division']['max']
    result = division.division_problem(config['results_directory'], min_value, max_value)
  elif kind == 'fraction':
    min_value = config['questions']['fraction']['min']
    max_value = config['questions']['fraction']['max']
    result = fraction.fraction_problem(config['results_directory'], min_value, max_value)
  elif kind == 'skipcount':
    by_values = config['questions']['skipcount']['by_values']
    result = skipcount.skip_count_problem(config['results_directory'], by_values)
  elif kind == 'maketens':
    result = maketens.make_tens_problem(config['results_directory'])
  elif kind == 'place_value':
    min_value = config['questions']['place_value']['min']
    max_value = config['questions']['place_value']['max']
    result = placevalue.place_value_problem(config['results_directory'], min_value, max_value)
  elif kind == 'decimal':
    digits = config['questions']['decimal']['digits']
    result = decimalplace.decimal_problem(config['results_directory'], digits)
  elif kind == 'greaterthan_lessthan':
    min_value = config['questions']['greaterthan_lessthan']['min']
    max_value = config['questions']['greaterthan_lessthan']['max']
    result = greaterless.gle_problem(config['results_directory'], min_value, max_value)
  return result

def comparator(num1, num2):
  if num1>num2:
    return 1
  elif num1<num2:
    return 2
  else:
    return 0

def main(args):
  print('Preparing test for', args.name)
  config = read_config(args.name)
  correct_count = 0
  for i in range(int(config['number_of_questions'])):
    print('Problem ', str(i + 1), ':')
    result = generate_problems(args.name, config)
    correct_count = correct_count + result
  print('Your score was ', correct_count, ' correct out of ', i + 1, ' problems.  Or ', "{:.0%}".format(correct_count/(i+1)))

if __name__ == "__main__":
  main(get_arg_parser().parse_args())
