import sys
import json

def make_sent_dict(fn):
  lines = [l.strip().split('\t', 2) for l in fn.readlines()]
  sent_dict = {i[0]: int(i[1]) for i in lines}
  return sent_dict

def calc_sent(tweet, sents):
  words = tweet.split()
  sent = 0
  for item in words:
    if item in sents:
      sent = sent + sents[item]
  return sent

def print_term_sentiments(tweets, sents):
  new_terms = {}
  for item in tweets:
    tweet = json.loads(item)
    if 'text' in tweet:
      sent = calc_sent(tweet['text'], sents)
      for word in tweet['text'].split():
        if not word in sents:
          if word in new_terms:
            new_terms[word][1] += 1
            new_terms[word][0] = (new_terms[word][0] + sent)/new_terms[word][1]
          else: 
            new_terms[word] = [sent, 1]
  for i in new_terms:
    print i,
    print new_terms[i][0]

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  sent_dict = make_sent_dict(sent_file)
  print_term_sentiments(tweet_file, sent_dict)

if __name__ == '__main__':
    main()
