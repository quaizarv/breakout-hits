import re
import numpy as np
import random
from numpy.linalg import *
import string
import sys
import collections
from datetime import datetime, date
import ast

def searchable_name(name):
  exclude = set(string.punctuation)
  words = re.split('\\s+', name)
  for word in words:
    if not word.isalnum():
      stripped = ''.join(ch for ch in word if ch not in exclude)
      if not stripped.isalnum():
        return False
  return True

def name_smaller_than(name, num_words):
  words = re.split('\\s+', name)
  if (len(words) < num_words):
    return True
  return False

def books_news_cat(cat):
  if cat == 6006 or cat == 6009 or cat == 6018 or cat > 13000:
    return True
  return False

# keep only games
def filter_cat(cat):
  if not (cat == 6014 or cat >= 7000 and cat <= 7050):
    return True
  return False

def filter_country(co):
  if not (co == 'us'):
    return True
  return False

def filter_by_date_range(date, lower_date, upper_date):
  if not (date >= lower_date and date <= upper_date):
    return True
  return False

def filter_app_name(name):
  #return not searchable_name(name) or not name_smaller_than(name, 5)
  return not searchable_name(name)
        
def read_pub_data(pub_data_file):
  publishers = {}
  input = open(pub_data_file, "r")
  for line in input:
    items = re.split('\t', line)
    pub_id = int(items[0])
    name = items[1]
    if not searchable_name(name):
      continue;
    publishers[pub_id] = name
  return publishers

def read_app_data(app_data_file):
  apps = {}
  input = open(app_data_file, "r")
  for line in input:
    items = re.split('\t', line)

    app_name = items[1]

    app_id = int(items[0])
    price = float(items[2])
    currency = items[3]
    rel_date_str = items[4]
    pub_id = int(items[5])
    rel_date = datetime.strptime(rel_date_str, '%Y-%m-%d %H:%M:%S')

    if filter_by_date_range(rel_date, datetime(2014, 2, 1), 
                            datetime(2014, 7, 1)):
      continue

    apps[app_id] = (app_name, price, currency, pub_id, rel_date)

  return apps

def read_app_ranks(app_ranks_file, apps):
  app_ranks_dict = {}
  input = open(app_ranks_file, "r")
  for line in input:
    items = re.split('\t', line.strip())

    app_id = int(items[0])
    if (not apps.has_key(app_id)):
      continue
    categ = int(items[1])

    if books_news_cat(categ):
      continue

    feedId = int(items[3])
    country = items[4]

    rankList = [(datetime.strptime(d, '%Y-%m-%d'), v) for d, v in
                 ast.literal_eval(items[2]).items()]
    rankList.sort()

    #print (app_id, categ, country, rankList)
    if app_ranks_dict.has_key(app_id):
      l = app_ranks_dict[app_id]
    else:
      l = []
      app_ranks_dict[app_id] = l
    l.append((categ, feedId, country, rankList))
    #app_ranks.append((app_id, categ, country, rank_list))
    
  return app_ranks_dict

def filter_apps(apps, filterFunc):
  filteredApps = {}
  for appId, val in apps.items:
    if filterFunc(val):
      continue
    filteredApps[appId] = val
  return filteredApps

def filter_ranks(app_ranks, filterFunc):
  filteredAppRanks = {}
  for appId, attrList in app_ranks.items():
    filteredList = []
    for attrs in attrList:
      if filterFunc(attrs):
        continue
      filteredList += [attrs]
    if len(filteredList):
      filteredAppRanks[appId] = filteredList
  return filteredAppRanks

def filter_app_by_searchable_name(appAttrs):
  name, _, _, _, _ = appAttrs
  if not searchable_name(name):
    return True
  return False

def filter_app_rank1(attrs):
  cat, feed, co, rl = attrs
  if filter_cat(cat):
    return True
  if filter_country(co):
    return True
  return False

def max_breakout_dur(rankList, threshold):
  startDate = None
  maxDur = 0
  boStart = None
  end = False
  for date, rankVal in rankList:
    if rankVal <= threshold:
      if not startDate:
        startDate = date
    else:
      if startDate and maxDur <= (date - startDate).days:
        maxDur = (date - startDate).days
        boStart = startDate
      startDate = None

  endDate = datetime(2014, 4, 30)
  date = endDate
  if startDate and maxDur <= (date - startDate).days:
    maxDur = (date - startDate).days
    boStart = startDate
    end = True

  return maxDur, boStart, end

def non_breakout_dur(rankList, nb_threshold, relDate):
  end = False
  for date, rankVal in rankList:
    if rankVal < nb_threshold:
      break
  dur = (date - relDate).days
  return dur

def find_consistent_br(app_ranks, apps, filterParams):
  nb_thresh, nb_dur, br_thresh, br_dur, takeEnd = filterParams
  result = []
  for appId, attrList in app_ranks.items():
    for attrs in attrList:
      _, _, _, rankList = attrs
      initial_nb_dur = non_breakout_dur(rankList, nb_thresh, apps[appId][4])
      maxDur, boStart, end = max_breakout_dur(rankList, br_thresh)
      if (initial_nb_dur >= nb_dur and maxDur >= br_dur and
          (end or not takeEnd)):
        result.append((appId, apps[appId][4], maxDur, boStart, attrs))
  return result

def aggr_consistent_br(cbr):
  aggrCBR = {}
  for appId, relDate, maxDur, boStart, attrs in cbr:
    if not aggrCBR.has_key(appId) or boStart < aggrCBR[appId][3]:
      aggrCBR[appId] = (appId, relDate, maxDur, boStart, attrs)
  return aggrCBR


def fizzled(rankList, params):
  br_thresh = params[0]
  fizzled_thresh = params[1]
  br_found = False
  cumRank = 0.0
  fallDays = 0.0
  endDate = datetime(2014,4,30)
  for date, rankVal in rankList:
    if rankVal <= br_thresh:
      if (endDate - date).days <= 15:
        return False
      br_found = True
    if br_found and (endDate - date).days <= 15:
      cumRank += prevRankVal * (date - prevDate).days
      fallDays += (date - prevDate).days
    prevDate = date
    prevRankVal = rankVal
  if not br_found:
    return False
  cumRank += prevRankVal * (endDate - prevDate).days
  fallDays += (endDate - prevDate).days
  if fallDays >= 15 and cumRank/fallDays >= fizzled_thresh:
    return True
  return False

def zero_breakout(rankList, params):
  br_thresh = params[0]
  for date, rankVal in rankList:
    if rankVal <= br_thresh:
      return False
  return True

def match_apps(app_ranks, apps, matchFunc, matchParam, matchAll):
  result = []
  for appId, attrList in app_ranks.items():
    for attrs in attrList:
      _, _, _, rankList = attrs
      matched = matchFunc(rankList, matchParam)
      if (matchAll and not matched) or (not matchAll and matched):
        break
    if matched:
      result.append(appId)
  return result
    

abrevFeedTypes = {'topPaidIpadApplications' : 'pi',
                  'topFreeIpadApplications' : 'fi',
                  'topPaidApplications'     : 'pa',
                  'topFreeApplications'     : 'fa',
                  'topApplications'         : 'ta'
                  }
  
def read_feeds(feeds_file):
  feeds = {}
  for line in file(feeds_file):
    feedId, feedTypeStr, cat, _ = re.split("\t", line.strip())
    feeds[int(feedId)] = (abrevFeedTypes[feedTypeStr], cat)
  return feeds
