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

import settings
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
import reward

CONFIG = '/home/timcherne/PythonProjects/Education_Program/'

# python3 educate.py -n Gavin -r /home/timcherne/Education_Results -c /home/timcherne/Git_Repo/Education/

def read_config(name, config_path):
  with open('/'.join([config_path, 'config']), 'r') as json_file:
    config_text = json.load(json_file)
    config = json.loads(config_text)
  return config[name]

def call_python_file(path):
  call(['python3', '{}'.format(path)])

def get_arg_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', '--name', help='childs name', required=True)
  parser.add_argument('-c', '--config_path', default=CONFIG)
  parser.add_argument('-r', '--results_path', required=True)
  return parser

def generate_problems(name, config):
  print('-----------------------------------------------------')
  question_types = []
  for qt in config['questions']:
    question_types.append(qt)
  kind = random.choice(question_types)

  if kind == 'addition':
    min_value = config['questions']['addition']['min']
    max_value = config['questions']['addition']['max']
    videos = config['questions']['addition']['videos']
    result = addition.addition_problem(config['results_directory'], int(min_value), int(max_value), videos, config['show_hints'])
  elif kind == 'subtraction':
    min_value = config['questions']['subtraction']['min']
    max_value = config['questions']['subtraction']['max']
    videos = config['questions']['subtraction']['videos']
    result = subtraction.subtraction_problem(config['results_directory'], int(min_value), int(max_value), videos, config['show_hints'])
  elif kind == 'multiplication':
    min_value = config['questions']['multiplication']['max_one']
    max_value = config['questions']['multiplication']['max_two']
    videos = config['questions']['multiplication']['videos']
    result = multiplication.multiplication_problem(config['results_directory'], int(min_value), int(max_value), videos, config['show_hints'])
  elif kind == 'division':
    min_value = config['questions']['division']['num_max']
    max_value = config['questions']['division']['denom_max']
    videos = config['questions']['division']['videos']
    result = division.division_problem(config['results_directory'], int(min_value), int(max_value), videos, config['show_hints'])
  elif kind == 'fraction':
    min_value = config['questions']['fraction']['min']
    max_value = config['questions']['fraction']['max']
    videos = config['questions']['fraction']['videos']
    result = fraction.fraction_problem(config['results_directory'], int(min_value), int(max_value), videos, config['show_hints'])
  elif kind == 'skipcount':
    by_values = config['questions']['skipcount']['by_values']
    videos = config['questions']['skipcount']['videos']
    result = skipcount.skip_count_problem(config['results_directory'], by_values, videos, config['show_hints'])
  elif kind == 'maketens':
    result = maketens.make_tens_problem(config['results_directory'])
  elif kind == 'place_value':
    min_value = config['questions']['place_value']['min']
    max_value = config['questions']['place_value']['max']
    videos = config['questions']['place_value']['videos']
    result = placevalue.place_value_problem(config['results_directory'], int(min_value), int(max_value), videos, config['show_hints'])
  elif kind == 'decimal':
    digits = config['questions']['decimal']['digits']
    videos = config['questions']['decimal']['videos']
    result = decimalplace.decimal_problem(config['results_directory'], int(digits), videos, config['show_hints'])
  elif kind == 'greaterthan_lessthan':
    min_value = config['questions']['greaterthan_lessthan']['min']
    max_value = config['questions']['greaterthan_lessthan']['max']
    videos = config['questions']['greaterthan_lessthan']['videos']
    result = greaterless.gle_problem(config['results_directory'], int(min_value), int(max_value), videos, config['show_hints'])
  return result

def comparator(num1, num2):
  if num1>num2:
    return 1
  elif num1<num2:
    return 2
  else:
    return 0

def main(args):
  settings.generate_settings(args.config_path, args.results_path)
  config = read_config(args.name, args.config_path)
  print('\n\n\nPreparing test for', args.name, '\nRecommended Video Channels')
  videos = config['videos']
  for key in videos:
    print(key, ': ', videos[key])
  print ('\n')

  correct_count = 0
  for i in range(int(config['number_of_questions'])):
    print('Problem ', str(i + 1), ':')
    result = generate_problems(args.name, config)
    correct_count = correct_count + result
    score = correct_count/(i+1)
  print('Your score was ', correct_count, ' correct out of ', i + 1, ' problems.  Or ', "{:.0%}".format(score))
  reward.rewared_video(score)

if __name__ == "__main__":
  main(get_arg_parser().parse_args())
