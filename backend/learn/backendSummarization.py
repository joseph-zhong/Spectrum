import urllib

import numpy
import nltk
import string
import networkx
import httplib, urllib, base64
import json
from math import log10
import newspaper
from newspaper import Article
from summa.preprocessing.textcleaner import clean_text_by_sentences

global article


def sentSimilar(sen1, sen2):
  sen1Words = sen1.split()
  sen2Words = sen2.split()
  numCommonWords = len(set(sen1Words) & set(sen2Words))
  sen1Log = log10(len(sen1Words))
  sen2Log = log10(len(sen2Words))
  if sen1Log + sen2Log == 0:
    return 0
  return numCommonWords / (sen1Log + sen2Log)


def buildGraph(senToken):
  graph = networkx.Graph()
  for sentence in senToken:
    if not graph.has_node(sentence):
      graph.add_node(sentence)
  return graph


def setGraphEdgeWeights(senGraph):
  for sen1 in senGraph.nodes():
    for sen2 in senGraph.nodes():
      if sen1 != sen2 and not senGraph.has_edge(sen1, sen2):
        similarityWeight = sentSimilar(sen1, sen2)
        if similarityWeight != 0:
          senGraph.add_edge(sen1, sen2, weight=similarityWeight)

#
# def setGraphEdgeWeightsTFIDF(senGraph, senToken):
#   for sen1 in senGraph.nodes():
#     for sen2 in senGraph.nodes():
#       if sen1 != sen2 and not senGraph.has_edge(sen1, sen2):
#         similarityWeight = idfModCos(senToken, sen1, sen2)
#         if similarityWeight != 0:
#           senGraph.add_edge(sen1, sen2, weight=similarityWeight)


def addScores(sentences, scores):
  for sentence in sentences:
    # Adds the score to the object if it has one.
    if sentence.token in scores:
      sentence.score = scores[sentence.token]
    else:
      sentence.score = 0


def extractSentences(url, length=2):
  # global article
  print 'extracting %s' % url
  paper = newspaper.build(url)
  article = Article(url)
  article.download()
  article.parse()
  print article

  origText = article.text.encode('utf-8')
  # print origText

  #### todo: something is wrong here
  ## fixme fixme fixme
  ####

  print 'before clean_text'

  sentence = clean_text_by_sentences(origText, language='english')
  # print sentence

  print 'before senToken'

  senToken = [sen.token for sen in sentence]
  print 'before senGraph'
  senGraph = buildGraph(senToken)
  print 'before setGraphWeights'
  setGraphEdgeWeights(senGraph)
  print 'before remove_nodes_from'
  senGraph.remove_nodes_from(networkx.isolates(senGraph))
  # nx.draw(senGraph)
  # plt.show()
  print 'before pageRank'
  pageRank = networkx.pagerank(senGraph, weight='weight')
  print 'before addScores'
  addScores(sentence, pageRank)
  print 'before sort'
  sentence.sort(key=lambda s: s.score, reverse=True)

  print 'sentence'
  pulledSentence = sentence[:int(length)]
  # most important sentences in ascending order of importance
  pulledSentence.sort(key=lambda s: s.index)
  return '\n'.join([sen.text for sen in pulledSentence]), origText, article.title, paper.brand, article.keywords




def bingArticle(headline, source, count='2'):
  print '[bing article]'
  headers = {'Ocp-Apim-Subscription-Key': '935c7077f70447cdb248c3f84e9695b8', }

  params = urllib.urlencode({
    'q': '%s -site:%s' % (headline, source),
    'count': count,
    'offset': '0',
    'mkt': 'en-us',
  })

  conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
  conn.request('GET', '/bing/v5.0/search?%s' % params, '{body}', headers)
  response = conn.getresponse()
  data = json.loads(response.read())
  # url = data['webPages']['value'][0]['url']

  print data
  return data, count

# bingArticle(' Trump administration sanctions Iran on missile test', 'washingtonpost.com')