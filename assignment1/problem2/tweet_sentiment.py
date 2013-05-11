import sys
import json


def make_sent_dict(fn):
  lines = [l.strip().split('\t', 2) for l in fn.readlines()]
  sent_dict = {i[0]: int(i[1]) for i in lines}
  return sent_dict

def print_tweet_sentiments(data, sents):
  for item in data:
    tweet = json.loads(item) 
    if 'text' in tweet:
      sent = calc_sent(tweet['text'], sents)

def calc_sent(tweet, sents):
  words = tweet.split()
  sent = 0
  for item in words:
    if item in sents:
      sent = sent + sents[item]
  print "<sentiment:" + str(sent) + ">"

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  sent_dict = make_sent_dict(sent_file)
  # print sent_dict['bastard']
  print_tweet_sentiments(tweet_file, sent_dict)

if __name__ == '__main__':
  main()
