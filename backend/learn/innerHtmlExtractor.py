import os
import urllib
import newspaper

import html2text

OUT = 'out'
LINKS = 'links'
CORPUS = 'corpus'

CONTENT_TAGS = {
  'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
  'p', 'span'
}

# import re, urlparse
#
# def urlEncodeNonAscii(b):
#     return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)
#
# def iriToUri(iri):
#     parts= urlparse.urlparse(iri)
#     return urlparse.urlunparse(
#         part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
#         for parti, part in enumerate(parts)
#     )


def create_corpus(links_filename):
  print 'create_corpus: %s' % links_filename
  with open (links_filename, 'r') as links_file:
    with open (links_filename.replace(LINKS, CORPUS), 'a+') as corpus_file:
      for url in links_file:
        print url
        # html = urllib.urlopen(url).read()
        # print html

        # text = html2text.html2text(html)
        newspaper.build(url)
        

        corpus_file.write(text)

for fn in {fn for fn in os.listdir(OUT) if LINKS in fn}:
  print fn
  create_corpus(os.path.join(OUT, fn))
