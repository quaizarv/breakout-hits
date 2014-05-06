#!/usr/bin/python

import sys
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
    for wc in range(1,5):
      if i + wc <= len(bodyWords):
        key = ' '.join(bodyWords[i:i+wc])
        if appNames.has_key(key):
          return appNames[key]

  normalizeBody = strip_punctuation(body.lower())
  bodyWords = re.split('\\s+', normalizeBody.strip())
  for i in range(len(bodyWords)):
    for wc in range(1,5):
      if i + wc <= len(bodyWords):
        key = ' '.join(bodyWords[i:i+wc])
        if appNames.has_key(key):
          return appNames[key]

  return ''

def search_urls(urlDescs, appNames):
  if urlDescs == '\N' or urlDescs == 'NULL':
    return ''
  try:
    urlDescList = ast.literal_eval(urlDescs)
  except SyntaxError:
    return ''
  except ValueError:
    return ''
  if not type(urlDescList) == list:
    return ''
  for urlDesc in urlDescList:
    url = urlDesc['expanded_url']
    items = re.split('[.:/\-_]', url)
    search_str = ' '.join(item for item in items if item not in ['', 'http', 'com'])
    appID = search_body(search_str, appNames)
    if appID != '':
      return appID
  return ''
  
def main():
  appNames = read_app_names("selected-apps.txt")
  count = 0
  total = 0
  for line in sys.stdin:
    total = total + 1
    items = line.strip().split('\t')
    if len(items) < 12:
      count = count + 1
      continue
    _, body, rC, fC, l, urls, src, foC, aFC, frC, pT, ID = items

    # search body
    appID = search_body(body, appNames)
    if  appID != '':
      print '\t'.join([appID, body, rC, fC, l, urls, src, foC, aFC, frC, pT, ID])
      continue

    # Check if name of the tweet source is an app's name
    if appNames.has_key(src.lower()):
      appID = appNames[src.lower()]
      print '\t'.join([appID, body, rC, fC, l, urls, src, foC, aFC, frC, pT, ID])
      continue;

    # search urls for app name
    appID = search_urls(urls, appNames)
    if appID != '':
      print '\t'.join([appID, body, rC, fC, l, urls, src, foC, aFC, frC, pT, ID])

  print '\t'.join(["0", "QuaizarV", "0" , "0", "en", "\N", "QuaizarV", str(count), str(total), "0", "0", "0"])

main()
