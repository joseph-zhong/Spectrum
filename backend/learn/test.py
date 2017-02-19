import json
import os
import newspaper
from watson_developer_cloud import ToneAnalyzerV3

from constants import private

tone_analyzer = ToneAnalyzerV3(
   username=private.username,
   password=private.password,
   version='2016-05-19')

LEARN = 'learn'
SENTIMENT = 'sentiment'
JSON = '.json'

source = [
  'http://www.occupydemocrats.com',
  # 'https://www.buzzfeed.com/',
  # 'https://www.buzzfeed.com/news',
]

for src in source:
  fn = os.path.join(SENTIMENT, src.split('.')[1] + JSON)
  print 'reading from website: %s' % src
  print 'writing to filename: %s' % fn
  with open(fn, 'a+') as json_file:
    paper = newspaper.build(src)
    num_articles = len(paper.articles)
    print 'len: %d ' % num_articles
    count = 0
    try:
      for article in paper.articles:
        print 'article.url: %s' % article.url
        article.download()
        article.parse()
        txt = article.text.encode('utf8')
        print txt
        try:
          analysis = json.dumps(tone_analyzer.tone(text=txt), indent=0)
          print(analysis)
          json_file.write(analysis)
        except Exception as e:
          print 'ANALYSIS ERROR %s ' % e

        count += 1
        print 'success: %d out of %d' % (count, num_articles)
    except Exception as e:
      print 'PARSE ERROR %s ' % e
