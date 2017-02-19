import json
import os

import numpy as np
from numpy import argmax
from sklearn.ensemble import RandomForestClassifier
import newspaper
from newspaper import Article
from watson_developer_cloud import ToneAnalyzerV3

from constants import private
from backendSummarization import extractSentences, bingArticle

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify

tone_analyzer = ToneAnalyzerV3(
   username=private.username,
   password=private.password,
   version='2016-05-19')

SENTIMENT = 'sentiment'

# See FEATURES.md about features and classifications
FEATURES = {
  'anger', 'disgust', 'fear', 'joy', 'sadness',
  'analytical', 'confident', 'tentative',
  'openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional range'
}
CLASSIFICATIONS = {
  -2: ['BuzzFeed', 'OccupyDemocrats', 'US Uncut'],
  -1: ['HuffingtonPost', 'MSNBC', 'Atlantic', 'Slate', 'Vox', 'The Guardian'],
  0: ['NPR', 'BBC', 'WashingtonPost', 'New York Times', 'ABC News','AP','Reuters',
      'USA Today', 'CNN', 'The Wall Street Journal'],
  1: ['The Economist', 'The Fiscal Times', 'The Hill', 'Fox News'],
  2: ['Red State', 'The Blaze']
}

POLITICAL_SPECTRUM = {
  'buzzfeed': -2,
  'occupydemocrats': -2,
  'usuncut': -2,
  'huffingtonpost': -1,
  'msnbc': -1,
  'atlantic': -1,
  'slate': -1,
  'vox': -1,
  'theguardian': -1,
  'npr': 0,
  'bbc': 0,
  'washingtonpost': 0,
  'newyorktimes': 0,
  'abcnews': 0,
  'ap': 0,
  'reuters': 0,
  'usatoday': 0,
  'cnn': 0,
  'thewallstreetjournal': 0,
  'theeconomist': 1,
  'thefiscaltimes': 1,
  'thehill': 1,
  'foxnews': 1,
  'redstate': 2,
  'theblaze': 2
}




# schema
DOCUMENT_TONE = 'document_tone'
TONE_CATEGORIES = 'tone_categories'
TONES = 'tones'
SCORE = 'score'
EMOTION_CATEGORY = 0
STYLE_CATEGORY = 1
SOCIAL_CATEGORY = 2

VERBOSE = False
global _clf


def init_tree():
  global _clf

  X = []
  Y = []

  for fn in os.listdir(SENTIMENT):
    print 'file: %s' % fn
    source = fn.split('.')[0]

    if source in POLITICAL_SPECTRUM:
      y_val = POLITICAL_SPECTRUM[source]
    else:
      y_val = 0

    with open(os.path.join(SENTIMENT, fn), 'r') as json_file:
      src_tone_data = json.load(json_file)
      for inference in src_tone_data:
        tone_categories = inference[DOCUMENT_TONE][TONE_CATEGORIES]
        emotion_category = tone_categories[EMOTION_CATEGORY]
        style_category = tone_categories[EMOTION_CATEGORY]
        social_category = tone_categories[EMOTION_CATEGORY]

        x_i = []
        for obj in [tone[SCORE] for tone in emotion_category[TONES][:]]:
          x_i.append(obj)

        for obj in [tone[SCORE] for tone in style_category[TONES][:]]:
          x_i.append(obj)

        for obj in [tone[SCORE] for tone in social_category[TONES][:]]:
          x_i.append(obj)

        X.append(x_i)
        Y.append(y_val)

  if VERBOSE:
    print X
    print Y
  print len(X)
  print len(Y)

  _clf = RandomForestClassifier(n_estimators=20)
  _clf = _clf.fit(X, Y)
  print _clf.classes_

  # dot_data = tree.export_graphviz(_clf, out_file=None,
  #                                 filled=True, rounded=True,
  #                                 special_characters=True)
  # graph = pydotplus.graph_from_dot_data(dot_data)
  # Image(graph.create_png())

