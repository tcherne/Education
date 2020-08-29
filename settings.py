import json

#example commandline
#python3 /home/timcherne/PythonProjects/Education_Program/educate.py -n Master -r /home/timcherne/Test_Results

addition_videos = {'Basic Addition':'https://www.youtube.com/watch?v=AuX7nPBqDts',
  'Number bonds':'https://www.youtube.com/watch?v=PGjeaWcXMao',
  'Make ten strategy':'https://www.youtube.com/watch?v=q9h4skGoWJ8',
  'Fill in the blank addition': 'https://www.youtube.com/watch?v=9FC0WT186aY',
  'Addition Carry Over':'https://www.youtube.com/watch?v=fOXo4p4WDKM'}
subtraction_videos = {'Relate Addition and Subtraction': 'https://www.youtube.com/watch?v=zVLjWIftX_o',
  'Two digit number bonds':'https://www.youtube.com/watch?v=6GOOjx2Zbq0',
  'Multi digit subtract with carryover':'https://www.youtube.com/watch?v=Y6M89-6106I',
  'Advanced Subtraction': 'https://www.youtube.com/watch?v=omUfrXtHtN0'}
multiplication_videos = {'Multiplication shown as addition': 'https://www.youtube.com/watch?v=qUAeDpmqWDQ',
  'One Digit Example': 'https://www.youtube.com/watch?v=mvOkMYCygps',
  'Numberline/Skip Counting and Multiplication':'https://www.youtube.com/watch?v=PLDfl6daajo',
  'Two Digit Numbers':'https://www.youtube.com/watch?v=DaQlieZH1kk'}
division_videos = {'Multiplication and Division Relationship': 'https://www.youtube.com/watch?v=i31rRt5m1-4',
  'Dividing by 10':'https://www.youtube.com/watch?v=Ehd3cgRBvl0',
  'Division and Fractions':'https://www.youtube.com/watch?v=c-_yrA-GUow',
  'Basic Division':'https://www.youtube.com/watch?v=rGMecZ_aERo',
  'Long Division': 'https://www.youtube.com/watch?v=HY-8ydAbiik',
  'Understanding why long division works': 'https://www.youtube.com/watch?v=jTbIw2iR8WU'}
fraction_videos = {'Comparing Fractions':'https://www.youtube.com/watch?v=8OKTrN0uT-Q',
  'Comparing Fractions with the Same Denominator or Numerator': 'https://www.youtube.com/watch?v=wbAxarp_Ug4',
  'Comparing Fractions with Different Denominators': 'https://www.youtube.com/watch?v=Oo-sc0v0zBU',
  }
decimal_videos = {'Comparing Decimals': 'https://www.youtube.com/watch?v=EX9CdUAMpgE&t=18s',
  'Comparing complex decimals':'https://www.youtube.com/watch?v=Dese7hoWZMM&t=17s',
  'Place Value':'https://www.youtube.com/watch?v=wtrrr15mbvQ'}
greaterthan_lessthan_videos = {'What do the signs mean?': 'https://www.youtube.com/watch?v=nFsQA2Zvy1o',
  'Alligator Chomp Song':'https://www.youtube.com/watch?v=xGvrG6049wE'}
skipcount_videos = {'Counting groups of pigs': 'https://www.youtube.com/watch?v=1tjJDdszcZg',
  'Skip counting charts':'https://www.youtube.com/watch?v=sQP5VRnCCUY'}
place_value_videos = {'Place Value Introduction': 'https://www.youtube.com/watch?v=wx2gI8iwMCA',
  'Find the value of a place value number':'https://www.youtube.com/watch?v=jxA8MffVmPs'}

def generate_settings(config_filepath, master_results_path):
  #generate the config json
  students = {
      'Master': {
        'results_directory': '/'.join([master_results_path, 'Master/']),
        'questions': {
          'addition': {'min': 0, 'max': 1000, 'videos': addition_videos},
          # 'subtraction': {'min': 0, 'max': 1000, 'videos': subtraction_videos},
          # 'multiplication': {'max_one': 1000, 'max_two': 1000, 'videos': multiplication_videos},
          # 'division': {'num_max': 1000, 'denom_max': 1000, 'videos': division_videos},
          # 'fraction': {'min': 0, 'max': 10, 'videos': fraction_videos},
          # 'decimal': {'digits': 9, 'videos': decimal_videos},
          # 'greaterthan_lessthan': {'min': 0, 'max': 10, 'videos': greaterthan_lessthan_videos},
          # 'skipcount': {'by_values':[15], 'videos': skipcount_videos},
          # 'maketens': True,
          # 'place_value': {'min': 100, 'max': 999, 'videos':place_value_videos }
          },
        'number_of_questions':2
        },
      'Henry': {
        'results_directory': '/'.join([master_results_path, 'Henry/']),
        'questions': {
          'addition': {'min': 0, 'max': 1000, 'videos': addition_videos},
          'subtraction': {'min': 0, 'max': 1000, 'videos': subtraction_videos},
          'multiplication': {'max_one': 200, 'max_two': 1000, 'videos': multiplication_videos},
          'division': {'num_max': 25, 'denom_max': 50000, 'videos': division_videos},
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
          'multiplication': {'max_one': 5, 'max_two': 5, 'videos': multiplication_videos},
          'fraction': {'min': 0, 'max': 4, 'videos': fraction_videos},
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
          'fraction': {'min': 0, 'max': 4, 'videos': fraction_videos},
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
