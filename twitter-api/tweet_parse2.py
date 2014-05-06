#!/usr/bin/python

import sys
import json
import unicodedata

def parse_json():
  count = 0
  total = 0
  for line in sys.stdin:
    try:
      dstr = json.loads(line)
    except ValueError:
      count = count + 1
      continue

    try:
      if (dstr['verb'] == 'delete'):
        continue
      body = dstr['body']
      rC = dstr['retweetCount']
      fC = dstr['favoritesCount']
      if (dstr.has_key('gnip')):
        if (dstr['gnip'].has_key('language')):
          lang = dstr['gnip']['language']['value']
      urls = '\N'
      if (dstr.has_key('gnip')):
        if (dstr['gnip'].has_key('urls')):
          urls = dstr['gnip']['urls']
      src = dstr['actor']['preferredUsername']
      foC = dstr['actor']['followersCount']
      aFC = dstr['actor']['favoritesCount']
      frC = dstr['actor']['friendsCount']
      pT = dstr['postedTime']
      ID = dstr['id']
    except KeyError:
      count = count + 1
      continue
    
    try:
      body = unicodedata.normalize('NFKD', body).encode('ascii','ignore')
      src = unicodedata.normalize('NFKD', src).encode('ascii','ignore')
      urls = str(urls).encode('ascii', 'ignore')
    except UnicodeEncodeError:
      print "------>", lang
      count = count + 1
      continue

    total = total + 1
    print '\t'.join([body, str(rC), str(fC), lang, urls, src, str(foC), str(aFC), str(frC), pT, ID])

  print '\t'.join(["QuaizarV", "0" , "0", "en", "\N", "QuaizarV", str(count), str(total), "0", "0", "0"])

def main():
  parse_json()

main()
