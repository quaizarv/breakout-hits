import re
import numpy as np
import random
from numpy.linalg import *
import string
import sys

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

def filter_books_news(cat):
  if cat == 6006 or cat == 6009 or cat == 6018 or cat > 13000:
    return True
  return False

def filter_app_name(name):
  return not searchable_name(name) or not name_smaller_than(name, 5)
        
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
    if filter_app_name(app_name):
      continue

    app_id = int(items[0])
    price = float(items[2])
    currency = items[3]
    rel_date_str = items[4]
    pub_id = int(items[5])
  
    rel_date_items = re.split(' ', rel_date_str)
    date_str = rel_date_items[0]
    date_elems = re.split('-', date_str)
    rel_date = (int(date_elems[0]), int(date_elems[1]), int(date_elems[2]))
    apps[app_id] = (app_name, price, currency, pub_id, rel_date)

  return apps

def read_app_ranks(app_ranks_file, apps):
  app_ranks = []
  input = open(app_ranks_file, "r")
  for line in input:
    items = re.split('\t', line)

    app_id = int(items[0])
    if (not apps.has_key(app_id)):
      continue
    categ = int(items[1])
    if filter_books_news(categ):
      apps.pop(app_id)
      continue

    country = items[4]
    country = country[:-1]
    rank_history_str = items[2]
    rank_history_str = rank_history_str[1:-1]
    rank_history_items = re.split(',', rank_history_str)
    rank_list = []
    for rank_str in rank_history_items:
      rank_items = re.split(': ', rank_str)
      rank = int(rank_items[1])
      date_str = rank_items[0]
      if (date_str[0] == ' '):
        date_str = date_str[1:]
      date_str = date_str[1:-1]
      date_elems = re.split('-', date_str)
      date = (int(date_elems[0]), int(date_elems[1]), int(date_elems[2]))
      rank_list.append((date, rank))
    rank_list.sort()

    #print (app_id, categ, country, rank_list)
    app_ranks.append((app_id, categ, country, rank_list))
    
  return app_ranks

def find_breakouts(app_ranks, apps, ge_k, le_l):
  breakouts = []
  idx = 0
  for app_id, categ, country, rank_history in app_ranks:
    if not apps.has_key(app_id):
      idx += 1
      continue
    ge_found = False
    le_found = False
    for date, rank in rank_history:
      if rank >= ge_k:
        ge_found = True
      elif rank <= le_l:
        le_found = True
    if ge_found and le_found:
      breakouts.append((app_id, idx))
    idx += 1
  return breakouts

def find_app(app_ranks, key):
  app_idx = 0
  for app_id, categ, country, rank_history in app_ranks:
    if app_id == key:
      return app_idx
    app_idx = app_idx + 1
  return 0;

def remove_books_news(app_ranks, apps):
  al = []
  for app_id, cat, _, _ in app_ranks:
    if cat == 6006 or cat == 6009 or cat == 6018 or cat > 13000:
      if apps.has_key(app_id):
        apps.pop(app_id)

def recently_released_br(app_list, apps, app_ranks):
  result = []
  for app_id, idx in app_list:
    if not apps.has_key(app_id):
      continue
    (_, _, _, _, rel_date) = apps[app_id]
    (app_id, _, _, rank_list) = app_ranks[idx]
    if rel_date >= rank_list[0][0]:
      result.append((app_id, idx))
  return result

def released_in_date_range(app_list, apps, lower_date, upper_date):
  result = []
  for app_id, idx in app_list:
    (_, _, _, _, rel_date) = apps[app_id]
    if rel_date >= lower_date and rel_date <= upper_date:
      result.append((app_id, idx))
  return result

def all_app_list(apps, app_ranks):
  result = []
  app_idx = 0
  for app_id, _, _, _ in app_ranks:
    if (apps.has_key(app_id)):
      result.append((app_id, app_idx))
    app_idx = app_idx + 1
  return uniq(result)