def run_inference(hyperlink):
  global _clf

  X = []
  retval = []
  try:
    article = newspaper.Article(hyperlink)
    article.download()
    article.parse()

    inference = tone_analyzer.tone(text=article.text.encode('utf-8'))

    tone_categories = inference[DOCUMENT_TONE][TONE_CATEGORIES]
    emotion_category = tone_categories[EMOTION_CATEGORY]
    style_category = tone_categories[EMOTION_CATEGORY]
    social_category = tone_categories[EMOTION_CATEGORY]

    x_i = []
    for obj in [tone[SCORE] for tone in emotion_category[TONES][:]]:
      x_i.append(obj)

    for obj in [tone[SCORE] for tone in style_category[TONES][:]]:
      x_i.append(obj)

    for obj in [tone[SCORE] for tone in social_category[TONES][:]]:
      x_i.append(obj)

    X.append(x_i)

    # retval = _clf.predict(X)
    retval = _clf.predict_proba(X)
    print 'spectrum score: %s' % retval
  except Exception as e:
    print 'ANALYSIS ERROR %s ' % e

  weighted_avg = 0
  for i in xrange(len(retval)):
    weight = retval[i]
    weighted_avg += (i - 2) * weight
  return weighted_avg, argmax(retval)

def run_inference_on_text(text):
  # print text
  global _clf

  X = []
  try:
    inference = tone_analyzer.tone(text=text)

    tone_categories = inference[DOCUMENT_TONE][TONE_CATEGORIES]
    emotion_category = tone_categories[EMOTION_CATEGORY]
    style_category = tone_categories[EMOTION_CATEGORY]
    social_category = tone_categories[EMOTION_CATEGORY]

    x_i = []
    for obj in [tone[SCORE] for tone in emotion_category[TONES][:]]:
      x_i.append(obj)

    for obj in [tone[SCORE] for tone in style_category[TONES][:]]:
      x_i.append(obj)

    for obj in [tone[SCORE] for tone in social_category[TONES][:]]:
      x_i.append(obj)

    X.append(x_i)

    retval = _clf.predict(X)
    # retval = _clf.predict_proba(X)
    print 'spectrum score: %s' % retval
  except Exception as e:
    print 'ANALYSIS ERROR %s ' % e



TEST = {
  'test expected -2' : [
    'http://occupydemocrats.com/2017/02/19/senate-intelligence-committee-just-secured-trump-russia-evidence-trump-cant-destroy/',
    'http://occupydemocrats.com/2017/02/19/senate-intelligence-committee-just-secured-trump-russia-evidence-trump-cant-destroy/',
    'http://occupydemocrats.com/2017/02/18/dan-rather-just-destroyed-republicans-enabling-trump-viral-post/',
  ],
  'test expected -1' : [

  ],
  'test expected 0' : [
    'http://www.nbcnews.com/news/us-news/flynn-s-resignation-could-thrust-white-house-legal-thicket-n721346',
    'http://www.nbcnews.com/politics/white-house/trump-again-attacks-media-campaign-style-rally-florida-n722891?cid=par-nbc_20170219',
    'http://www.nbcnews.com/business/autos/tesla-under-fire-after-explosive-crash-n722541',
    'http://www.nbcnews.com/politics/elections/dnc-race-shakeup-ray-buckley-exit-endorse-keith-ellison-n722591'
  ],
  'test expected 1' : [

  ],
  'test expected 2' : [
    'http://www.breitbart.com/milo/2017/02/18/leftist-columnists-throw-tantrum-attack-bill-maher-milo-appearance/',
    'http://www.breitbart.com/milo/2017/02/18/deray-mckesson-attacks-bill-maher-for-interviewing-milo/',
    'http://www.breitbart.com/milo/2017/02/18/milo-deliver-keynote-address-cpac/',
  ]
}


init_tree()
# for test in TEST:
#   print test
#   for hyperlink in TEST[test]:
#     # print hyperlink
#     run_inference(hyperlink)
#
# OCCUPY_ARTICLE = 'occupy_article'
# print 'occupy test expected -2'
# for fn in os.listdir(OCCUPY_ARTICLE):
#   with open(os.path.join(OCCUPY_ARTICLE, fn), 'r') as article_file:
#     lines = article_file.readlines()
#     run_inference_on_text(''.join(lines))


# initialize the Flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
  return 'hello'


"""

"""
@app.route('/spectrum', methods=['POST'])
def spectrum():
  data = json.loads(request.data.decode())
  print data

  url = data['url']

  # extract summary, score, suggested sites
  summary, original, title = extractSentences(url.encode('utf-8'), 3)
  political_score, max_score = run_inference(original)[0]

  suggestions = []
  for i in range(3):
    suggestions.append(bingArticle(title, np.random.choice(CLASSIFICATIONS[-(max_score) - 1])))

  result = {}
  result['summary'] = summary
  result['sentences'] = summary
  result['political_score'] = political_score
  result['suggestions'] = suggestions

  return json.dumps(result)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)