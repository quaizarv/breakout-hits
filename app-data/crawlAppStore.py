import re
import httplib
import ujson
import unicodedata

#"./selected/rel-after-20140131.txt"
def crawl_apps(appNamesFile):
  appIds = [line.strip() for line in file(appNamesFile)]
  conn = httplib.HTTPConnection("itunes.apple.com")
  count = 0
  for appId in appIds:
    conn.request('GET', '/lookup?id=' + appId)
    r1 = conn.getresponse()
    if r1.status == 200:
      data = r1.read()
      dstr = ujson.loads(data)
      print appId + '\t' + ujson.dumps(dstr)
    else:
      count = count + 1
    
  conn.close()
  print count

#crawl_apps()

def parse_date(dateTimeStr):
  dateStr, _ = re.split('T', dateTimeStr.strip())
  yr, mo, day = re.split('-', dateStr)
  return (int(yr), int(mo), int(day))

def parse_app_data(appDataFile):
  appInfo = [re.split('\\t', line.strip()) for line in file(appDataFile)]
  count = 0
  for appId, appJson in appInfo:
    dstr = ujson.loads(appJson)
    if not dstr['results'] or not dstr['results'][0].has_key("version"):
      count +=1
      continue
    version = dstr['results'][0]['version']
    version = unicodedata.normalize('NFKD', version).encode('ascii', 'ignore')
    version = re.split('[\.,vV]', version)
    version = [elem for elem in version if elem != '']
    try:
      major_ver = int(version[0])
    except ValueError:
      continue
    relDateStr = dstr['results'][0]['releaseDate']
    relDate = parse_date(relDateStr)
    if relDate >= (2014, 01, 01):
      print appId, '.'.join(version), re.split('T', relDateStr)[0],
      if dstr['results'][0].has_key("userRatingCount"):
        reviewsCount = dstr['results'][0]["userRatingCount"]
        print reviewsCount,
      if dstr['results'][0].has_key("averageUserRating"):
        rating = dstr['results'][0]["averageUserRating"]
        print rating,
      print
  print count

#parse_app_data()  