def uniq(app_list):
  result = []
  last = 0
  for app_id, idx in app_list:
    if app_id != last:
      result.append((app_id, idx))
      last = app_id
  return result

def app_name_smaller_than(app_list, apps, num_words):
  result = []
  last = 0
  for app_id, idx in app_list:
    app_name = apps[app_id][0]
    words = re.split('\\s+', app_name)
    if (len(words) < num_words):
      result.append((app_id, idx))
  return result

def consistent_br(app_list, ge_k, le_l, app_ranks):
  result = []
  for app_id, idx in app_list:
    (_, _, _, rank_list) = app_ranks[idx]
    if len(rank_list) >= 8:
      le_l_count, ge_k_count  = 0, 0
      for _, rank in rank_list[:8]:
        if rank >= ge_k:
          ge_k_count += 1;
      for _, rank in rank_list[-4:]:
        if rank <= le_l:
          le_l_count += 1;
      if ge_k_count >= 4 and le_l_count >= 4:
        result.append((app_id, idx))
  return result

def print_apps(app_list, apps, fileName = None):
  if fileName != None:
    f = open(fileName, "w")
  else:
    f = sys.stdout
  for app_id, idx in app_list:
    f.write(apps[app_id][0] + '\t' + str(app_id) + '\n')

def print_app_name(app_list, apps):
  for app_id, idx in app_list:
    print apps[app_id][0]

def print_pub_name(app_list, apps, publishers, fileName = None):
  if fileName != None:
    f = open(fileName, "w")
  else:
    f = sys.stdout
  for app_id, idx in app_list:
    pub_id = apps[app_id][3]
    if (publishers.has_key(pub_id)):
      f.write(publishers[pub_id]+ '\t' +  str(pub_id) + '\n')
  
def union_app_lists(al1, al2):
  dict = {}
  al = []
  for app in al1:
    dict[app[0]] = 1
    al.append(app)
  for app in al2:
    if not dict.has_key(app[0]):
      al.append(app)
  return al    
    

def extract_random(from_list, not_in_list, count):
  dict = {}
  for app in not_in_list:
    dict[app[0]] = 1
  diff_list = []
  for app in from_list:
    if not dict.has_key(app[0]):
      diff_list.append(app)
  sampleIndices = random.sample(range(len(diff_list)),
                                min(len(diff_list), count))
  result_list = []
  for idx in sampleIndices:
    result_list.append(diff_list[idx])
  return result_list
  

def extract_apps(app_ranks, apps):
  #apps = read_app_data('apps.txt')
  #app_ranks = read_app_ranks('ranks.txt')
  br = find_breakouts(app_ranks, apps, 200, 20)
  ubr = uniq(br)
  ubr_newest = released_in_date_range(ubr, apps, (2014, 3, 1), (2014, 4, 30))
  ubr_new = released_in_date_range(ubr, apps, (2013, 1, 1), (2014, 2, 28))

  cbr = consistent_br(br, 200, 40, app_ranks)
  ucbr = uniq(cbr)
  ucbr_new = released_in_date_range(ucbr, apps, (2013, 1, 1), (2014, 4, 30))

  all_apps = all_app_list(apps, app_ranks)
  newest_apps = released_in_date_range(all_apps, apps, (2014, 3, 1), (2014, 4, 30))
  new_apps = released_in_date_range(all_apps, apps, (2013, 1, 1), (2014, 2, 28))
  return (ucbr_new, ubr_newest, ubr_new, newest_apps, new_apps)
  
def extract_random_apps(ucbr_new, ubr_newest, ubr_new, newest_apps, new_apps):
  rand_ubr_newest = extract_random(ubr_newest, ucbr_new, 500)
  rand_ubr_new = extract_random(ubr_new, ucbr_new, 500)

  ul = union_app_lists(ubr_newest, ubr_new)
  rand_newest = extract_random(newest_apps, ul, 500)
  rand_new = extract_random(new_apps, ul, 500)

  return (ucbr_new, rand_ubr_newest, rand_ubr_new, rand_newest, rand_new)
