import json

addition_videos = ['https://www.youtube.com/watch?v=4ilGm8cD77c', 'https://www.youtube.com/watch?v=LFki4BENvcw']
subtraction_videos = ['https://www.youtube.com/watch?v=L_1gwP8m2JM', 'https://www.youtube.com/watch?v=BkzoUfyAXDU']
multiplication_videos = ['https://www.youtube.com/watch?v=LD4zp8ruvaI', 'https://www.youtube.com/watch?v=FJ5qLWP3Fqo']
division_videos = ['https://www.youtube.com/watch?v=KGMf314LUc0', 'https://www.youtube.com/watch?v=NaECBQhTaCU']
fraction_videos = ['https://www.youtube.com/watch?v=7VcOShOuQMA', 'https://www.youtube.com/watch?v=C1dGmnS7g-4']
decimal_videos = ['https://www.youtube.com/watch?v=BItpeFXC4vA', 'https://www.youtube.com/watch?v=9frz4ODJUc0']
greaterthan_lessthan_videos = ['https://www.youtube.com/watch?v=YhOf0H_gLP8', 'https://www.youtube.com/watch?v=xGvrG6049wE']
skipcount_videos = ['https://www.youtube.com/watch?v=jYloCGfSoOk', 'https://www.youtube.com/watch?v=7AnoVea8UCM']
place_value_videos = ['https://www.youtube.com/watch?v=QS32l5WhSuY', 'https://www.youtube.com/watch?v=wx2gI8iwMCA']

def generate_settings(config_filepath, master_results_path):
  #generate the config json
  students = {
      'Master': {
        'results_directory': '/'.join([master_results_path, 'Master/']),
        'questions': {
          'addition': {'min': 0, 'max': 1000, 'videos': addition_videos},
          'subtraction': {'min': 0, 'max': 1000, 'videos': subtraction_videos},
          'multiplication': {'min': 0, 'max': 1000, 'videos': multiplication_videos},
          'division': {'min': 0, 'max': 1000, 'videos': division_videos},
          'fraction': {'min': 0, 'max': 10, 'videos': fraction_videos},
          'decimal': {'digits': 9, 'videos': decimal_videos},
          'greaterthan_lessthan': {'min': 0, 'max': 10, 'videos': greaterthan_lessthan_videos},
          'skipcount': {'by_values':[2,4,6], 'videos': skipcount_videos},
          'maketens': True,
          'place_value': {'min': 100, 'max': 999, 'videos':place_value_videos }
          },
        'number_of_questions':20
        },
      'Henry': {
        'results_directory': '/'.join([master_results_path, 'Henry/']),
        'questions': {
          'addition': {'min': 0, 'max': 1000, 'videos': addition_videos},
          'subtraction': {'min': 0, 'max': 1000, 'videos': subtraction_videos},
          'multiplication': {'min': 0, 'max': 1000, 'videos': multiplication_videos},
          'division': {'min': 0, 'max': 200, 'videos': division_videos},
          'fraction': {'min': 0, 'max': 50, 'videos': fraction_videos},
          'decimal': {'digits': 4, 'videos': decimal_videos},
          'greaterthan_lessthan': {'min': 0, 'max': 1000, 'videos': greaterthan_lessthan_videos},
          'skipcount': {'by_values':[3,4,6,7,8,9,11,12,13,14,15,100], 'videos': skipcount_videos},
          'place_value': {'min': 100, 'max': 999, 'videos':place_value_videos }
          },
        'number_of_questions':20
        },
      'Gavin': {
        'results_directory': '/'.join([master_results_path, 'Gavin/']),
        'questions': {
          'addition': {'min': 0, 'max': 500, 'videos': addition_videos},
          'subtraction': {'min': 0, 'max': 500, 'videos': subtraction_videos},
          'multiplication': {'min': 0, 'max': 10, 'videos': multiplication_videos},
          'fraction': {'min': 0, 'max': 20, 'videos': fraction_videos},
          'greaterthan_lessthan': {'min': 0, 'max': 500, 'videos': greaterthan_lessthan_videos},
          'skipcount': {'by_values':[2,3,4,5,6,7,8,9,10,12,15,100], 'videos': skipcount_videos},
          'maketens': True,
          'place_value': {'min': 100, 'max': 999, 'videos':place_value_videos }
          },
        'number_of_questions':20
        },
      'Benjamin': {
        'results_directory': '/'.join([master_results_path, 'Benjamin/']),
        'questions': {
          'addition': {'min': 0, 'max': 20, 'videos': addition_videos},
          'subtraction': {'min': 0, 'max': 20, 'videos': subtraction_videos},
          'fraction': {'min': 0, 'max': 6, 'videos': fraction_videos},
          'greaterthan_lessthan': {'min': 0, 'max': 25, 'videos': greaterthan_lessthan_videos},
          'skipcount': {'by_values':[2,4,5,10,100], 'videos': skipcount_videos},
          'maketens': True,
          'place_value': {'min': 100, 'max': 999, 'videos':place_value_videos }
          },
        'number_of_questions':20
        },
    }
  #write the config
  with open('/'.join([config_filepath, 'config']), 'w') as outfile:
    pretty_json = json.dumps(students, indent=2)
    json.dump(pretty_json, outfile)