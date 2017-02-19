import os
import json
import newspaper
from watson_developer_cloud import ToneAnalyzerV3

from constants import private

tone_analyzer = ToneAnalyzerV3(
   username=private.username,
   password=private.password,
   version='2016-05-19')

NEWS_SOURCES = [
  'http://www.buzzfeed.com',
  'http://www.occupydemocrats.com',
  'http://www.usuncut.com',
  'http://www.huffingtonpost.com',
  'http://www.msnbc.com',
  'http://www.theatlantic.com',
  'http://www.usatoday.com',
  'http://www.slate.com',
  'http://www.vox.com',
  'http://www.theguardian.com',
  'http://www.bbc.com',
  'http://www.washingtonpost.com',
  'http://www.newyorktimes.com',
  'http://www.abcnews.com',
  'http://www.ap.org',
  'http://www.reuters',
  'http://www.cnn.com',
  'http://www.thewallstreetjournal.com',
  'http://www.theeconomist.com',
  'http://www.thefiscal times.com',
  'http://www.thehill.com',
  'http://www.foxnews.com',
  'http://www.redstate.com',
  'http://www.theblaze.com',
]

LEARN = 'learn'
SENTIMENT = 'sentiment'
OUT = 'out'
LINKS = 'links'
CORPUS = 'corpus'
JSON = '.json'

for source in NEWS_SOURCES:
  fn = os.path.join(LEARN, SENTIMENT, source.split('.')[1] + JSON)
  print 'reading from website: %s' % source
  print 'writing to filename: %s' % fn
  with open(fn, 'a+') as json_file:
    paper = newspaper.build(source)
    num_articles = len(paper.articles)
    print 'len: %d ' % num_articles
    count = 0
    try:
      for article in paper.articles:
        print 'article.url: %s' % article.url
        article.download()
        article.parse()
        txt = article.text.encode('utf8')
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
