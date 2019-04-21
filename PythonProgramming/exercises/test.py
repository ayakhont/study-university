import urllib.request as urllib
import re


keyword = re.compile('schistosoma', re.IGNORECASE)
pmids = ['18235848', '22607149', '22405002', '21630672']


for pmid in pmids:
   url = "http://www.ncbi.nlm.nih.gov/pubmed?term=%s" % pmid
   handler = urllib.urlopen(url)
   html = handler.read()
   utf = html.decode('utf-8')
   title_regexp = re.compile("<h1>.{5,400}</h1>")
   match_t = title_regexp.search(utf)
   title = match_t.group()
   abstract_regexp = re.compile("<h3>Abstract</h3>.*<p>.{20,3000}</p></div>")
   match_ab = abstract_regexp.search(utf)
   abstract = match_ab.group()
   word = keyword.search(abstract)
   if word:
       print(title)
       print(word.group(), word.start(), word.end())