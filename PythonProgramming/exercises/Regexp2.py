import urllib.request as urllib
import re

overall_author_regexp = re.compile('<div class=\"auths\">.*?</div>')
author_regexp = re.compile("<a href.*?>(.*?)</a>")

url = "https://www.ncbi.nlm.nih.gov/pubmed/29405081"
handler = urllib.urlopen(url)
text = str(handler.read())
author_block = overall_author_regexp.findall(text)
if author_block:
    authors = author_regexp.findall(author_block[0])
    print(authors)

