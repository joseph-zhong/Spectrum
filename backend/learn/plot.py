import numpy as np
import matplotlib.pyplot as plt
import os
import json

# directory
SENTIMENT_DIR = 'sentiment'

# classification
CLASSIFICATIONS = {-2, -1, 0, 1, 2}
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

# plotting features
FEATURE = 'feature'
CONFIDENCE = 'confidence'

anger = []
disgust = []
fear = []
joy = []
sadness = []
analytical = []
confident = []
tentative = []
openness = []
conscientiousness = []
extraversion = []
agreeableness = []
emotional_range = []

anger1 = []
disgust1 = []
fear1 = []
joy1 = []
sadness1 = []
analytical1 = []
confident1 = []
tentative1 = []
openness1 = []
conscientiousness1 = []
extraversion1 = []
agreeableness1 = []
emotional_range1 = []

anger2 = []
disgust2 = []
fear2 = []
joy2 = []
sadness2 = []
analytical2 = []
confident2 = []
tentative2 = []
openness2 = []
conscientiousness2 = []
extraversion2 = []
agreeableness2 = []
emotional_range2 = []

anger3 = []
disgust3 = []
fear3 = []
joy3 = []
sadness3 = []
analytical3 = []
confident3 = []
tentative3 = []
openness3 = []
conscientiousness3 = []
extraversion3 = []
agreeableness3 = []
emotional_range3 = []

anger4 = []
disgust4 = []
fear4 = []
joy4 = []
sadness4 = []
analytical4 = []
confident4 = []
tentative4 = []
openness4 = []
conscientiousness4 = []
extraversion4 = []
agreeableness4 = []
emotional_range4 = []

