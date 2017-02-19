import os

import newspaper

NEWS_SOURCES = [
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
  'http://www.Reuters',
  'http://www.CNN.com',
  'http://www.TheWallStreetJournal.com',
  'http://www.TheEconomist.com',
  'http://www.TheFiscal Times.com',
  'http://www.TheHill.com',
  'http://www.FoxNews.com',
  'http://www.RedState.com',
  'http://www.theblaze.com'

]

OUT = 'out'
LINKS = 'links'
CORPUS = 'corpus'

for source in NEWS_SOURCES:
  fn = os.path.join(OUT, source.split('.')[1] + CORPUS)
  print 'filename: %s' % fn
  with open(fn, 'a+') as corpus_file:
    paper = newspaper.build(source)
    num_articles = len(paper.articles)
    print 'len: %d ' % num_articles
    count = 0
    try:
      for article in paper.articles:
        print 'article.url: %s' % article.url
        article.download()
        article.parse()
        txt = article.text
        # print txt
        corpus_file.write(txt.encode('utf8'))
        count += 1
        print 'success: %d out of %d' % (count, num_articles)
    except Exception as e:
      print 'ERROR %s ' % e
