import numpy as np
import matplotlib.pyplot as pp
import os
import json

data_file = open('./non_confused.json', 'r')
str = ""
for line in data_file:
  str += line

  # print d
d = json.loads(str)
print d

sadness = []
neutral = []
contempt = []
disgust = []
anger = []
surprise = []
fear = []
happiness = []

val = 0. # this is the value where you want the data to appear on the y-axis.
for obj in d:
  sadness.append(obj['scores']['sadness'])
  neutral.append(obj['scores']['neutral'])
  contempt.append(obj['scores']['contempt'])
  disgust.append(obj['scores']['disgust'])
  anger.append(obj['scores']['anger'])
  surprise.append(obj['scores']['surprise'])
  fear.append(obj['scores']['fear'])
  happiness.append(obj['scores']['happiness'])

pp.plot(sadness, np.zeros_like(sadness) + val, 'x')
pp.plot(neutral, np.zeros_like(neutral) + 1, 'x')
pp.plot(contempt, np.zeros_like(contempt) + 2, 'x')
pp.plot(disgust, np.zeros_like(disgust) + 3, 'x')
pp.plot(anger, np.zeros_like(anger) + 4, 'x')
pp.plot(surprise, np.zeros_like(surprise) + 5, 'x')
pp.plot(fear, np.zeros_like(fear) + 6, 'x')
pp.plot(happiness, np.zeros_like(happiness) + 7, 'x')

pp.show()