def aggregate_data_helper(tone_categories, index):
  print index
  if index == -2:
    # Emotion
    anger.append(tone_categories[EMOTION_CATEGORY][TONES][0][SCORE])
    disgust.append(tone_categories[EMOTION_CATEGORY][TONES][1][SCORE])
    fear.append(tone_categories[EMOTION_CATEGORY][TONES][2][SCORE])
    joy.append(tone_categories[EMOTION_CATEGORY][TONES][3][SCORE])
    sadness.append(tone_categories[EMOTION_CATEGORY][TONES][4][SCORE])

    # Style
    analytical.append(tone_categories[STYLE_CATEGORY][TONES][0][SCORE])
    confident.append(tone_categories[STYLE_CATEGORY][TONES][1][SCORE])
    tentative.append(tone_categories[STYLE_CATEGORY][TONES][2][SCORE])

    # Social
    openness.append(tone_categories[SOCIAL_CATEGORY][TONES][0][SCORE])
    conscientiousness.append(
      tone_categories[SOCIAL_CATEGORY][TONES][1][SCORE])
    extraversion.append(tone_categories[SOCIAL_CATEGORY][TONES][2][SCORE])
    agreeableness.append(tone_categories[SOCIAL_CATEGORY][TONES][3][SCORE])
    emotional_range.append(tone_categories[SOCIAL_CATEGORY][TONES][4][SCORE])
  elif index == -1:
    # Emotion
    anger1.append(tone_categories[EMOTION_CATEGORY][TONES][0][SCORE])
    disgust1.append(tone_categories[EMOTION_CATEGORY][TONES][1][SCORE])
    fear1.append(tone_categories[EMOTION_CATEGORY][TONES][2][SCORE])
    joy1.append(tone_categories[EMOTION_CATEGORY][TONES][3][SCORE])
    sadness1.append(tone_categories[EMOTION_CATEGORY][TONES][4][SCORE])

    # Style
    analytical1.append(tone_categories[STYLE_CATEGORY][TONES][0][SCORE])
    confident1.append(tone_categories[STYLE_CATEGORY][TONES][1][SCORE])
    tentative1.append(tone_categories[STYLE_CATEGORY][TONES][2][SCORE])

    # Social
    openness1.append(tone_categories[SOCIAL_CATEGORY][TONES][0][SCORE])
    conscientiousness1.append(
      tone_categories[SOCIAL_CATEGORY][TONES][1][SCORE])
    extraversion1.append(tone_categories[SOCIAL_CATEGORY][TONES][2][SCORE])
    agreeableness1.append(tone_categories[SOCIAL_CATEGORY][TONES][3][SCORE])
    emotional_range1.append(tone_categories[SOCIAL_CATEGORY][TONES][4][SCORE])
  elif index == 0:
    # Emotion
    anger2.append(tone_categories[EMOTION_CATEGORY][TONES][0][SCORE])
    disgust2.append(tone_categories[EMOTION_CATEGORY][TONES][1][SCORE])
    fear2.append(tone_categories[EMOTION_CATEGORY][TONES][2][SCORE])
    joy2.append(tone_categories[EMOTION_CATEGORY][TONES][3][SCORE])
    sadness2.append(tone_categories[EMOTION_CATEGORY][TONES][4][SCORE])

    # Style
    analytical2.append(tone_categories[STYLE_CATEGORY][TONES][0][SCORE])
    confident2.append(tone_categories[STYLE_CATEGORY][TONES][1][SCORE])
    tentative2.append(tone_categories[STYLE_CATEGORY][TONES][2][SCORE])

    # Social
    openness2.append(tone_categories[SOCIAL_CATEGORY][TONES][0][SCORE])
    conscientiousness2.append(
      tone_categories[SOCIAL_CATEGORY][TONES][1][SCORE])
    extraversion2.append(tone_categories[SOCIAL_CATEGORY][TONES][2][SCORE])
    agreeableness2.append(tone_categories[SOCIAL_CATEGORY][TONES][3][SCORE])
    emotional_range2.append(tone_categories[SOCIAL_CATEGORY][TONES][4][SCORE])
  elif index == 1:
    # Emotion
    anger3.append(tone_categories[EMOTION_CATEGORY][TONES][0][SCORE])
    disgust3.append(tone_categories[EMOTION_CATEGORY][TONES][1][SCORE])
    fear3.append(tone_categories[EMOTION_CATEGORY][TONES][2][SCORE])
    joy3.append(tone_categories[EMOTION_CATEGORY][TONES][3][SCORE])
    sadness3.append(tone_categories[EMOTION_CATEGORY][TONES][4][SCORE])

    # Style
    analytical3.append(tone_categories[STYLE_CATEGORY][TONES][0][SCORE])
    confident3.append(tone_categories[STYLE_CATEGORY][TONES][1][SCORE])
    tentative3.append(tone_categories[STYLE_CATEGORY][TONES][2][SCORE])

    # Social
    openness3.append(tone_categories[SOCIAL_CATEGORY][TONES][0][SCORE])
    conscientiousness3.append(
      tone_categories[SOCIAL_CATEGORY][TONES][1][SCORE])
    extraversion3.append(tone_categories[SOCIAL_CATEGORY][TONES][2][SCORE])
    agreeableness3.append(tone_categories[SOCIAL_CATEGORY][TONES][3][SCORE])
    emotional_range3.append(tone_categories[SOCIAL_CATEGORY][TONES][4][SCORE])
  elif index == 2:
    # Emotion
    anger4.append(tone_categories[EMOTION_CATEGORY][TONES][0][SCORE])
    disgust4.append(tone_categories[EMOTION_CATEGORY][TONES][1][SCORE])
    fear4.append(tone_categories[EMOTION_CATEGORY][TONES][2][SCORE])
    joy4.append(tone_categories[EMOTION_CATEGORY][TONES][3][SCORE])
    sadness4.append(tone_categories[EMOTION_CATEGORY][TONES][4][SCORE])

    # Style
    analytical4.append(tone_categories[STYLE_CATEGORY][TONES][0][SCORE])
    confident4.append(tone_categories[STYLE_CATEGORY][TONES][1][SCORE])
    tentative4.append(tone_categories[STYLE_CATEGORY][TONES][2][SCORE])

    # Social
    openness4.append(tone_categories[SOCIAL_CATEGORY][TONES][0][SCORE])
    conscientiousness4.append(
      tone_categories[SOCIAL_CATEGORY][TONES][1][SCORE])
    extraversion4.append(tone_categories[SOCIAL_CATEGORY][TONES][2][SCORE])
    agreeableness4.append(tone_categories[SOCIAL_CATEGORY][TONES][3][SCORE])
    emotional_range4.append(tone_categories[SOCIAL_CATEGORY][TONES][4][SCORE])

