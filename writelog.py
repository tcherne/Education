import datetime
import os


def log_writer(results_directory, log_entry):
  date = datetime.datetime.now().strftime('%Y%m%d')
  # directory = '/'.join([aresults_directory, args.name])
  filename = '/'.join([results_directory, date])
  if not os.path.exists(results_directory):
    os.makedirs(results_directory)
  with open(filename, "a") as file:
    file.writelines(log_entry + '\n')
