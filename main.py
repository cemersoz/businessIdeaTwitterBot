import random
import re

formats_file = open('formats.txt', 'r')
nouns_file = open('nouns.txt', 'r')
adjectives_file = open('adjectives.txt', 'r')
buzzwords_file = open('buzzwords.txt', 'r')

formats = []
nouns = []
adjectives = []
buzzwords = []

for l in formats_file.readlines():
  formats.append(l.strip())

for l in nouns_file.readlines():
  nouns.append(l.strip())

for l in adjectives_file.readlines():
  adjectives.append(l.strip())

for l in buzzwords_file.readlines():
  buzzwords.append(l.strip())

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
  f_ad = smart_replace('{a}', format_string, adjectives, 0, 2)
  f_no = smart_replace('{n}', f_ad, nouns, 1, 1)
  f_bz = smart_replace('{b}', f_no, buzzwords, 0, 2)

  result = re.sub(' +',' ', f_bz.strip())
  print(result)
  raw_input()