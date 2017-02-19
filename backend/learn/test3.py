import json
import os
import urllib
import pickle

import numpy as np
import time
import tldextract
from numpy import argmax
from sklearn.ensemble import RandomForestClassifier
import newspaper
from newspaper import Article
from watson_developer_cloud import ToneAnalyzerV3

from constants import private
from backendSummarization import extractSentences

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

# global POLITICAL_SPECTRUM
SPECTRUM = 'spectrum'
TRAINING = 'training'
SPECTRUM_JSON = 'spectrum.json'
with open(os.path.join(TRAINING, SPECTRUM, SPECTRUM_JSON)) as spectrum_json:
  print 'loading POLITICAL_SPECTRUM'
  POLITICAL_SPECTRUM = json.load(spectrum_json)
  print POLITICAL_SPECTRUM

# schema
DOCUMENT_TONE = 'document_tone'
TONE_CATEGORIES = 'tone_categories'
TONES = 'tones'
SCORE = 'score'
EXTRACT_DOMAIN = 1
EMOTION_CATEGORY = 0
STYLE_CATEGORY = 1
SOCIAL_CATEGORY = 2

VERBOSE = False
global _clf
global _clf_backup

def create_x_feature_vector(inference, source=None):
  tone_categories = inference[DOCUMENT_TONE][TONE_CATEGORIES]

  emotion_category = tone_categories[EMOTION_CATEGORY]
  style_category = tone_categories[STYLE_CATEGORY]
  social_category = tone_categories[SOCIAL_CATEGORY]

  x_i = []
  # print 'adding emotion category'
  for obj in [tone[SCORE] for tone in emotion_category[TONES][:]]:
    x_i.append(obj)

  # print 'adding style category'
  for obj in [tone[SCORE] for tone in style_category[TONES][:]]:
    x_i.append(obj)

  # print 'adding social category'
  for obj in [tone[SCORE] for tone in social_category[TONES][:]]:
    x_i.append(obj)

  # print 'adding source category'
  if source is not None and source in POLITICAL_SPECTRUM:
    x_i.append(POLITICAL_SPECTRUM[source])
  else:
    print '[create x ftr vector] SOURCE NOT IN POLITICAL_SPECTRUM %s ' % source
    x_i.append(np.random.randint(-2, 3)) # remove to train a backup tree

  return x_i

def init_tree():
  global _clf
  global _clf_backup
  X = []
  X_backup = []
  Y = []

  for fn in os.listdir(SENTIMENT):
    print 'file: %s' % fn
    source = fn.split('.')[0]

    if source in POLITICAL_SPECTRUM:
      y_val = POLITICAL_SPECTRUM[source]
    else:
      print '[init tree] SOURCE NOT IN POLITICAL_SPECTRUM %s ' % source
      y_val = np.random.randint(-2, 3)

    with open(os.path.join(SENTIMENT, fn), 'r') as json_file:
      src_tone_data = json.load(json_file)
      for inference in src_tone_data:
        X.append(create_x_feature_vector(inference, source=source))
        X_backup.append(create_x_feature_vector(inference))

        Y.append(y_val)

  # print X
  # print Y

  curr_time = time.time()
  with open('training/x/x_features_%s' % curr_time, 'wb') as fp:
    pickle.dump(X, fp)
  with open('training/y/y_features_%s' % curr_time, 'wb') as fp:
    pickle.dump(Y, fp)

  print len(X)
  print len(Y)

  print 'classifier'
  _clf = RandomForestClassifier(n_estimators=20)
  _clf = _clf.fit(X, Y)
  print _clf.classes_

  print 'backup'
  _clf_backup = RandomForestClassifier(n_estimators=40)
  _clf_backup = _clf_backup.fit(X_backup, Y)
  print _clf_backup.classes_


def run_inference(hyperlink):
  global _clf
  global _clf_backup

  X = []
  retval = []
  try:
    article = newspaper.Article(hyperlink)
    article.download()
    article.parse()

    inference = tone_analyzer.tone(text=article.text.encode('utf-8'))

    print inference

    domain = tldextract.extract(article.url)[EXTRACT_DOMAIN]
    print 'extracted domain %s' % domain
    use_backup_tree = domain in POLITICAL_SPECTRUM
    if use_backup_tree:
      X.append(create_x_feature_vector(inference, source=domain))
      # retval = _clf_backup.predict(X)
      retval = _clf.predict_proba(X)
      retval = _clf_backup.predict_proba(X)
    else:
      X.append(create_x_feature_vector(inference, source=domain))
      # retval = _clf.predict(X)
      retval = _clf.predict_proba(X)
    print X

    print 'spectrum score: %s' % retval
  except Exception as e:
    print '[run infr on link] ANALYSIS ERROR %s ' % e

  weighted_avg = 0
  for i in xrange(len(retval[0])):
    weight = retval[0][i]
    weighted_avg += (i - 2) * weight

  return weighted_avg, argmax(retval)


def run_inference_on_text(text):
  # print text
  global _clf
  global _clf_backup

  X = []
  try:
    inference = tone_analyzer.tone(text=text)
    X.append(create_x_feature_vector(inference))

    # retval = _clf.predict(X)
    retval = _clf.predict_proba(X)
    print 'spectrum score: %s' % retval
  except Exception as e:
    print '[run infr on txt] ANALYSIS ERROR %s ' % e



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

def test_tree():
  for test in TEST:
    print test
    for hyperlink in TEST[test]:
      print 'hyperlink %s ' % hyperlink
      run_inference(hyperlink)

  OCCUPY_ARTICLE = 'occupy_article'
  print 'occupy test expected -2'
  for fn in os.listdir(OCCUPY_ARTICLE):
    with open(os.path.join(OCCUPY_ARTICLE, fn), 'r') as article_file:
      lines = article_file.readlines()
      run_inference_on_text(''.join(lines))

# initialize the Flask app
init_tree()
test_tree()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
  return 'hello'


"""

"""
@app.route('/spectrum', methods=['GET'])
def spectrum():
  url = request.args.get('url')
  print url

  # extract summary, score, suggested sites
  summary, original, title, brand = extractSentences(url.encode('utf-8'))
  weighted_avg, max_score = run_inference(url)

  print 'brand: %s' % brand
  print 'weighted_avg: %s' % weighted_avg
  print 'summary: %s' % summary

  result = {}
  result['title'] = title
  result['brand'] = brand
  result['weighted_average'] = weighted_avg
  result['summary'] = summary

  return json.dumps(result)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000)