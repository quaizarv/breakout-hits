#!/usr/bin/python

import sys
import re
import string
import collections
import ujson
from datetime import datetime, date

def appsByTweetFreq(dataFile):
  freqMap = {}
  inp = open(dataFile, "r")
  for line in inp:
    items = line.strip().split('\t')
    appId, body, rC, fC, l, urls, src, foC, aFC, frC, pT, ID = items
    if freqMap.has_key(appId):
      freqMap[appId] = freqMap[appId] + 1
    else:
      freqMap[appId] = 1

  sorted_list = sorted([(freq, appId) for (appId, freq) in freqMap.items()])
  return sorted_list

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

stopWords = {w:1 for w in re.split(',', file('./stop-words.txt').read().strip())}

def word_basket(body):
  normalizeBody = strip_punctuation(body.lower())
  bodyWords = re.split('\\s+', normalizeBody.strip())
  bodyWords = [w for w in bodyWords if not stopWords.has_key(w)]
  return bodyWords

def parse_date(date_str):
  date_items = re.split('T', date_str)
  if (len(date_items) < 2):
    return None
  date_str = date_items[0]
  date_elems = re.split('-', date_str)
  if (len(date_elems) < 3):
    return None
  try:
    date = (int(date_elems[0]), int(date_elems[1]), int(date_elems[2]))
  except ValueError:
    return None
  return date

def date_filter_create(d1, d2):
 return (lambda date: date > d1 and date < d2)

appWords = ['game', 'app', 'games', 'puzzler', 'ios', 'android', 'iphone', 
            'ipad', 'itunes', 'phone', 'appstore', 'mobile', 'free', 'play',
            '#games', '#app', '#ios', '#iosapp', '#iosgames',
            'download', 'google', 'puzzler', 'apple',
            'toucharcade', 'appadvice', 'gamemob', '148apps', 'cultofmac',
            'maclife', 'eurogamer', 'pocketgamer', 'joystiq', 'puzzleretreat',
            'dippler', 'techcrunch', 'technologyreview', 'ustwo', 'ustwogames']
moreWords = ['score', 'scored', 'addicted', 'numbers', 'puzzle', 'beat', 'points']
appUrls = {w:0 for w in appWords}

def read_app_names(appDataFile):
  appNames = {}
  #urlAppName = {}
  input = open(appDataFile, "r")
  for line in input:
    items = re.split('\t', line.strip())
    appName = ' '.join(re.split('\\s+', items[0]))
    appName = appName.lower()
    #urlAppNames[appName] = items[1]
    normalizedName = strip_punctuation(appName)
    #if (normalizedName != appName):
      #urlAppNames[normalizedName] = items[1]
    hashtag1 = ''.join(re.split('\\s+', normalizedName))
    appNames[hashtag1] = items[1]
    hashtag2 = hashtag1 + 'game'
    appNames[hashtag2] = items[1]
    hashtag3 = hashtag1 + 'app'
    appNames[hashtag3] = items[1]
  return appNames



def search_body(body, names):
  lowerBody = body.lower()
  bodyWords = re.split('\\s+', lowerBody.strip())
  for i in range(len(bodyWords)):
    for wc in range(1,2):
      if i + wc <= len(bodyWords):
        key = ' '.join(bodyWords[i:i+wc])
        if names.has_key(key):
          return key

  normalizeBody = strip_punctuation(body.lower())
  bodyWords = re.split('\\s+', normalizeBody.strip())
  for i in range(len(bodyWords)):
    for wc in range(1,2):
      if i + wc <= len(bodyWords):
        key = ' '.join(bodyWords[i:i+wc])
        if names.has_key(key):
          return key

  return ''

def search_urls(urls):
  if urls == "\N":
    return ''
  try:
    urlDescs = ujson.loads(urls)
  except ValueError:
    print urls
    return ''
  for urlDesc in urlDescs:
    url = urlDesc['expanded_url']
    items = re.split('[.:/\-_]', url)
    search_str = ' '.join(item for item in items if item not in ['', 'http', 'com'])
    key = search_body(search_str, appUrls)
    if key != '':
      return ".".join(re.split('\s', key))
  return ''
  

#TBD: look at tweet src
#TBD: look for publisher-id in tweets, src & expanded-urls
def buildWordBasketsByApp(dataFile):
  appNames = read_app_names('selected-apps.txt')
  appWordStats = {w:0 for w in appWords}
  appTweetCount = 0
  wordBasketsByApp = {}
  inp = open(dataFile, "r")
  for line in inp:
    items = line.strip().split('\t')
    appId, body, rC, fC, l, urls, src, foC, aFC, frC, pT, ID = items

    if pT =='\N':
      continue
    try:
      dt = datetime.strptime(pT, '%Y-%m-%dT%H:%M:%S.000Z')
      dt = datetime.date(dt)
    except:
      continue

    b = word_basket(body)
    urlWord = search_urls(urls)
    if urlWord:
      b += [urlWord]
    if not b:
      continue

    isAppTweet = 0
    for w in b:
      if appWordStats.has_key(w):
        appWordStats[w] +=1
        isAppTweet = 1

    if appNames.has_key(w):
        isAppTweet = 1

    if isAppTweet:
      appTweetCount +=1

    if wordBasketsByApp.has_key(appId):
      #print appId, wordBasketsByApp[appId]
      wordBasketsByApp[appId].append((dt, b, isAppTweet))
    else:
      wordBasketsByApp[appId] = [(dt, b, isAppTweet)]


  inp.close()
  return wordBasketsByApp, appWordStats, appTweetCount


