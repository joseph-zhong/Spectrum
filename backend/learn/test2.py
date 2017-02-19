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
TARGET = 'occupy_article'
JSON = '.json'
TARGET_FN = 'occupydemocrats.json'


with open(os.path.join(SENTIMENT, TARGET_FN), 'a+') as json_file:
  for fn in os.listdir(TARGET):
    with open(os.path.join(TARGET, fn), 'r') as article:
      txt = ''.join(article.readlines())
      print txt
      try:
        analysis = tone_analyzer.tone(text=txt.encode('utf-8'))
        print(analysis)

        json_file.write(analysis)
      except Exception as e:
        print 'ANALYSIS ERROR %s ' % e
