import numpy
import nltk
import string
import networkx
import httplib, urllib, base64
import json
from math import log10
from newspaper import Article
from summa.preprocessing.textcleaner import clean_text_by_sentences

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
					senGraph.add_edge(sen1, sen2, weight = similarityWeight)

def setGraphEdgeWeightsTFIDF(senGraph, senToken):
	for sen1 in senGraph.nodes():
   		for sen2 in senGraph.nodes():
			if sen1 != sen2 and not senGraph.has_edge(sen1, sen2):
				similarityWeight = idfModCos(senToken, sen1, sen2)
				if similarityWeight != 0:
					senGraph.add_edge(sen1, sen2, weight = similarityWeight)

def addScores(sentences, scores):
    for sentence in sentences:
        # Adds the score to the object if it has one.
        if sentence.token in scores:
            sentence.score = scores[sentence.token]
        else:
            sentence.score = 0

def extractSentences(url, length):
	origText = getArticleText(url).encode('utf-8')
	sentence = clean_text_by_sentences(origText, language="english")
	senToken = [sen.token for sen in sentence]
	senGraph = buildGraph(senToken)
	setGraphEdgeWeights(senGraph)
	senGraph.remove_nodes_from(networkx.isolates(senGraph))
	#nx.draw(senGraph)
	#plt.show()
	pageRank = networkx.pagerank(senGraph, weight='weight')
	addScores(sentence, pageRank)
	sentence.sort(key=lambda s: s.score, reverse=True)

	pulledSentence = sentence[:int(length)]
    # most important sentences in ascending order of importance
	pulledSentence.sort(key=lambda s: s.index)
	return "\n".join([sen.text for sen in pulledSentence])

def getArticleText(url):
	article = Article(url)
	article.download()
	article.html
	article.parse()
	return article.text

def getArticleTitle(url):
	article = Article(url)
	article.download()
	article.html
	article.parse()
	return article.title

def bingArticle(headline, altSite):
	headers = {'Ocp-Apim-Subscription-Key': '935c7077f70447cdb248c3f84e9695b8',}

	params = urllib.urlencode({
	    'q': headline + altSite,
	    'count': '1',
	    'offset': '0',
	    'mkt': 'en-us',
	})

	conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
	conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
	response = conn.getresponse()
	data = json.loads(response.read())
	url = data['webPages']['value'][0]['url']
	print url
	return url


