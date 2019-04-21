import urllib.request as urllib
import re

pmids = ['18235848', '22607149', '22405002', '21630672']
keyword_regexp = re.compile('schistosoma', re.IGNORECASE)
title_regexp = re.compile("<h1>(.*?)</h1>")
abstract_regexp = re.compile("<h3>Abstract</h3>.*?</p></div>")

for pmid in pmids:
   url = "http://www.ncbi.nlm.nih.gov/pubmed?term=%s" % pmid
   handler = urllib.urlopen(url)
   utf = str(handler.read())

   match_t = title_regexp.search(utf)
   title = match_t.group(1)
   match_ab = abstract_regexp.search(utf)
   abstract = match_ab.group()
   word = keyword_regexp.search(abstract)
   if word:
      print(title)
      print(word.group(), word.start(), word.end())
