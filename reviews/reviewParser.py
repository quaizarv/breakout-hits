from os import listdir
from os.path import isfile, join
import re
import xml.etree.ElementTree as ET
from datetime import datetime, date
import itertools as IT

trainDataPath = '/Users/qv/breakout-hits/train-data/'
rvwDataPath = '/Users/qv/breakout-hits/macappstore/all-reviews/'
top25ByCatPath = '/Users/qv/breakout-hits/macappstore/top25-by-cat/'

def corpus(path): 
  return [join(path, f)
          for f in listdir(path)
          if isfile(join(path, f))]

def parse_app_reviews(reviewFile):
  tree = ET.parse(reviewFile)
  root = tree.getroot()

  appRvws = {}
  appRvwAttrs = {}
  appId, name = root.attrib.values()
  if root.getchildren() == []:
    return 0, None
  appRvws['id'] = int(appId)
  appRvws['name'] = name
  store = root.getchildren()[0]
  countryOfRvw = store.attrib.values()[0]
  appRvws['country'] = countryOfRvw

  rvwsXML = store.getchildren()
  rvws = {}
  appRvws['reviews'] = rvws
  for rvwXML in rvwsXML:
    rvwId = int(rvwXML.attrib['id'])
    rvw = {}
    rvw['title'] = rvwXML[0].text
    rvw['reviewer'] = rvwXML[1].text
    rvw['rating'] = int(rvwXML[2].text)
    rvw['version'] = rvwXML[3].text
    rvw['date'] = datetime.strptime(rvwXML[4].text, '%b %d, %Y').date()
    rvw['body'] = rvwXML[5].text
    rvws[rvwId] = rvw

  return int(appId), appRvws

def parse_app_reviews_all_apps(path):
  allAppRvws = {}
  for f in corpus(path):
    appId, appRvws = parse_app_reviews(f)
    if appRvws == None:
      continue
    allAppRvws[appId] = appRvws
  return allAppRvws

def runningAvgRating(ratingsByDate):
  cum_rating = 0.0
  num_ratings = 0.0
  runningAvgRating = []
  for dt, g in IT.groupby(ratingsByDate, key = lambda x: x[0]):
    ratings = [int(r[1]) for r in list(g)]
    cum_rating += sum([r for r in ratings])
    num_ratings += len(ratings)
    runningAvgRating.append((dt, cum_rating/num_ratings))
  return runningAvgRating

def insert_missing_dates(dateValueList, usePrevVal = False, default = 0):
  prev, prevVal = dateValueList[0]
  result = [(prev, prevVal)]
  for  dt, val in dateValueList[1:]:
    while (dt - prev).days > 1:
      prev = date.fromordinal(prev.toordinal() + 1)
      if usePrevVal:
        result.append((prev, prevVal))
      else:
        result.append((prev, default))
    result.append((dt, val))
    prev, prevVal = dt, val
  return result
    

def app_review_stats(appRvws):
  ratingsByDate = sorted([(r['date'], r['rating'])
                          for r in appRvws['reviews'].values()])
  
  # # of reviews/day
  rvwsPerDay = [(dt, len(list(g)))
                for dt, g in IT.groupby(ratingsByDate, key = lambda x: x[0])]

  rvwsPerDay = insert_missing_dates(rvwsPerDay)
    
  # sum-of-ratings-across-all-reviews/day for the first few days
  ratingVolPerDay = [(dt, sum([int(r[1]) for r in list(g)]))
                     for dt, g in IT.groupby(ratingsByDate, 
                                             key = lambda x: x[0])]

  ratingVolPerDay = insert_missing_dates(ratingVolPerDay)
    

  #TBD: avg sentiment on first few  days

  # running average rating/day
  return rvwsPerDay, ratingVolPerDay,  insert_missing_dates(
    runningAvgRating(ratingsByDate), True)


def read_app_names_and_bo_dates():
  appNames = {}
  boDatesAll = {}
  for line in file(trainDataPath + 'breakout-dates.txt'):
    name, appId, dateStr = re.split("\t", line.strip())
    appId = int(appId)
    appNames[appId] = name
    boDatesAll[appId] = datetime.strptime(dateStr, '%Y-%m-%d').date()
  return appNames, boDatesAll

appNames, boDatesAll = read_app_names_and_bo_dates()

def write_review_stats(allAppRvws, appList, fileName):
  f = open(trainDataPath + fileName, 'w')
  for a in appList:
    line = appNames[a] + ', '
    line += str(a) + ', '
    if a not in allAppRvws.keys():
      line += str(boDatesAll[a]) + '\n'
    else:
      rpd, vpd, rar = app_review_stats(allAppRvws[a])
      line += str(boDatesAll[a]) + ', ' + str(rpd[0][0]) + ', '
      line += " ".join([str(i) for dt, i in rpd]) + ', '
      line += " ".join([str(i) for dt, i in vpd]) + ', ' 
      line += " ".join(["%1.1f"%i for dt, i in rar]) + '\n'
    f.write(line)
  f.close()
    
def read_selected_apps(appFile):
  return [int(re.split("\t", line.strip())[1]) for line in file(appFile)]

def main():
  cbr = read_selected_apps(trainDataPath + 'cbr-clean.txt')
  fizz = read_selected_apps(trainDataPath + 'fizz-clean.txt')
  zb = read_selected_apps(trainDataPath + 'zb-clean.txt')

  allAppRvws = parse_app_reviews_all_apps(rvwDataPath)
  write_review_stats(allAppRvws, cbr, 'cbr-rvw-stats.csv')
  write_review_stats(allAppRvws, fizz, 'fizz-rvw-stats.csv')
  write_review_stats(allAppRvws, zb, 'zb-rvw-stats.csv')

main()

def rvws_rate_by_cat():
  startRvwdate = date(2014, 2, 1)
  endRvwDate = date(2014, 5, 24)
  topCatApps = [re.split("\t", line.strip())
                for line in file(trainDataPath + 'cat-top25-apps.txt')]
  topCatApps = [(int(appId), int(cat)) for appId, cat in topCatApps]
  appCats = collections.defaultdict(lambda: [])
  for i, c in topCatApps:
    appCats[i].append(c)
  allAppRvws = parse_app_reviews_all_apps(top25ByCatPath)
  rvwsRate = collections.defaultdict(lambda: 0)
  for appId, appRvws in allAppRvws.items():
    rvws = filter(lambda r: r['date'] >= startRvwDate and 
                  r['date'] <= endRvwDate,
                  appRvws['reviews'].values())
    firstRvwDate = min([r['date'] for r in rvws])
    rate = len(rvws)/(endRvwdate - firstRvwDate).days
    for c in appCats[appId]:
      rvwsRate[c] += rate
  file(trainDataPath + "cat-rvws-rate.txt").write(
    "\n".join([str(c) + "\t" + rvwsRate[c] for c in rvwsRate,keys()]))


