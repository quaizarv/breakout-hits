#!/usr/bin/python

import sys
import json
import unicodedata
import re
import string
import ast

punctuation_set = set(string.punctuation)
def strip_punctuation(name):
  words = re.split('\\s+', name)
  s = ''
  for word in words:
    if not word.isalnum():
      word = ''.join(ch for ch in word if ch not in punctuation_set)
    if s == '':
      s = word
    else:
      s += ' ' + word
  return s

def read_app_names(appDataFile):
  appNames = {}
  input = open(appDataFile, "r")
  for line in input:
    items = re.split('\t', line.strip())
    #if len(re.split('\\s+', items[0])) < 2:
    #  print items[0]
    appName = ' '.join(re.split('\\s+', items[0]))
    appName = appName.lower()
    appNames[appName] = items[1]
    normalizedName = strip_punctuation(appName)
    if (normalizedName != appName):
      appNames[normalizedName] = items[1]
    hashtag1 = ''.join(re.split('\\s+', normalizedName))
    appNames[hashtag1] = items[1]
    appNames['#' + hashtag1] = items[1]
    hashtag2 = hashtag1 + 'game'
    appNames[hashtag2] = items[1]
    appNames['#' + hashtag2] = items[1]
    hashtag3 = hashtag1 + 'app'
    appNames[hashtag3] = items[1]
    appNames['#' + hashtag3] = items[1]
    #TBD: should we create hashtags with punctuations
    appNames['#app'] = "1111"
    appNames['#games'] = "1111"
    appNames['#ios'] = "1111"
    appNames['#iosapp'] = "1111"
    appNames['#iosgames'] = "1111"
  return appNames


def read_pub_names():
  pubNames = {}
  input = open("selected-pubs.txt", "r")
  for line in input:
    items = re.split('\t', line.strip())
    name = ' '.join(re.split('\\s+', items[0]))
    name = name.lower()
    pubNames[name] = items[1]
    normalizedName = strip_punctuation(name)
    pubNames[normalizedName] = items[1]
    words = re.split('\\s+', normalizedName)
    if len(words) >= 2:
      pubNames[words[0]] = items[1]
      if len(words) > 2:
        pubNames[words[0] + ' ' + words[1]] = items[1]
      
  return pubNames

def search_body(body, appNames):
  lowerBody = body.lower()
  bodyWords = re.split('\\s+', lowerBody.strip())
  for i in range(len(bodyWords)):
    for wc in range(1,6):
      if i + wc <= len(bodyWords):
        key = ' '.join(bodyWords[i:i+wc])
        if appNames.has_key(key):
          return appNames[key]

  normalizeBody = strip_punctuation(body.lower())
  bodyWords = re.split('\\s+', normalizeBody.strip())
  for i in range(len(bodyWords)):
    for wc in range(1,6):
      if i + wc <= len(bodyWords):
        key = ' '.join(bodyWords[i:i+wc])
        if appNames.has_key(key):
          return appNames[key]

  return ''

def search_urls(urlDescs, appNames):
  for urlDesc in urlDescs:
    url = urlDesc['expanded_url']
    items = re.split('[.:/\-_]', url)
    search_str = ' '.join(item for item in items if item not in ['', 'http', 'com'])
    appID = search_body(search_str, appNames)
    if appID != '':
      return appID
  return ''
  
def parse_json():
  appNames = read_app_names("selected-apps.txt")
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
      urls = None
      src = None

      # search body
      appID = search_body(body, appNames)
      if  appID == '':
        # Check if name of the tweet source is an app's name
        src = dstr['actor']['preferredUsername']
        if appNames.has_key(src.lower()):
          appID = appNames[src.lower()]
        # search urls for app name
        else:
          if (dstr.has_key('gnip')):
            if (dstr['gnip'].has_key('urls')):
              urls = dstr['gnip']['urls']
              appID = search_urls(urls, appNames)

      if appID == '':
        continue

      if src == None:
        src = dstr['actor']['preferredUsername']

      if urls == None:
        urls = '\N'
        if (dstr.has_key('gnip')):
          if (dstr['gnip'].has_key('urls')):
            urls = dstr['gnip']['urls']

    except KeyError:
      count = count + 1
      continue
    
    try:
      body = unicodedata.normalize('NFKD', body).encode('ascii','ignore')
      body = body.replace('\n', ' ')
      body = body.replace('\t', ' ')
      src = unicodedata.normalize('NFKD', src).encode('ascii','ignore')
      src = src.replace('\n', ' ')
      src = src.replace('\t', ' ')
      urls = str(urls).encode('ascii', 'ignore')
      #urls = unicodedata.normalize('NFKD', str(urls)).urls('ascii','ignore')
      #urls = urls.replace('\n', ' ')
      #urls = urls.replace('\t', ' ')
    except UnicodeEncodeError:
      count = count + 1
      continue

    try:
      rC = dstr['retweetCount']
      fC = dstr['favoritesCount']
      lang = 'en'
      if (dstr.has_key('gnip')):
        if (dstr['gnip'].has_key('language')):
          lang = dstr['gnip']['language']['value']
      foC = dstr['actor']['followersCount']
      aFC = dstr['actor']['favoritesCount']
      frC = dstr['actor']['friendsCount']
      pT = dstr['postedTime']
      ID = dstr['id']
    except KeyError:
      count = count + 1
      continue

    total = total + 1
    print '\t'.join([appID, body, str(rC), str(fC), lang, urls, src, str(foC), str(aFC), str(frC), pT, ID])

  print '\t'.join(["0", "QuaizarV", "0" , "0", "en", "\N", "QuaizarV", str(count), str(total), "0", "0", "0"])

def main():
  parse_json()

main()
