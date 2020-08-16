import json

CONFIG = '/home/timcherne/PythonProjects/Education_Program/config'

students = {
    'Master': {
      'results_directory': '/home/timcherne/Test_Results/Master/',
      'questions': {
        'addition': {'min': 0, 'max': 1000},
        'subtraction': {'min': 0, 'max': 1000},
        'multiplication': {'min': 0, 'max': 1000},
        'division': {'min': 0, 'max': 1000},
        'fraction': {'min': 0, 'max': 10},
        'decimal': {'digits': 9},
        'greaterthan_lessthan': {'min': 0, 'max': 10},
        'skipcount': {'by_values':[2,4,6]},
        'maketens': True,
        'place_value': {'min': 100, 'max': 999}
        },
      'number_of_questions':20
      },
      'Henry': {
      'results_directory': '/home/timcherne/Test_Results/Henry/',
      'questions': {
        'addition': {'min': 0, 'max': 1000},
        'subtraction': {'min': 0, 'max': 1000},
        'multiplication': {'min': 0, 'max': 250},
        'division': {'min': 0, 'max': 200},
        'fraction': {'min': 0, 'max': 50},
        'decimal': {'digits': 4},
        'skipcount': {'by_values':[3,4,6,7,8,9,11,12,13,14,15]}
        },
      'number_of_questions':20
      },
      'Gavin': {
      'results_directory': '/home/timcherne/Test_Results/Gavin/',
      'questions': {
        'addition': {'min': 0, 'max': 500},
        'subtraction': {'min': 0, 'max': 500},
        'multiplication': {'min': 0, 'max': 10},
        'fraction': {'min': 0, 'max': 20},
        'greaterthan_lessthan': {'min': 0, 'max': 250},
        'skipcount': {'by_values':[2,3,4,5,6,7,8,9,10,11,12,13,14,15]},
        'maketens': True,
        'place_value': {'min': 100, 'max': 999}
        },
      'number_of_questions':20
      },
      'Benjamin': {
      'results_directory': '/home/timcherne/Test_Results/Benjamin/',
      'questions': {
        'addition': {'min': 0, 'max': 20},
        'subtraction': {'min': 0, 'max': 20},
        'fraction': {'min': 0, 'max': 10},
        'greaterthan_lessthan': {'min': 0, 'max': 20},
        'skipcount': {'by_values':[2,3,4,5,10]},
        'maketens': True,
        'place_value': {'min': 100, 'max': 999}
        },
      'number_of_questions':20
      }
  }


with open(CONFIG, 'w') as outfile:
  pretty_json = json.dumps(students, indent=2)
  print(pretty_json)
  json.dump(pretty_json, outfile)