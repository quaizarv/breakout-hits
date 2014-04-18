#!/usr/bin/python

import sys
import re
import string

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

def read_app_names():
  appNames = {}
  input = open("selected-apps.txt", "r")
  for line in input:
    items = re.split('\t', line.strip())
    appName = ' '.join(re.split('\\s+', items[0]))
    appName.lower()
    appNames[appName] = items[1]
    normalizedName = strip_punctuation(appName)
    appNames[normalizedName] = items[1]
    hashtag1 = ''.join(re.split('\\s+', normalizedName))
    appNames[hashtag1] = items[1]
    hashtag2 = hastag1 + 'game'
    appNames[hashtag2] = items[1]
    hashtag3 = hastag1 + 'app'
    appNames[hashtag3] = items[1]
    #TBD: should we create hashtags with punctuations
  return appNames

def read_pub_names():
  pubNames = {}
  input = open("selected-pubs.txt", "r")
  for line in input:
    items = re.split('\t', line.strip())
    name = ' '.join(re.split('\\s+', items[0]))
    name.lower()
    pubNames[name] = items[1]
    normalizedName = strip_punctuation(name)
    pubNames[normalizedName] = items[1]
    words = re.split('\\s+', normalizedName)
    if len(words) >= 2:
      pubNames[words[0]] = items[1]
      if len(words) > 2:
        pubNames[words[0] + ' ' + words[1]] = items[1]
      
  return pubNames

def main():
  count = 0
  total = 0
  for line in sys.stdin:
    total = total + 1
    items = line.strip().split('\t')
    if len(items) < 6:
      count = count + 1
      continue
    body, rC, l, c , foC, frC = items
    words = re.split('\\s+', body.strip())
    for i in range(len(words)-1):
      if gameNames.has_key(words[i] + ' ' + words[i+1]):
        print '\t'.join([body, rC, l, c, foC, frC])

  print '\t'.join(["QuaizarV", str(count) , "en", "QuaizarV", str(total), "0"])