def aggregate_data(src):
  print src
  with open(os.path.join(SENTIMENT_DIR, fn), 'r') as data_file:
    str = ""
    for line in data_file:
      str += line

    d = json.loads(str)
    print d

    for i in xrange(len(d)):
      obj = d[i]
      tone_categories = obj[DOCUMENT_TONE][TONE_CATEGORIES]
      aggregate_data_helper(tone_categories, POLITICAL_SPECTRUM[src])

def plot_all_data():
  fig = plt.figure()
  fig.suptitle('Liberal')
  plt.xlabel(CONFIDENCE, fontsize=18)
  plt.ylabel(FEATURE, fontsize=16)
  plt.grid('on')


  plt.plot(anger, np.zeros_like(anger) + 0, 'x')
  plt.plot(disgust, np.zeros_like(disgust) + 1, 'x')
  plt.plot(fear, np.zeros_like(fear) + 2, 'x')
  plt.plot(joy, np.zeros_like(joy) + 3, 'x')
  plt.plot(sadness, np.zeros_like(sadness) + 4, 'x')
  plt.plot(analytical, np.zeros_like(analytical) + 5, 'x')
  plt.plot(confident, np.zeros_like(confident) + 6, 'x')
  plt.plot(tentative, np.zeros_like(tentative) + 7, 'x')
  plt.plot(openness, np.zeros_like(openness) + 8, 'x')
  plt.plot(conscientiousness, np.zeros_like(conscientiousness) + 9, 'x')
  plt.plot(extraversion, np.zeros_like(extraversion) + 10, 'x')
  plt.plot(agreeableness, np.zeros_like(agreeableness) + 11, 'x')
  plt.plot(emotional_range, np.zeros_like(emotional_range) + 12, 'x')


  fig = plt.figure()
  fig.suptitle('Center Liberal')
  plt.xlabel(CONFIDENCE, fontsize=18)
  plt.ylabel(FEATURE, fontsize=16)
  plt.grid('on')

  plt.plot(anger1, np.zeros_like(anger1) + 0, 'x')
  plt.plot(disgust1, np.zeros_like(disgust1) + 1, 'x')
  plt.plot(fear1, np.zeros_like(fear1) + 2, 'x')
  plt.plot(joy1, np.zeros_like(joy1) + 3, 'x')
  plt.plot(sadness1, np.zeros_like(sadness1) + 4, 'x')
  plt.plot(analytical1, np.zeros_like(analytical1) + 5, 'x')
  plt.plot(confident1, np.zeros_like(confident1) + 6, 'x')
  plt.plot(tentative1, np.zeros_like(tentative1) + 7, 'x')
  plt.plot(openness1, np.zeros_like(openness1) + 8, 'x')
  plt.plot(conscientiousness1, np.zeros_like(conscientiousness1) + 9, 'x')
  plt.plot(extraversion1, np.zeros_like(extraversion1) + 10, 'x')
  plt.plot(agreeableness1, np.zeros_like(agreeableness1) + 11, 'x')
  plt.plot(emotional_range1, np.zeros_like(emotional_range1) + 12, 'x')

  fig = plt.figure()
  fig.suptitle('Bi-partisan')
  plt.xlabel(CONFIDENCE, fontsize=18)
  plt.ylabel(FEATURE, fontsize=16)
  plt.grid('on')

  plt.plot(anger2, np.zeros_like(anger2) + 0, 'x')
  plt.plot(disgust2, np.zeros_like(disgust2) + 1, 'x')
  plt.plot(fear2, np.zeros_like(fear2) + 2, 'x')
  plt.plot(joy2, np.zeros_like(joy2) + 3, 'x')
  plt.plot(sadness2, np.zeros_like(sadness2) + 4, 'x')
  plt.plot(analytical2, np.zeros_like(analytical2) + 5, 'x')
  plt.plot(confident2, np.zeros_like(confident2) + 6, 'x')
  plt.plot(tentative2, np.zeros_like(tentative2) + 7, 'x')
  plt.plot(openness2, np.zeros_like(openness2) + 8, 'x')
  plt.plot(conscientiousness2, np.zeros_like(conscientiousness2) + 9, 'x')
  plt.plot(extraversion2, np.zeros_like(extraversion2) + 10, 'x')
  plt.plot(agreeableness2, np.zeros_like(agreeableness2) + 11, 'x')
  plt.plot(emotional_range2, np.zeros_like(emotional_range2) + 12, 'x')


  fig = plt.figure()
  fig.suptitle('Center Conservative')
  plt.xlabel(CONFIDENCE, fontsize=18)
  plt.ylabel(FEATURE, fontsize=16)
  plt.grid('on')

  plt.plot(anger3, np.zeros_like(anger3) + 0, 'x')
  plt.plot(disgust3, np.zeros_like(disgust3) + 1, 'x')
  plt.plot(fear3, np.zeros_like(fear3) + 2, 'x')
  plt.plot(joy3, np.zeros_like(joy3) + 3, 'x')
  plt.plot(sadness3, np.zeros_like(sadness3) + 4, 'x')
  plt.plot(analytical3, np.zeros_like(analytical3) + 5, 'x')
  plt.plot(confident3, np.zeros_like(confident3) + 6, 'x')
  plt.plot(tentative3, np.zeros_like(tentative3) + 7, 'x')
  plt.plot(openness3, np.zeros_like(openness3) + 8, 'x')
  plt.plot(conscientiousness3, np.zeros_like(conscientiousness3) + 9, 'x')
  plt.plot(extraversion3, np.zeros_like(extraversion3) + 10, 'x')
  plt.plot(agreeableness3, np.zeros_like(agreeableness3) + 11, 'x')
  plt.plot(emotional_range3, np.zeros_like(emotional_range3) + 12, 'x')

  fig = plt.figure()
  fig.suptitle('Conservative')
  plt.xlabel(CONFIDENCE, fontsize=18)
  plt.ylabel(FEATURE, fontsize=16)
  plt.grid('on')

  plt.plot(anger4, np.zeros_like(anger4) + 0, 'x')
  plt.plot(disgust4, np.zeros_like(disgust4) + 1, 'x')
  plt.plot(fear4, np.zeros_like(fear4) + 2, 'x')
  plt.plot(joy4, np.zeros_like(joy4) + 3, 'x')
  plt.plot(sadness4, np.zeros_like(sadness4) + 4, 'x')
  plt.plot(analytical4, np.zeros_like(analytical4) + 5, 'x')
  plt.plot(confident4, np.zeros_like(confident4) + 6, 'x')
  plt.plot(tentative4, np.zeros_like(tentative4) + 7, 'x')
  plt.plot(openness4, np.zeros_like(openness4) + 8, 'x')
  plt.plot(conscientiousness4, np.zeros_like(conscientiousness4) + 9, 'x')
  plt.plot(extraversion4, np.zeros_like(extraversion4) + 10, 'x')
  plt.plot(agreeableness4, np.zeros_like(agreeableness4) + 11, 'x')
  plt.plot(emotional_range4, np.zeros_like(emotional_range4) + 12, 'x')

  print analytical
  print analytical1
  print analytical2
  print analytical3
  print analytical4

  plt.show()


for fn in os.listdir(SENTIMENT_DIR):
  src = fn.split('.')[0]
  aggregate_data(src)
plot_all_data()