# generate tuples of a given size from a list of items
def generate_tuples (size, items):
  if size > len(items): return []
  if size == 0: return [()]
  return (map(lambda tup: (items[0], ) + tup, generate_tuples(size-1, items[1:])) + 
          generate_tuples(size, items[1:]))

# Apriori algorithm - find all frequent (k+1)-tuples given frequent k-tuples and
# frequent Single items
def apriori_k_plus_1(k_plus_1, wordBaskets, freq_k_tuples,
                     freq_items, threshold, date_filter):
  freq_table = {}
  for d, b, _ in wordBaskets:
    if not date_filter(d):
      continue
    b = sorted(b)
    kp1_tuples = generate_tuples(k_plus_1, b)
    for kp1_tuple in kp1_tuples:
      if (k_plus_1 == 1 or ((kp1_tuple[0],) in freq_items and kp1_tuple[1:] in freq_k_tuples)):
        if (kp1_tuple in freq_table):
          freq_table[kp1_tuple] = freq_table[kp1_tuple] + 1
        else:
          freq_table[kp1_tuple] = 1
  return dict([elem for elem in freq_table.items() if (elem[1] >= threshold)])

def findTopWords(wordBasketsByApp):
  df1 = date_filter_create(date(2014, 2, 27), date(2014, 2, 28))
  topWords = {}
  for appId in wordBasketsByApp.keys():
    topWords[appId] = apriori_k_plus_1(1, wordBasketsByApp[appId], {}, {}, 5, df1)

  topBiGrams = {}
  for appId in wordBasketsByApp.keys():
    topBiGrams[appId] = apriori_k_plus_1(2, wordBasketsByApp[appId], 
                                         topWords[appId], topWords[appId], 5, df1)

  freqTW1 = collections.defaultdict(lambda: 0)
  for appId in wordBasketsByApp.keys():
    topK = min(50, len(topWords))
    for f, w in topTuples(topWords[appId])[:topK]:
      freqTW1[w[0]] += 1

  df2 = date_filter_create(date(2014, 2, 28), date(2014, 3, 15))
  topWords = {}
  for appId in wordBasketsByApp.keys():
    topWords[appId] = apriori_k_plus_1(1, wordBasketsByApp[appId], {}, {}, 1, df2)

  freqTW2 = collections.defaultdict(lambda: 0)
  for appId in wordBasketsByApp.keys():
    topK = min(50, len(topWords))
    for f, w in topTuples(topWords[appId])[:topK]:
      freqTW2[w[0]] += f

  return freqTW1, freqTW2
    

def topTuples(topTupleDict):
  top = sorted([(f, w) for w, f in topTupleDict.items()])
  top.reverse()
  return top

# df1 and df2 are date filter functions (generated using date_filter_create()
# above
def cmp_co_words_by_date(appId, wBBA, df1, df2):
  if type(appId) == int:
    appId = str(appId)
  top1 = apriori_k_plus_1(1, wBBA[appId], {}, {}, 1, df1)
  top2 = apriori_k_plus_1(1, wBBA[appId], {}, {}, 5, df2)
  return zip(topTuples(top1)[:20], topTuples(top2)[:20])

#boDates = [(id, bod.date()) for id, (_, _, _, bod, _) in aggrCbr.items()]

def cmp_co_words(wBBA, appBODates):
  result = {}
  startDate = date(2014, 2, 28)
  for appId, boDate in appBODates:
    if not wBBA.has_key(str(appId)):
      continue
    if (boDate - startDate).days < 8:
      continue
    midDate = startDate + (boDate - startDate)/2
    df1 = date_filter_create(date(2014, 2, 28), midDate)
    df2 = date_filter_create(midDate, boDate)
    result[appId] = cmp_co_words_by_date(str(appId), wBBA, df1, df2)
  return result

def app_tweet_graph(wordBasketsByApp, appId, app_specific):
  if type(appId) == int:
    appId = str(appId)
  appTweets = wordBasketsByApp[appId]
  twByDay = [(d.date(), isApp) for d, _, isApp in appTweets]
  app_gr = collections.defaultdict(lambda: 0)
  for d, isApp in twByDay:
    if not app_specific or isApp:
      app_gr[d] += 1
  return sorted(app_gr.items())
