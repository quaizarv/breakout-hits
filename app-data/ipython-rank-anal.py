# coding: utf-8

import parseRanks
from parseRanks import *
reload parseRanks
reload(parseRanks)
from parseRanks import *
apps = read_app_data('apps.txt)
apps = read_app_data('apps.txt')
len(apps)
app_ranks = read_app_ranks('ranks.txt')
app_ranks = read_app_ranks('ranks.txt', apps)
len(apps)
apps.keys()[:20
]
[apps[key] for key in apps.keys()[:20]]
apps[395245636]
str = 'Diabetes @Point of Care™'
str
unicodedata.normalize('NFKD', str)
import unicodedata
unicodedata.normalize('NFKD', str)
str
str = u'Diabetes @Point of Care™'
str
unicodedata.normalize('NFKD', str)
unicodedata.normalize('NFKD', str).encode(ascii, ignore)
unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
len(apps)
all_apps = all_app_list(apps, app_ranks)
len(all_apps)
released_in_date_range(all_apps, apps, (2014, 3, 1), (2014, 4, 30))
newest = released_in_date_range(all_apps, apps, (2014, 3, 1), (2014, 4, 30))
len(newest)
len(app_ranks)
len(apps)
len(app_ranks)/len(apps)
1.0 * len(app_ranks)/len(apps)
import httplib
conn = httplib.HTTPConnection('itunes.apple.com')
conn.request('GET', '/lookup?id=674653944')
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1
appIds = file("./selected/newest").read()
appIds
[re.split("\\s+", line.strip()) for line in file("./selected/newest")]
[re.split("\\t+", line.strip()) for line in file("./selected/newest")]
[re.split("\\s+", line.strip()) for line in file("./selected/newest")]
[re.split("\\s+", line.strip())[1] for line in file("./selected/newest")]
[re.split("\\t+", line.strip())[1] for line in file("./selected/newest")]
[re.split("\\t", line.strip())[1] for line in file("./selected/newest")]
r1.read()
r1 = conn.getresponse()
conn.request('GET', '/lookup?id=674653944')
r1 = conn.getresponse()
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print r2.status, r2.reason
404 Not Found
data2 = r2.read()
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print r2.status, r2.reason
404 Not Found
data2 = r2.read()
conn = httplib.HTTPConnection("itunes.apple.com")
conn.request('GET', '/lookup?id=674653944')
r1 = conn.getresponse()
data = r1.read()
data
import ujson
dstr = ujson.loads(data)
dstr
appIds = [re.split("\\t", line.strip())[1] for line in file("./selected/newest")]
appIds
conn.close()
conn = httplib.HTTPConnection("itunes.apple.com")
conn.request('GET', '/lookup?id=' + appIds[0])
r1 = conn.getresponse()
data = r1.read()
data
r1.status
import crawlAppStore
from crawlAppStore import *
len(appIds)
data
dstr = ujson.loads(data)
dstr
dstr
data
data.strip()
print data.strip()
dstr = ujson.loads(data)
dstr
ujson.dumps(dstr)
newest
newest[0]
apps[newest[0][0]]
appIds
appIds[0]
apps[appIds[0]]
apps[int(appIds[0])]
len(newest)
print newest \> junk
print newest \> 'junk.txt'
print newest > 'junk.txt'
get_ipython().magic(u'pwd ')
get_ipython().magic(u"store newest 'junk.txt'")
newest
get_ipython().magic(u"save 'junk.txt' 108")
file('junk.txt).write(newest)
file('junk.txt).write(str(newest))
str1 = str(newest)
newest
str1 = newest.__str__()
str1
file("junk.txt").write(newest.__str__())
file("./junk.txt", 'w').write(newest.__str__())
newest
data
dstr
dstr['version']
dstr['results]['version']
dstr['results']
dstr['results'][0]['version']
int(dstr['results'][0]['version'])
flost(dstr['results'][0]['version'])
float(dstr['results'][0]['version'])
float(dstr['results'][0]['version'])
unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
str = dstr['results'][0]['version']
str
unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
unicodedata.normalize('NFKD', str)
dstr['results'][0]
dstr['results'][0]['release_date']
dstr['results'][0]['releaseDate']
dstr['results'][0]['userRatings']
str = '{"resultCount":1,"results":[{"contentAdvisoryRating":"4+","features":["gameCenter","iosUniversal"],"ipadScreenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d2\/03\/a3\/d203a3e4-f1b5-2511-39ae-dcb232a99f00\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c7\/ca\/c1\/c7cac12d-b741-2eea-d747-ddf79c122bc4\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c3\/0e\/b4\/c30eb42b-a6bb-e54a-2c6c-2f0f2c4cd1ee\/screen480x480.jpeg"],"averageUserRatingForCurrentVersion":4.5,"releaseDate":"2014-03-14T22:42:22Z","currency":"USD","artistId":365530479,"userRatingCountForCurrentVersion":35,"description":"He's strong to do travel to a lifetime.\nBut he's tired at times.\nSO Please help his long distance trip.\nJust tap the touch screen to flap the little wings and avoid pesticide poles.\n\n- Easy one touch control\n- Moving colorful poles.\n- 8-bit pixel retro graphics.\n- Easier than Flappy Bird.","genres":["Games","Entertainment","Action","Adventure"],"trackId":492020793,"artworkUrl512":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","version":"1.0","primaryGenreId":6014,"primaryGenreName":"Games","bundleId":"com.Mighty.Mosquito","languageCodesISO2A":["EN"],"isGameCenterEnabled":true,"trackCensoredName":"Mighty Mosquito","genreIds":["6014","6016","7001","7002"],"trackName":"Mighty Mosquito","price":0.0,"sellerUrl":"http:\/\/youtu.be\/Wce3p9K-vEI","screenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/fa\/a5\/16\/faa51679-0f50-3aa8-b920-707cc78f5e31\/screen1136x1136.jpeg","http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/ff\/33\/69\/ff3369a5-1f59-68d1-1bed-ce94e1c6e7cc\/screen1136x1136.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d6\/7b\/66\/d67b662e-3369-d00a-6bce-b0608be55a9c\/screen1136x1136.jpeg"],"userRatingCount":35,"trackContentRating":"4+","trackViewUrl":"https:\/\/itunes.apple.com\/us\/app\/mighty-mosquito\/id492020793?mt=8&uo=4","formattedPrice":"Free","artistViewUrl":"https:\/\/itunes.apple.com\/us\/artist\/wiseit\/id365530479?uo=4","kind":"software","fileSizeBytes":"4467944","sellerName":"Wiseit","supportedDevices":["iPad23G","iPad3G","iPadMini4G","iPhone-3GS","iPodTouchThirdGen","iPodTouchFifthGen","iPhone5c","iPadThirdGen4G","iPadFourthGen","iPhone4","iPadMini","iPadFourthGen4G","iPadWifi","iPhone4S","iPadThirdGen","iPhone5","iPhone5s","iPodTouchourthGen","iPad2Wifi"],"artworkUrl100":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","artistName":"Wiseit","averageUserRating":4.5,"artworkUrl60":"http:\/\/a1733.phobos.apple.com\/us\/r30\/Purple\/v4\/fc\/14\/ce\/fc14ce2a-1aa2-9f8b-2ca6-83de554f02ba\/AppIcon57x57.png","wrapperType":"software"}]}'
str = '{"resultCount":1,"results":[{"contentAdvisoryRating":"4+","features":["gameCenter","iosUniversal"],"ipadScreenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d2\/03\/a3\/d203a3e4-f1b5-2511-39ae-dcb232a99f00\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c7\/ca\/c1\/c7cac12d-b741-2eea-d747-ddf79c122bc4\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c3\/0e\/b4\/c30eb42b-a6bb-e54a-2c6c-2f0f2c4cd1ee\/screen480x480.jpeg"],"averageUserRatingForCurrentVersion":4.5,"releaseDate":"2014-03-14T22:42:22Z","currency":"USD","artistId":365530479,"userRatingCountForCurrentVersion":35,"description":"He's strong to do travel to a lifetime.\nBut he's tired at times.\nSO Please help his long distance trip.\nJust tap the touch screen to flap the little wings and avoid pesticide poles.\n\n- Easy one touch control\n- Moving colorful poles.\n- 8-bit pixel retro graphics.\n- Easier than Flappy Bird.","genres":["Games","Entertainment","Action","Adventure"],"trackId":492020793,"artworkUrl512":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","version":"1.0","primaryGenreId":6014,"primaryGenreName":"Games","bundleId":"com.Mighty.Mosquito","languageCodesISO2A":["EN"],"isGameCenterEnabled":true,"trackCensoredName":"Mighty Mosquito","genreIds":["6014","6016","7001","7002"],"trackName":"Mighty Mosquito","price":0.0,"sellerUrl":"http:\/\/youtu.be\/Wce3p9K-vEI","screenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/fa\/a5\/16\/faa51679-0f50-3aa8-b920-707cc78f5e31\/screen1136x1136.jpeg","http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/ff\/33\/69\/ff3369a5-1f59-68d1-1bed-ce94e1c6e7cc\/screen1136x1136.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d6\/7b\/66\/d67b662e-3369-d00a-6bce-b0608be55a9c\/screen1136x1136.jpeg"],"userRatingCount":35,"trackContentRating":"4+","trackViewUrl":"https:\/\/itunes.apple.com\/us\/app\/mighty-mosquito\/id492020793?mt=8&uo=4","formattedPrice":"Free","artistViewUrl":"https:\/\/itunes.apple.com\/us\/artist\/wiseit\/id365530479?uo=4","kind":"software","fileSizeBytes":"4467944","sellerName":"Wiseit","supportedDevices":["iPad23G","iPad3G","iPadMini4G","iPhone-3GS","iPodTouchThirdGen","iPodTouchFifthGen","iPhone5c","iPadThirdGen4G","iPadFourthGen","iPhone4","iPadMini","iPadFourthGen4G","iPadWifi","iPhone4S","iPadThirdGen","iPhone5","iPhone5s","iPodTouchourthGen","iPad2Wifi"],"artworkUrl100":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","artistName":"Wiseit","averageUserRating":4.5,"artworkUrl60":"http:\/\/a1733.phobos.apple.com\/us\/r30\/Purple\/v4\/fc\/14\/ce\/fc14ce2a-1aa2-9f8b-2ca6-83de554f02ba\/AppIcon57x57.png","wrapperType":"software"}]}'
str = '{"resultCount":1,"results":[{"contentAdvisoryRating":"17+","features":["iosUniversal"],"ipadScreenshotUrls":["http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/fc\/39\/1a\/fc391a75-c97c-beaf-2242-de477413be69\/screen480x480.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/eb\/5c\/6c\/eb5c6c39-7c4e-fdb3-87e1-67b7beeb6d86\/screen480x480.jpeg","http:\/\/a5.mzstatic.com\/us\/r30\/Purple\/v4\/fb\/36\/33\/fb363359-b408-f941-6513-be2f004b40c6\/screen480x480.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d9\/32\/37\/d93237da-a9c4-708c-8173-60b28caab443\/screen480x480.jpeg","http:\/\/a1.mzstatic.com\/us\/r30\/Purple\/v4\/da\/7d\/90\/da7d904f-6cc9-d7a0-84a3-cfd42cadaa2d\/screen480x480.jpeg"],"releaseDate":"2014-03-29T16:14:36Z","currency":"USD","artistId":335127887,"description":"Cougar Dating - #1 cougar personals community!\n\nCougar Dating is the No.1 cougar dating site for older women and younger men looking for fun and love around the world.\nThe Cougar Dating App provides customized cougar dating features.\n- Cougar searches\n- Verified Photo \/ Age \/ Education\n- Check emails and winks from other members\n- View who is interested in me, winked at me and viewed me.\nAnd more!\n\nWe have multiple subscription options to choose from - starting as low as $33.99\/month:\nYour iTunes account will be charged at confirmation of your purchase and auto-renews for the same upgrade price at the end of one-month period.\nAuto-renew may be turned off by going to your Account Settings after purchase and must be turned off at least 24-hours before the end of the current period.\nNo cancellation of the current upgrade plan is allowed during your active period.\n\nOther things you need to know:\nYou can view our Privacy Policy at http:\/\/www.olderwomendating.com\/privacy_policy_\nYou can view our Service Agreement at http:\/\/www.olderwomendating.com\/service_agreement\nYou must be at least 18 years old to download and use this app","genres":["Social Networking","Entertainment"],"trackId":477091899,"artworkUrl512":"http:\/\/a826.phobos.apple.com\/us\/r30\/Purple\/f5\/84\/21\/mzl.tcyvfckv.png","version":"3.4","primaryGenreId":6005,"primaryGenreName":"Social Networking","bundleId":"com.successfulmatch.olderwomendating","languageCodesISO2A":["EN","DE"],"isGameCenterEnabled":false,"trackCensoredName":"Date Cougar","genreIds":["6005","6016"],"trackName":"Date Cougar","price":0.0,"sellerUrl":"http:\/\/www.successfulmatch.com","screenshotUrls":["http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/db\/bd\/3d\/dbbd3d48-5137-1955-2968-93bacd0cf4b1\/screen1136x1136.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/ce\/35\/e6\/ce35e691-0e84-5643-3dd3-506b4c628455\/screen1136x1136.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/e8\/3a\/4a\/e83a4abd-e023-b60e-656f-301a656cbb2c\/screen1136x1136.jpeg","http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/e0\/27\/43\/e0274371-1043-710d-2f14-5cbf26d53992\/screen1136x1136.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/ed\/da\/ea\/eddaea63-a9b9-7aee-15a6-e24599f82b28\/screen1136x1136.jpeg"],"trackContentRating":"17+","trackViewUrl":"https:\/\/itunes.apple.com\/us\/app\/date-cougar\/id477091899?mt=8&uo=4","formattedPrice":"Free","artistViewUrl":"https:\/\/itunes.apple.com\/us\/artist\/successfulmatch.com\/id335127887?uo=4","kind":"software","fileSizeBytes":"24631093","sellerName":"SuccessfulMatch.com","supportedDevices":["iPhone-3GS","iPhone5s","iPadFourthGen4G","iPadMini","iPadThirdGen","iPhone5","iPodTouchFifthGen","iPhone5c","iPad23G","iPadFourthGen","iPhone4S","iPadMini4G","iPodTouchourthGen","iPadThirdGen4G","iPhone4","iPad2Wifi"],"artworkUrl100":"http:\/\/a826.phobos.apple.com\/us\/r30\/Purple\/f5\/84\/21\/mzl.tcyvfckv.png","artistName":"SuccessfulMatch.com","artworkUrl60":"http:\/\/a926.phobos.apple.com\/us\/r30\/Purple4\/v4\/f7\/49\/2e\/f7492ec5-d1b9-85bd-e0a5-b72e02509df3\/AppIcon57x57.png","wrapperType":"software"}]}'
str
dstr = ujson.loads(str)
dstr
str = '{"resultCount":1,"results":[{"contentAdvisoryRating":"17+","features":["iosUniversal"],"ipadScreenshotUrls":["http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/fc\/39\/1a\/fc391a75-c97c-beaf-2242-de477413be69\/screen480x480.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/eb\/5c\/6c\/eb5c6c39-7c4e-fdb3-87e1-67b7beeb6d86\/screen480x480.jpeg","http:\/\/a5.mzstatic.com\/us\/r30\/Purple\/v4\/fb\/36\/33\/fb363359-b408-f941-6513-be2f004b40c6\/screen480x480.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d9\/32\/37\/d93237da-a9c4-708c-8173-60b28caab443\/screen480x480.jpeg","http:\/\/a1.mzstatic.com\/us\/r30\/Purple\/v4\/da\/7d\/90\/da7d904f-6cc9-d7a0-84a3-cfd42cadaa2d\/screen480x480.jpeg"],"releaseDate":"2014-03-29T16:14:36Z","currency":"USD","artistId":335127887,"description":"Cougar Dating - #1 cougar personals community!\n\nCougar Dating is the No.1 cougar dating site for older women and younger men looking for fun and love around the world.\nThe Cougar Dating App provides customized cougar dating features.\n- Cougar searches\n- Verified Photo \/ Age \/ Education\n- Check emails and winks from other members\n- View who is interested in me, winked at me and viewed me.\nAnd more!\n\nWe have multiple subscription options to choose from - starting as low as $33.99\/month:\nYour iTunes account will be charged at confirmation of your purchase and auto-renews for the same upgrade price at the end of one-month period.\nAuto-renew may be turned off by going to your Account Settings after purchase and must be turned off at least 24-hours before the end of the current period.\nNo cancellation of the current upgrade plan is allowed during your active period.\n\nOther things you need to know:\nYou can view our Privacy Policy at http:\/\/www.olderwomendating.com\/privacy_policy_\nYou can view our Service Agreement at http:\/\/www.olderwomendating.com\/service_agreement\nYou must be at least 18 years old to download and use this app","genres":["Social Networking","Entertainment"],"trackId":477091899,"artworkUrl512":"http:\/\/a826.phobos.apple.com\/us\/r30\/Purple\/f5\/84\/21\/mzl.tcyvfckv.png","version":"3.4","primaryGenreId":6005,"primaryGenreName":"Social Networking","bundleId":"com.successfulmatch.olderwomendating","languageCodesISO2A":["EN","DE"],"isGameCenterEnabled":false,"trackCensoredName":"Date Cougar","genreIds":["6005","6016"],"trackName":"Date Cougar","price":0.0,"sellerUrl":"http:\/\/www.successfulmatch.com","screenshotUrls":["http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/db\/bd\/3d\/dbbd3d48-5137-1955-2968-93bacd0cf4b1\/screen1136x1136.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/ce\/35\/e6\/ce35e691-0e84-5643-3dd3-506b4c628455\/screen1136x1136.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/e8\/3a\/4a\/e83a4abd-e023-b60e-656f-301a656cbb2c\/screen1136x1136.jpeg","http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/e0\/27\/43\/e0274371-1043-710d-2f14-5cbf26d53992\/screen1136x1136.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/ed\/da\/ea\/eddaea63-a9b9-7aee-15a6-e24599f82b28\/screen1136x1136.jpeg"],"trackContentRating":"17+","trackViewUrl":"https:\/\/itunes.apple.com\/us\/app\/date-cougar\/id477091899?mt=8&uo=4","formattedPrice":"Free","artistViewUrl":"https:\/\/itunes.apple.com\/us\/artist\/successfulmatch.com\/id335127887?uo=4","kind":"software","fileSizeBytes":"24631093","sellerName":"SuccessfulMatch.com","supportedDevices":["iPhone-3GS","iPhone5s","iPadFourthGen4G","iPadMini","iPadThirdGen","iPhone5","iPodTouchFifthGen","iPhone5c","iPad23G","iPadFourthGen","iPhone4S","iPadMini4G","iPodTouchourthGen","iPadThirdGen4G","iPhone4","iPad2Wifi"],"artworkUrl100":"http:\/\/a826.phobos.apple.com\/us\/r30\/Purple\/f5\/84\/21\/mzl.tcyvfckv.png","artistName":"SuccessfulMatch.com","artworkUrl60":"http:\/\/a926.phobos.apple.com\/us\/r30\/Purple4\/v4\/f7\/49\/2e\/f7492ec5-d1b9-85bd-e0a5-b72e02509df3\/AppIcon57x57.png","wrapperType":"software"}]}
492020793{"resultCount":1,"results":[{"contentAdvisoryRating":"4+","features":["gameCenter","iosUniversal"],"ipadScreenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d2\/03\/a3\/d203a3e4-f1b5-2511-39ae-dcb232a99f00\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c7\/ca\/c1\/c7cac12d-b741-2eea-d747-ddf79c122bc4\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c3\/0e\/b4\/c30eb42b-a6bb-e54a-2c6c-2f0f2c4cd1ee\/screen480x480.jpeg"],"averageUserRatingForCurrentVersion":4.5,"releaseDate":"2014-03-14T22:42:22Z","currency":"USD","artistId":365530479,"userRatingCountForCurrentVersion":35,"description":"He's strong to do travel to a lifetime.\nBut he's tired at times.\nSO Please help his long distance trip.\nJust tap the touch screen to flap the little wings and avoid pesticide poles.\n\n- Easy one touch control\n- Moving colorful poles.\n- 8-bit pixel retro graphics.\n- Easier than Flappy Bird.","genres":["Games","Entertainment","Action","Adventure"],"trackId":492020793,"artworkUrl512":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","version":"1.0","primaryGenreId":6014,"primaryGenreName":"Games","bundleId":"com.Mighty.Mosquito","languageCodesISO2A":["EN"],"isGameCenterEnabled":true,"trackCensoredName":"Mighty Mosquito","genreIds":["6014","6016","7001","7002"],"trackName":"Mighty Mosquito","price":0.0,"sellerUrl":"http:\/\/youtu.be\/Wce3p9K-vEI","screenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/fa\/a5\/16\/faa51679-0f50-3aa8-b920-707cc78f5e31\/screen1136x1136.jpeg","http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/ff\/33\/69\/ff3369a5-1f59-68d1-1bed-ce94e1c6e7cc\/screen1136x1136.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d6\/7b\/66\/d67b662e-3369-d00a-6bce-b0608be55a9c\/screen1136x1136.jpeg"],"userRatingCount":35,"trackContentRating":"4+","trackViewUrl":"https:\/\/itunes.apple.com\/us\/app\/mighty-mosquito\/id492020793?mt=8&uo=4","formattedPrice":"Free","artistViewUrl":"https:\/\/itunes.apple.com\/us\/artist\/wiseit\/id365530479?uo=4","kind":"software","fileSizeBytes":"4467944","sellerName":"Wiseit","supportedDevices":["iPad23G","iPad3G","iPadMini4G","iPhone-3GS","iPodTouchThirdGen","iPodTouchFifthGen","iPhone5c","iPadThirdGen4G","iPadFourthGen","iPhone4","iPadMini","iPadFourthGen4G","iPadWifi","iPhone4S","iPadThirdGen","iPhone5","iPhone5s","iPodTouchourthGen","iPad2Wifi"],"artworkUrl100":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","artistName":"Wiseit","averageUserRating":4.5,"artworkUrl60":"http:\/\/a1733.phobos.apple.com\/us\/r30\/Purple\/v4\/fc\/14\/ce\/fc14ce2a-1aa2-9f8b-2ca6-83de554f02ba\/AppIcon57x57.png","wrapperType":"software"}]}'
str = '{"resultCount":1,"results":[{"contentAdvisoryRating":"4+","features":["gameCenter","iosUniversal"],"ipadScreenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d2\/03\/a3\/d203a3e4-f1b5-2511-39ae-dcb232a99f00\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c7\/ca\/c1\/c7cac12d-b741-2eea-d747-ddf79c122bc4\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c3\/0e\/b4\/c30eb42b-a6bb-e54a-2c6c-2f0f2c4cd1ee\/screen480x480.jpeg"],"averageUserRatingForCurrentVersion":4.5,"releaseDate":"2014-03-14T22:42:22Z","currency":"USD","artistId":365530479,"userRatingCountForCurrentVersion":35,"description":"He's strong to do travel to a lifetime.\nBut he's tired at times.\nSO Please help his long distance trip.\nJust tap the touch screen to flap the little wings and avoid pesticide poles.\n\n- Easy one touch control\n- Moving colorful poles.\n- 8-bit pixel retro graphics.\n- Easier than Flappy Bird.","genres":["Games","Entertainment","Action","Adventure"],"trackId":492020793,"artworkUrl512":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","version":"1.0","primaryGenreId":6014,"primaryGenreName":"Games","bundleId":"com.Mighty.Mosquito","languageCodesISO2A":["EN"],"isGameCenterEnabled":true,"trackCensoredName":"Mighty Mosquito","genreIds":["6014","6016","7001","7002"],"trackName":"Mighty Mosquito","price":0.0,"sellerUrl":"http:\/\/youtu.be\/Wce3p9K-vEI","screenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/fa\/a5\/16\/faa51679-0f50-3aa8-b920-707cc78f5e31\/screen1136x1136.jpeg","http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/ff\/33\/69\/ff3369a5-1f59-68d1-1bed-ce94e1c6e7cc\/screen1136x1136.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d6\/7b\/66\/d67b662e-3369-d00a-6bce-b0608be55a9c\/screen1136x1136.jpeg"],"userRatingCount":35,"trackContentRating":"4+","trackViewUrl":"https:\/\/itunes.apple.com\/us\/app\/mighty-mosquito\/id492020793?mt=8&uo=4","formattedPrice":"Free","artistViewUrl":"https:\/\/itunes.apple.com\/us\/artist\/wiseit\/id365530479?uo=4","kind":"software","fileSizeBytes":"4467944","sellerName":"Wiseit","supportedDevices":["iPad23G","iPad3G","iPadMini4G","iPhone-3GS","iPodTouchThirdGen","iPodTouchFifthGen","iPhone5c","iPadThirdGen4G","iPadFourthGen","iPhone4","iPadMini","iPadFourthGen4G","iPadWifi","iPhone4S","iPadThirdGen","iPhone5","iPhone5s","iPodTouchourthGen","iPad2Wifi"],"artworkUrl100":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","artistName":"Wiseit","averageUserRating":4.5,"artworkUrl60":"http:\/\/a1733.phobos.apple.com\/us\/r30\/Purple\/v4\/fc\/14\/ce\/fc14ce2a-1aa2-9f8b-2ca6-83de554f02ba\/AppIcon57x57.png","wrapperType":"software"}]}'
str = '{"resultCount":1,"results":[{"contentAdvisoryRating":"4+","features":["gameCenter","iosUniversal"],"ipadScreenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d2\/03\/a3\/d203a3e4-f1b5-2511-39ae-dcb232a99f00\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c7\/ca\/c1\/c7cac12d-b741-2eea-d747-ddf79c122bc4\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c3\/0e\/b4\/c30eb42b-a6bb-e54a-2c6c-2f0f2c4cd1ee\/screen480x480.jpeg"],"averageUserRatingForCurrentVersion":4.5,"releaseDate":"2014-03-14T22:42:22Z","currency":"USD","artistId":365530479,"userRatingCountForCurrentVersion":35,"description":"He's strong to do travel to a lifetime.\nBut he's tired at times.\nSO Please help his long distance trip.\nJust tap the touch screen to flap the little wings and avoid pesticide poles.\n\n- Easy one touch control\n- Moving colorful poles.\n- 8-bit pixel retro graphics.\n- Easier than Flappy Bird.","genres":["Games","Entertainment","Action","Adventure"],"trackId":492020793,"artworkUrl512":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","version":"1.0","primaryGenreId":6014,"primaryGenreName":"Games","bundleId":"com.Mighty.Mosquito","languageCodesISO2A":["EN"],"isGameCenterEnabled":true,"trackCensoredName":"Mighty Mosquito","genreIds":["6014","6016","7001","7002"],"trackName":"Mighty Mosquito","price":0.0,"sellerUrl":"http:\/\/youtu.be\/Wce3p9K-vEI","screenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/fa\/a5\/16\/faa51679-0f50-3aa8-b920-707cc78f5e31\/screen1136x1136.jpeg","http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/ff\/33\/69\/ff3369a5-1f59-68d1-1bed-ce94e1c6e7cc\/screen1136x1136.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d6\/7b\/66\/d67b662e-3369-d00a-6bce-b0608be55a9c\/screen1136x1136.jpeg"],"userRatingCount":35,"trackContentRating":"4+","trackViewUrl":"https:\/\/itunes.apple.com\/us\/app\/mighty-mosquito\/id492020793?mt=8&uo=4","formattedPrice":"Free","artistViewUrl":"https:\/\/itunes.apple.com\/us\/artist\/wiseit\/id365530479?uo=4","kind":"software","fileSizeBytes":"4467944","sellerName":"Wiseit","supportedDevices":["iPad23G","iPad3G","iPadMini4G","iPhone-3GS","iPodTouchThirdGen","iPodTouchFifthGen","iPhone5c","iPadThirdGen4G","iPadFourthGen","iPhone4","iPadMini","iPadFourthGen4G","iPadWifi","iPhone4S","iPadThirdGen","iPhone5","iPhone5s","iPodTouchourthGen","iPad2Wifi"],"artworkUrl100":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","artistName":"Wiseit","averageUserRating":4.5,"artworkUrl60":"http:\/\/a1733.phobos.apple.com\/us\/r30\/Purple\/v4\/fc\/14\/ce\/fc14ce2a-1aa2-9f8b-2ca6-83de554f02ba\/AppIcon57x57.png","wrapperType":"software"}]}"
str = "{"resultCount":1,"results":[{"contentAdvisoryRating":"4+","features":["gameCenter","iosUniversal"],"ipadScreenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d2\/03\/a3\/d203a3e4-f1b5-2511-39ae-dcb232a99f00\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c7\/ca\/c1\/c7cac12d-b741-2eea-d747-ddf79c122bc4\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c3\/0e\/b4\/c30eb42b-a6bb-e54a-2c6c-2f0f2c4cd1ee\/screen480x480.jpeg"],"averageUserRatingForCurrentVersion":4.5,"releaseDate":"2014-03-14T22:42:22Z","currency":"USD","artistId":365530479,"userRatingCountForCurrentVersion":35,"description":"He's strong to do travel to a lifetime.\nBut he's tired at times.\nSO Please help his long distance trip.\nJust tap the touch screen to flap the little wings and avoid pesticide poles.\n\n- Easy one touch control\n- Moving colorful poles.\n- 8-bit pixel retro graphics.\n- Easier than Flappy Bird.","genres":["Games","Entertainment","Action","Adventure"],"trackId":492020793,"artworkUrl512":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","version":"1.0","primaryGenreId":6014,"primaryGenreName":"Games","bundleId":"com.Mighty.Mosquito","languageCodesISO2A":["EN"],"isGameCenterEnabled":true,"trackCensoredName":"Mighty Mosquito","genreIds":["6014","6016","7001","7002"],"trackName":"Mighty Mosquito","price":0.0,"sellerUrl":"http:\/\/youtu.be\/Wce3p9K-vEI","screenshotUrls":["http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/fa\/a5\/16\/faa51679-0f50-3aa8-b920-707cc78f5e31\/screen1136x1136.jpeg","http:\/\/a4.mzstatic.com\/us\/r30\/Purple\/v4\/ff\/33\/69\/ff3369a5-1f59-68d1-1bed-ce94e1c6e7cc\/screen1136x1136.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple\/v4\/d6\/7b\/66\/d67b662e-3369-d00a-6bce-b0608be55a9c\/screen1136x1136.jpeg"],"userRatingCount":35,"trackContentRating":"4+","trackViewUrl":"https:\/\/itunes.apple.com\/us\/app\/mighty-mosquito\/id492020793?mt=8&uo=4","formattedPrice":"Free","artistViewUrl":"https:\/\/itunes.apple.com\/us\/artist\/wiseit\/id365530479?uo=4","kind":"software","fileSizeBytes":"4467944","sellerName":"Wiseit","supportedDevices":["iPad23G","iPad3G","iPadMini4G","iPhone-3GS","iPodTouchThirdGen","iPodTouchFifthGen","iPhone5c","iPadThirdGen4G","iPadFourthGen","iPhone4","iPadMini","iPadFourthGen4G","iPadWifi","iPhone4S","iPadThirdGen","iPhone5","iPhone5s","iPodTouchourthGen","iPad2Wifi"],"artworkUrl100":"http:\/\/a459.phobos.apple.com\/us\/r30\/Purple\/v4\/da\/d0\/0b\/dad00b35-e97c-e6e7-b778-db54d56f77ec\/mzl.ajcgvubz.png","artistName":"Wiseit","averageUserRating":4.5,"artworkUrl60":"http:\/\/a1733.phobos.apple.com\/us\/r30\/Purple\/v4\/fc\/14\/ce\/fc14ce2a-1aa2-9f8b-2ca6-83de554f02ba\/AppIcon57x57.png","wrapperType":"software"}]}"
str = "{"resultCount":1,"results":[{"contentAdvisoryRating":"4+","features":[],"ipadScreenshotUrls":["http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c8\/35\/b4\/c835b495-0915-699d-655e-5b5fa21e7d54\/screen480x480.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple2\/v4\/43\/9a\/ae\/439aaed2-a977-4f5d-d70e-5d1211e53933\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple2\/v4\/d5\/37\/69\/d537693f-4021-4a81-3244-a1d72eb18412\/screen480x480.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple2\/v4\/1d\/57\/9c\/1d579c23-79d2-0cf0-80ed-65dcd00123a4\/screen480x480.jpeg","http:\/\/a4.mzstatic.com\/us\/r30\/Purple2\/v4\/d6\/6e\/c3\/d66ec377-6f63-0fb2-12a2-3543442f0b4e\/screen480x480.jpeg"],"releaseDate":"2012-12-31T08:00:00Z","currency":"USD","artistId":418553597,"description":"The FlipChart+ application has taken one of Stryker\u2019s most popular patient education tools and has made it available for the customer who wants to utilize his or her iPad to support patient dialogue. Taking advantage of the versatility of the iPad, this application adds a new dimension to education and the sharing of information. The Orthopaedic section provides an overview of a normal joint, arthritic joint and replacement joint through graphics and X-rays. The Spine section provides an overview of a normal lumbar spine, a lumbar spine with pathology and a depiction of a post-surgery spine with instrumentation. The ability to annotate and mark specific areas of images can help surgeons explain hip, knee or shoulder replacement procedures as well as diseased and healthy spine anatomy with their patients.  FlipChart+ incorporates chart interaction and customization functionality, allowing the user to add images, blank pages, reorder pages and email charts.","genres":["Medical","Education"],"trackId":494105518,"artworkUrl512":"http:\/\/a410.phobos.apple.com\/us\/r30\/Purple2\/v4\/3a\/38\/09\/3a380902-85cd-20d9-a95b-ede2ba6e3c2f\/mzl.lzocpcpm.png","version":"1.1.3","primaryGenreId":6020,"primaryGenreName":"Medical","bundleId":"com.stryker.flipcharthd","releaseNotes":"* Content added for Stryker Craniomaxillofacial\n* Bug fixes","isGameCenterEnabled":false,"trackCensoredName":"FlipChart Plus","genreIds":["6020","6017"],"trackName":"FlipChart Plus","price":0.0,"sellerUrl":"http:\/\/www.stryker.com\/en-us\/Apps\/FlipChartPlus\/iPad\/index.htm","screenshotUrls":[],"trackContentRating":"4+","trackViewUrl":"https:\/\/itunes.apple.com\/us\/app\/flipchart-plus\/id494105518?mt=8&uo=4","formattedPrice":"Free","artistViewUrl":"https:\/\/itunes.apple.com\/us\/artist\/stryker\/id418553597?uo=4","kind":"software","fileSizeBytes":"65618433","sellerName":"Stryker","supportedDevices":["iPadFourthGen4G","iPadFourthGen","iPad23G","iPadThirdGen4G","iPadThirdGen","iPadMini4G","iPad3G","iPadMini","iPadWifi","iPad2Wifi"],"artworkUrl100":"http:\/\/a410.phobos.apple.com\/us\/r30\/Purple2\/v4\/3a\/38\/09\/3a380902-85cd-20d9-a95b-ede2ba6e3c2f\/mzl.lzocpcpm.png","languageCodesISO2A":["EN"],"artistName":"Stryker","artworkUrl60":"http:\/\/a1725.phobos.apple.com\/us\/r30\/Purple2\/v4\/c0\/1c\/d1\/c01cd12b-b2c4-0a9b-3182-b9364be92f1e\/Icon-72.png","wrapperType":"software"}]}"
str = "{"resultCount":1,"results":[{"contentAdvisoryRating":"4+","features":[],"ipadScreenshotUrls":["http:\/\/a2.mzstatic.com\/us\/r30\/Purple\/v4\/c8\/35\/b4\/c835b495-0915-699d-655e-5b5fa21e7d54\/screen480x480.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple2\/v4\/43\/9a\/ae\/439aaed2-a977-4f5d-d70e-5d1211e53933\/screen480x480.jpeg","http:\/\/a2.mzstatic.com\/us\/r30\/Purple2\/v4\/d5\/37\/69\/d537693f-4021-4a81-3244-a1d72eb18412\/screen480x480.jpeg","http:\/\/a3.mzstatic.com\/us\/r30\/Purple2\/v4\/1d\/57\/9c\/1d579c23-79d2-0cf0-80ed-65dcd00123a4\/screen480x480.jpeg","http:\/\/a4.mzstatic.com\/us\/r30\/Purple2\/v4\/d6\/6e\/c3\/d66ec377-6f63-0fb2-12a2-3543442f0b4e\/screen480x480.jpeg"],"releaseDate":"2012-12-31T08:00:00Z","currency":"USD","artistId":418553597,"description":"The FlipChart+ application has taken one of Stryker\u2019s most popular patient education tools and has made it available for the customer who wants to utilize his or her iPad to support patient dialogue. Taking advantage of the versatility of the iPad, this application adds a new dimension to education and the sharing of information. The Orthopaedic section provides an overview of a normal joint, arthritic joint and replacement joint through graphics and X-rays. The Spine section provides an overview of a normal lumbar spine, a lumbar spine with pathology and a depiction of a post-surgery spine with instrumentation. The ability to annotate and mark specific areas of images can help surgeons explain hip, knee or shoulder replacement procedures as well as diseased and healthy spine anatomy with their patients.  FlipChart+ incorporates chart interaction and customization functionality, allowing the user to add images, blank pages, reorder pages and email charts.","genres":["Medical","Education"],"trackId":494105518,"artworkUrl512":"http:\/\/a410.phobos.apple.com\/us\/r30\/Purple2\/v4\/3a\/38\/09\/3a380902-85cd-20d9-a95b-ede2ba6e3c2f\/mzl.lzocpcpm.png","version":"1.1.3","primaryGenreId":6020,"primaryGenreName":"Medical","bundleId":"com.stryker.flipcharthd","releaseNotes":"* Content added for Stryker Craniomaxillofacial\n* Bug fixes","isGameCenterEnabled":false,"trackCensoredName":"FlipChart Plus","genreIds":["6020","6017"],"trackName":"FlipChart Plus","price":0.0,"sellerUrl":"http:\/\/www.stryker.com\/en-us\/Apps\/FlipChartPlus\/iPad\/index.htm","screenshotUrls":[],"trackContentRating":"4+","trackViewUrl":"https:\/\/itunes.apple.com\/us\/app\/flipchart-plus\/id494105518?mt=8&uo=4","formattedPrice":"Free","artistViewUrl":"https:\/\/itunes.apple.com\/us\/artist\/stryker\/id418553597?uo=4","kind":"software","fileSizeBytes":"65618433","sellerName":"Stryker","supportedDevices":["iPadFourthGen4G","iPadFourthGen","iPad23G","iPadThirdGen4G","iPadThirdGen","iPadMini4G","iPad3G","iPadMini","iPadWifi","iPad2Wifi"],"artworkUrl100":"http:\/\/a410.phobos.apple.com\/us\/r30\/Purple2\/v4\/3a\/38\/09\/3a380902-85cd-20d9-a95b-ede2ba6e3c2f\/mzl.lzocpcpm.png","languageCodesISO2A":["EN"],"artistName":"Stryker","artworkUrl60":"http:\/\/a1725.phobos.apple.com\/us\/r30\/Purple2\/v4\/c0\/1c\/d1\/c01cd12b-b2c4-0a9b-3182-b9364be92f1e\/Icon-72.png","wrapperType":"software"}]}"
re.split('[\.,vV]', 'v1.00')
re.split('[\.,vV]', 'v1.00'.strip())
ver = re.split('[\.,vV]', 'v1.00'.strip())
ver
[el for el in ver if el != '']
ver = re.split('[\.,]', 'v1.00'.strip())
ver
int(ver[0]_
int(ver[0])
apps[848651098]
apps[820868997]
len(newest)
rand_newest = [re.split('\t', line) for line in file('./selected/newest')]
rand_newest
rand_newest = [re.split('\t', line.strip) for line in file('./selected/newest')]
rand_newest = [re.split('\t', line.strip()) for line in file('./selected/newest')]
rand_newest
newest = [re.split(' ', line.strip()) for line in file('./rel-after-200140101.txt')]
newest
rand_newest
d_newest = {}
d_newest = {int(id), name for name, id in newest}
d_newest = {(int(id), name) for name, id in newest}
d_newest = {(int(id), name) for name, id in newest}
newest
d_newest = {(int(app[0]), app[2]) for app in newest}
d_newest = {(int(app[0]), 1) for app in newest}
d_newest
len(d_newest)
rand_newest
d_rand_newest = [int(id) for _,id in rand_newest]
d_rand_newest
sum([1 for id in d_rand_newest if d_newest.has_key(id)])
d_newest = {(int(app[0]): 1) for app in newest}
d_newest = dict{(int(app[0]), 1) for app in newest}
d_newest = {int(app[0]):1 for app in newest}
sum([1 for id in d_rand_newest if d_newest.has_key(id)])
new = released_in_date_range(all_apps, apps, (2014, 1, 1), (2014, 4, 30))
len(new)
new = released_in_date_range(all_apps, apps, (2014, 2, 1), (2014, 4, 30))
len(new)
new[1]
file("./junk.txt", 'w').write(new.__str__())
len(newest)
rand_br_newest = [re.split('\t', line.strip()) for line in file('./selected/br_newest')]
d_rand_br = [int(id) for _,id in rand_br_newest]
sum([1 for id in d_rand_br if d_newest.has_key(id)])
cbr = [re.split('\t', line.strip()) for line in file('./selected/cbr_new')]
cbr
d_cbr = [int(id) for _,id in cbr]
d_cbr
d_rand_br
sum([1 for id in d_rand_br if d_newest.has_key(id)])
sum([1 for id in d_cbr if d_newest.has_key(id)])
sel = [re.split('\t', line.strip()) for line in file('../selected-apps.txt')]
len(sel)
d_sel = [int(id) for _,id in sel]
d_sel[1]
sum([1 for id in d_sel if d_newest.has_key(id)])
sum([1 for id in d_rand_br if d_newest.has_key(id)])
sum([1 for id in d_rand_newest if d_newest.has_key(id)])
d_newest
d_newest = {int(app[0]):app[1:] for app in newest}
d_newest
newest = [re.split(' ', line.strip()) for line in file('./selected/rel-after-200140131.txt')]
newest = [re.split(' ', line.strip()) for line in file('./selected/rel-after-20140131.txt')]
len(newest)
d_newest = {int(app[0]):app[1:] for app in newest}
len(d_newest)
sum([1 for id in d_rand_newest if d_newest.has_key(id)])
sum([1 for id in d_rand_br if d_newest.has_key(id)])
sum([1 for id in cbr if d_newest.has_key(id)])
sum([1 for id in d_cbr if d_newest.has_key(id)])
rand_new = [re.split('\t', line.strip()) for line in file('./selected/new')]
d_rand_new = [int(id) for _,id in rand_new]
sum([1 for id in d_rand_new if d_newest.has_key(id)])
rand_br_new = [re.split('\t', line.strip()) for line in file('./selected/br_new')]
d_rand_br_new = [int(id) for _,id in rand_br_new]
sum([1 for id in d_rand_br_new if d_newest.has_key(id)])
[id in d_rand_br_new if d_newest.has_key(id)])
[id for id in d_rand_br_new if d_newest.has_key(id)])
[id for id in d_rand_br_new if d_newest.has_key(id)]
len([id for id in d_rand_br_new if d_newest.has_key(id)])
file("./post-20140131/rand_br_new", 'w').write([id for id in d_rand_br_new if d_newest.has_key(id)])
file("./post-20140131/rand_br_new", 'w').write('\n'.join([id for id in d_rand_br_new if d_newest.has_key(id)]))
file("./post-20140131/rand_br_new", 'w').write("\n".join([id for id in d_rand_br_new if d_newest.has_key(id)]))
str = "\n".join([id for id in d_rand_br_new if d_newest.has_key(id)])
l = [id for id in d_rand_br_new if d_newest.has_key(id)]
l
len(l)
str = "\n".join(l)
str = "\n".join([str(id) for id in l)
str = "\n".join([str(id) for id in l])
str1 = "\n".join([str(id) for id in l])
str1 = "\n".join([id.__str__() for id in l])
str1
file("./post-20140131/rand_br_new", 'w').write(str1)
l = [id.__str__() for id in d_rand_new if d_newest.has_key(id)]
l
len(l)
file("./post-20140131/rand_br_new", 'w').write("\n)
file("./post-20140131/rand_new", 'w').write("\n".join(l))
l = [id.__str__() for id in d_rand_newest if d_newest.has_key(id)]
len(l)
file("./post-20140131/rand_newest", 'w').write("\n".join(l))
len(d_rand_br)
len(d_rand_br_new)
d_rand_br_newest = d_rand_br
l = [id.__str__() for id in d_rand_br_newest if d_newest.has_key(id)]
len(l)
file("./post-20140131/rand_br_newest", 'w').write("\n".join(l))
len(cbr)
cbr
short_apps = [re.split(' ', line.strip()) for line in file('./selected/short-apps.txt')]
short_apps
short_apps = [re.split('\t', line.strip()) for line in file('./selected/short-apps.txt')]
short_apps
sh_apps = {int(app[0]):app[1:] for app in short_apps}
sh_apps = [int(app[1]) for app in short_apps}
sh_apps = [int(app[1]) for app in short_apps]
sh_apps = [int(app[0]) for app in short_apps]
short_apps
sh_apps = [int(app[1]) for app in short_apps]
sh_apps = [int(app[1]) for app in short_apps]
short_apps[0]
short_apps[0][1]
[app for app in short_apps{:2]
[app for app in short_apps[:2]]
[app[0] for app in short_apps[:2]]
[int(app[1]) for app in short_apps[:2]]
[int(app[1]) for app in short_apps]
[int(app[1]) for app in short_apps[:]]
short_apps
[int(app[1]) for app in short_apps[:] if len(app) >= 2]
sh_apps = [int(app[1]) for app in short_apps[:] if len(app) >= 2]
len(sh_apps)
sh_apps = {int(app[1]):1 for app in short_apps[:] if len(app) >= 2}
sh_apps
d_newest
sum([1 for id in d_rand_br_new if sh_apps.has_key(id)])
sum([1 for id in d_rand_br_newest if sh_apps.has_key(id)])
sum([1 for id in d_rand_newest if sh_apps.has_key(id)])
sum([1 for id in d_rand_new if sh_apps.has_key(id)])
sum([1 for id in d_cbr if sh_apps.has_key(id)])
l1 = [id.__str__() for id in d_rand_br_newest if d_newest.has_key(id) and sh_apps.has_key(id)]
len(l1)
l1 = [id.__str__() for id in d_rand_br_newest if d_newest.has_key(id) and not sh_apps.has_key(id)]
len(l1)
newest = [re.split(' ', line.strip()) for line in file('./selected/rel-after-20140131.txt')]
len(newest)
len(d_newest)
l = [id.__str__() for id in d_rand_br_newest if d_newest.has_key(id) and not sh_apps.has_key(id)]
l1 = [id.__str__() for id in d_rand_br_newest if d_newest.has_key(id) and not sh_apps.has_key(id)]
l1 = [id.__str__() for id in d_rand_br_newest if d_newest.has_key(id) and not sh_apps.has_key(id)]
file("./post-20140131/rand_br_newest", 'w').write("\n".join(l))
l1 = [id.__str__() for id in d_rand_br_new if d_newest.has_key(id) and not sh_apps.has_key(id)]
file("./post-20140131/rand_br_new", 'w').write("\n".join(l))
len(l1)
l1 = [id.__str__() for id in d_rand_new if d_newest.has_key(id) and not sh_apps.has_key(id)]
len(l1)
file("./post-20140131/rand_new", 'w').write("\n".join(l1))
l1 = [id.__str__() for id in d_rand_br_new if d_newest.has_key(id) and not sh_apps.has_key(id)]
len(l1)
file("./post-20140131/rand_br_new", 'w').write("\n".join(l1))
l1 = [id.__str__() for id in d_rand_br_newest if d_newest.has_key(id) and not sh_apps.has_key(id)]
len(l1)
file("./post-20140131/rand_br_newest", 'w').write("\n".join(l1))
l1 = [id.__str__() for id in d_rand_newest if d_newest.has_key(id) and not sh_apps.has_key(id)]
len(l1)
l1 = [id.__str__() for id in d_rand_newest if d_newest.has_key(id)]
len(l1)
len(d_rand_newest)
l1 = [id.__str__() for id in d_rand_newest if d_newest.has_key(id) and not sh_apps.has_key(id)]
file("./post-20140131/rand_newest", 'w').write("\n".join(l1))
l1 = [id.__str__() for id in d_cbr if d_newest.has_key(id) and not sh_apps.has_key(id)]
len(d_cbr)
len(l1)
l1 = [id.__str__() for id in d_cbr if d_newest.has_key(id)]
len(l1)
l1 = [id.__str__() for id in d_cbr if d_newest.has_key(id) and not sh_apps.has_key(id)]
len(l1)
file("./post-20140131/cbr_new", 'w').write("\n".join(l1))
d_cbr
l1 = [id.__str__() for id in d_cbr if not sh_apps.has_key(id)]
len(11)
len(l1)
file("./post-20140131/cbr", 'w').write("\n".join(l1))
cbr = [id for id in d_cbr if not sh_apps.has_key(id)]
cbr_new = [id for id in d_cbr if d_newest.has_key(id) and not sh_apps.has_key(id)]
cbr_new
[apps[id] for apps in cbr_new]
[apps[id] for id in cbr_new]
cbr_new
[apps[id] for id in cbr_new]
id
apps[id]
[apps[id.__str__()] for id in cbr_new]
apps['820868997']
apps
apps = read_app_data('apps.txt')
[apps[id] for id in cbr_new]
cbr_new
apps[cbr_new[0]]
d = {}
d[1][2] = 4
d[1] = 4
d
d['1'] = 4
d
d.items
d.items()
d[1] = 5
d
d[1][2] = 5
d = {}
d[1][2] = 5
d = {}
if not d.had_keys(1):
    d[1] = {}
    
if not d.has_keys(1):
    d[1] = {}
    
if not d.haskeys(1):
    d[1] = {}
    
if not d.has_key(1):
    d[1] = {}
    
d
if not d.has_key(1):
    d[1] = {}
    
d = {}
if not d.has_key(1):
    l = []
    d[1] = l
else:
    l = d[1]
    
l
d
l.append('a')
l
d
if not d.has_key(1):
    l = []
    d[1] = l
else:
    l = d[1]
    
l
l.append('b')
l
d
app_ranks, ard = app_ranks_dict("./ranks.txt", apps)
app_ranks, ard = read_app_ranks("./ranks.txt", apps)
len(ard)
reload(parseRanks_
reload(parseRanks)
reload(parseRanks)
app_ranks, ard = read_app_ranks("./ranks.txt", apps)
ard, app_ranks = read_app_ranks("./ranks.txt", apps)
get_ipython().magic(u'pwd ')
reload(parseRanks)
from parseRanks import *
app_ranks, ard = read_app_ranks("./ranks.txt", apps)
reload(parseRanks)
from parseRanks import *
app_ranks, ard = read_app_ranks("./ranks.txt", apps)
app_ranks, ard = read_app_ranks("./ranks.txt", apps)
reload(parseRanks)
from parseRanks import *
app_ranks, ard = read_app_ranks("./ranks.txt", apps)
len(app_ranks)
len(ard)
len(apps)
cbr_new
ard[cbr_new[0]]
ard[cbr_new[0]][0]
ard[cbr_new[0]][0][3]
ard[cbr_new[0]][0][0]
ard[cbr_new[0]][0][1]
ard[cbr_new[0]][0][2]
ard[cbr_new[0]][1][2]
ard[cbr_new[0]][2][2]
ard[cbr_new[0]][3][2]
ard[cbr_new[0]][4][2]
ard[cbr_new[0]][5][2]
ard[cbr_new[0]][5][0]
ard[cbr_new[0]][5][1]
ard[cbr_new[0]][1][1]
ard[cbr_new[0]][0]
ard[cbr_new[0]][0][1]
ard[cbr_new[0]][0][2]
ard[cbr_new[0]][1][1]
ard[cbr_new[0]][7][1]
ard[cbr_new[0]][13][1]
ard[cbr_new[0]][19][1]
ard[cbr_new[0]][19][2]
ard[cbr_new[0]][19][3]
ard[cbr_new[0]][19][0]
ard[cbr_new[0]][1][0]
ard[cbr_new[0]][2][0]
ard[cbr_new[0]][7][0]
ard[cbr_new[0]][7][1]
ard[cbr_new[0]][7][0]
ard[cbr_new[0]][22][0]
ard[cbr_new[0]][21][0]
ard[cbr_new[0]][20][0]
ard[cbr_new[0]][18][0]
ard[cbr_new[0]][17][0]
ard[cbr_new[0]][36][0]
ard[cbr_new[0]][54][0]
ard[cbr_new[0]][0][1]
ard[cbr_new[0]][6][1]
ard[cbr_new[0]][0][3]
reload(parseRanks)
range(1:5)
range(1:5)
reload(parseRanks)
from parseRanks import *
range(1:5)
range(1,5)
day_of_year((2014, 3, 1))
reload(parseRanks)
from parseRanks import *
day_of_year((2014, 3, 1))
ard[cbr_new[0]][6][1]
ard[cbr_new[0]][0][3][0]
ard[cbr_new[0]][0][3][0][1]
ard[cbr_new[0]][0][3][0][0]
gr = [day_of_year(date), rank for date, rank in ard[cbr_new[0]][0][3]]
gr = [(day_of_year(date), rank) for date, rank in ard[cbr_new[0]][0][3]]
gr
import matplotlib.pyplot as plt
gr[0]
gr[:][0]
gr[:]
gr[:][1]
import numpy as np
d = np.array(gr)
d
d[:][1]
d[0]
d[0][0]
d[:][0]
d[0][:]
d.shape
d[:, 0]
d[:, 1]
plt.plot(d[:, 0], d[:, 1])
plt.show()
gr = [(day_of_year(date), rank) for date, rank in ard[cbr_new[0]][1][3]]
d1 = np.array(gr)
plt.plot(d1[:, 0], d1[:, 1])
plt.show()
plt.plot(d[:, 0], d[:, 1])
plt.plot(d1[:, 0], d1[:, 1])
plt.show()
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[0]][i][3]] for i in range(6)]
gr
gr[0]
gr
A = [np.array(gr[i]) for i in range(6)]
A
A[0].shape
[plt.plot(A[i][:, 0], A[i][:, 1]) for i in range(6)]
ard[cbr_new[0]][0][2]]
ard[cbr_new[0]][0][2]
ard[cbr_new[0]][1][2]
[ard[cbr_new[0]][i][2] for i in range(6)]
plt.legend('a', 'c', 'g', 'p', 's', 'u')
plt.legend([ard[cbr_new[0]][i][2] for i in range(6)])
plt.show()
plt.plot(A[0][:, 0], A[1][:, 1])
plt.show()
plt.plot(A[0][:, 0], A[1][:, 1])
plt.plot(A[1][:, 0], A[1][:, 1])
plt.show()
plt.plot(A[0][:, 0], A[1][:, 1])
plt.show()
plt.plot(A[0][:, 0], A[0][:, 1])
plt.plot(A[1][:, 0], A[1][:, 1])
plt.legend([ard[cbr_new[0]][i][2] for i in range(2)])
plt.show()
[plt.plot(A[i][:, 0], A[i][:, 1]) for i in range(3)]
plt.legend([ard[cbr_new[0]][i][2] for i in range(3)])
plt.show()
[apps[id] for id in cbr_new]
plt.legend([ard[cbr_new[0]][i][2] for i in range(6)])
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[4]][i][3]] for i in range(6)]
A = [np.array(gr[i]) for i in range(6)]
[plt.plot(A[i][:, 0], A[i][:, 1]) for i in range(3)]
plt.legend([ard[cbr_new[0]][i][2] for i in range(3)])
plt.show()
[plt.plot(A[i][:, 0], A[i][:, 1]) for i in range(6)]
plt.legend([ard[cbr_new[0]][i][2] for i in range(6)])
plt.show()
A[0]
A[0].size
A[1].size
A[1].shape
A[0].shape
A[1].shape
A[2].shape
A[3].shape
A[4].shape
A[5].shape
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[5]][i][3]] for i in range(6)]
A = [np.array(gr[i]) for i in range(6)]
A[0].shape
A[1].shape
A[2].shape
A[3].shape
A[4].shape
A[5].shape
A[6].shape
[plt.plot(A[i][:, 0], A[i][:, 1]) for i in range(6)]
plt.legend([ard[cbr_new[0]][i][2] for i in range(3)])
plt.legend([ard[cbr_new[0]][i][2] for i in range(6)])
plt.show()
gr
[apps[id] for id in cbr_new]
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[4]][i][3]] for i in range(6)]
gr
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[0]][i][3]] for i in range(6)]
gr
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[1]][i][3]] for i in range(6)]
gr
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[2]][i][3]] for i in range(6)]
gr
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[2]][i][3]] for i in range(7:12)]
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[2]][i][3]] for i in range(7,12)]
gr
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[2]][i][3]] for i in range(12,18)]
gr
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[2]][i][3]] for i in range(18,24)]
gr
gr = [[(day_of_year(date), rank) for date, rank in ard[cbr_new[2]][i][3]] for i in range(18,24)]
ard[cbr_new[2]][18][0]
ard[cbr_new[2]][18][1]
ard[cbr_new[2]][18][2]
cbr
len(ard[cbr[1]])
len(ard[cbr[1]])
ard[cbr[1]]
ard[cbr[1]][0]
ard[cbr[1]][1]
ard[cbr[1]][2]
ard[cbr[1]][3]
ard[cbr[1]][4]
ard[cbr[1]][0]
ard[cbr[1]][1]
ard[cbr[1]][2]
ard[cbr[1]][3]
ard[cbr[1]]
apps[cbr[1]]
ard[cbr[1]][:2
]
ard[cbr[1]][2:8]
ard[cbr[1]][8:14]
ard[cbr[1]][8:10]
ard[cbr[1]][14:16]
ard[cbr[1]][16:22]
ard[cbr[1]][22:28]
ard[cbr[1]][28:34]
ard[cbr[1]][32:38]
ard[cbr[1]][35:40]
ard[cbr[1]]
get_ipython().magic(u"save 500-600 './ipython-rank-anal'")