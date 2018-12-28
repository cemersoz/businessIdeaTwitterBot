import random
import re
import tweepy
import time

formats_file = open('formats.txt', 'r')
nouns_file = open('nouns.txt', 'r')
adjectives_file = open('adjectives.txt', 'r')
buzzwords_file = open('buzzwords.txt', 'r')
companies_file = open('companies.txt', 'r')
types_file = open('types.txt', 'r')

formats = []
nouns = []
adjectives = []
buzzwords = []
companies = []
types = []

for l in formats_file.readlines():
  formats.append(l.strip())

for l in nouns_file.readlines():
  nouns.append(l.strip())

for l in adjectives_file.readlines():
  adjectives.append(l.strip())

for l in buzzwords_file.readlines():
  buzzwords.append(l.strip())

for l in companies_file.readlines():
  companies.append(l.strip())

for l in types_file.readlines():
  types.append(l.strip())

def smart_replace(pattern, string, options, mincount, maxcount):
  while pattern in string:
    a = random.randint(0, len(options)-1)
    count = random.randint(mincount, maxcount)
    repl = ''
    for c in range(count):
      a_old = a
      a = random.randint(0, len(options)-1)
      while a == a_old:
        a = random.randint(0, len(options)-1)
      repl += ' '+options[a]
    string = re.sub(pattern, repl, string, 1)
  return string

while True:
  f = random.randint(0, len(formats)-1)
  format_string = formats[f]
  f_cm = smart_replace('{c}', format_string, companies, 1, 1)
  f_ad = smart_replace('{a}', f_cm, adjectives, 0, 2)
  f_no = smart_replace('{n}', f_ad, nouns, 1, 1)
  f_bz = smart_replace('{b}', f_no, buzzwords, 0, 2)
  f_ty = smart_replace('{t}', f_bz, types, 1, 1)
  result = re.sub(' +',' ', f_ty.strip())
  result.capitalize()
  print(result)
  raw_input()
