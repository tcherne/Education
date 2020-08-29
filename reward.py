import random
def rewared_video(score):
  video_list = ['https://www.youtube.com/watch?v=uINilnFCKQ8',
                'https://www.youtube.com/watch?v=TReCLbmhlMs',
                'https://www.youtube.com/watch?v=28xjtYY3V3Q',
                'https://www.youtube.com/watch?v=PYOSKYWg-5E',
                'https://www.youtube.com/watch?v=77VfQKzYsnY',
                'https://www.youtube.com/watch?v=QcdlGjAP0xs',
                'https://www.youtube.com/watch?v=WhzmR07WeKU&t=35s',
                'https://www.youtube.com/watch?v=SAgYiERRDPY',
                'https://www.youtube.com/watch?v=b6m-XlOxjbk',
                'https://www.youtube.com/watch?v=spMkaJp975s',
                'https://www.youtube.com/watch?v=n7gcats5uCQ',
                'https://www.youtube.com/watch?v=SCwcJsBYL3o',
                'https://www.youtube.com/watch?v=q9BAHM8KTWE',
                'https://www.youtube.com/watch?v=DkmeZwsi3HA',
                'https://www.youtube.com/watch?v=0bZbUrv1UK4',
                'https://www.youtube.com/watch?v=oMjI-8TPtRw',
                'https://www.youtube.com/watch?v=sbj0wRWY3QE',
                'https://www.youtube.com/watch?v=47UojiRyYHk',
                'https://www.youtube.com/watch?v=pI63Rbxml5U']

  video = random.choice(video_list)
  print('Good job, here is a fun video: ', video)
