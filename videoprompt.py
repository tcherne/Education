def print_video_message(videos, show_hints):
  if show_hints == True:
    print('For hints watch these videos:')
    for key, value in videos.items():
      print(key, ': ', value)
    print('\n')